#! /usr/bin/perl

###### Change to point yours ######

$rundir = "/home/dtalukder/test/ligocam_test/LigoCAM/PEM";
$pubhtmldir = "/home/dtalukder/public_html/test/ligocam_test/LigoCAM/PEM";
$scratchdir = "/usr1/dtalukder/log/ligocam";
$user = "dipongkar.talukder";
$group = "ligo.prod.o2.detchar.chan_mon.ligocam";
$url = "https://ldas-jobs.ligo-wa.caltech.edu/~dtalukder/test/ligocam_test/LigoCAM/PEM";

###################################

$sub = "condor";
$TimeNow = `tconvert now`;
chomp($TimeNow);
$TimeNowSave = $TimeNow;
$TimeStart = $TimeNow-1800;
$TimeStartUTC = `tconvert $TimeStart`;
chomp($TimeStartUTC);
substr($TimeStartUTC, -4) = '';
$TimeStartUTC =~ s/ /_/g;
$TimeEnd = $TimeStart+512;
$TimeEndUTC = `tconvert $TimeEnd -f %H:%M:%S`;
chomp($TimeEndUTC);
$TimeNowUTC = join "", $TimeStartUTC, "-", $TimeEndUTC, "_UTC";
$jobDir = sprintf "%s/jobs/%s", $rundir, $TimeNow;
$mkdirCommand = sprintf "mkdir %s", $jobDir;
system "$mkdirCommand";
$logsdir = sprintf "%s/logs", $jobDir;
$mkdirCommand2 = sprintf "mkdir %s", $logsdir;
system "$mkdirCommand2";
$ymdh = `tconvert $TimeNow -f %Y%m%d%H`;
chomp($ymdh);
$hour = `tconvert $TimeNow -f %H`;
chomp($hour);
$month = `tconvert $TimeNow -f %m`;
chomp($month);
$year = `tconvert $TimeNow -f %Y`;
chomp($year);


$dagfile = sprintf "%s/ligocam_analysis.dag",$jobDir;
open(jobfile, "< ${rundir}/channel_files.txt");
open(dag,">$dagfile");
while(<jobfile>) {
    $line = $_;
    chomp($line);
    if($line =~ m|(.*) (.*) (.*) (.*)|)
    {
    ($job,$chanlist,$ifo,$fmtype) = ($1,$2,$3,$4);
    print dag "JOB $job $jobDir/$sub.sub\n";
    print dag "RETRY $job 2\n";
    print dag "VARS $job ";
    print dag "jobNumber=\"$job\" ";
    print dag "channelList=\"$chanlist\" ";
    print dag "ifo=\"$ifo\" ";
    print dag "frameType=\"$fmtype\" ";
    print dag "currTime=\"$TimeNow\" ";
    print dag "currTimeUTC=\"$TimeNowUTC\" ";
    print dag "run_dir=\"$rundir\" ";
    print dag "\n\n";
}
}
$ppjob = $job + 1;
print dag "JOB $ppjob $jobDir/condorpp.sub\n";
print dag "RETRY $ppjob 2\n";
print dag "VARS $ppjob ";
print dag "jobNumber=\"$ppjob\" \n\n";
print dag "PARENT 0 ";
for ($j=1; $j<$job+1; $j=$j+1) {print dag "$j ";}
print dag "CHILD ";
for ($k = $job+1) {print dag "$k ";}
print dag "\n";
close(jobfile);
close(dag);

$subfile = sprintf "%s/condor.sub",$jobDir;
open(consub,">$subfile");
print consub "universe = vanilla\n";
#print consub "universe = local\n";
print consub "executable = $rundir/LigoCAM\n";
print consub "log = $scratchdir/ligocam_$TimeNow\_\$(frameType).log\n";
print consub "error = $logsdir/ligocam_$TimeNow\_\$(channelList).err\n";
print consub "output = $logsdir/ligocam_$TimeNow\_\$(channelList).out\n";
print consub "arguments = \"--channel-list \$(channelList) --ifo \$(ifo) --frame-type \$(frameType) --cur-time \$(currTime) --run-dir \$(run_dir) --cur-utctime \$(currTimeUTC)\"\n";
print consub "request_memory = 3000\n";
print consub "priority = 20\n";
print consub "+LIGOCAM = True\n";
print consub "notification = error\n";
print consub "accounting_group_user = $user\n";
print consub "accounting_group = $group\n";
print consub "queue";
print consub "\n";
close(consub);

$makeImageDir = sprintf "python ${rundir}/LigoCAM_preparedir.py --run-dir ${rundir} --cur-time $TimeNow";
system $makeImageDir;

$Run_datafind_cur = sprintf "python ${rundir}/LigoCAM_datafind.py --ifo $ifo --frame-type $fmtype --cache-group current --run-dir $rundir --cur-time $TimeNow";
system $Run_datafind_cur;
for ($k=0; $k<12; $k=$k+1) {
 $TimeRef = $TimeNow - 3600;
 $Run_datafind_ref = sprintf "python ${rundir}/LigoCAM_datafind.py --ifo $ifo --frame-type $fmtype --cache-group reference --run-dir $rundir --cur-time $TimeRef";
 system $Run_datafind_ref;
 $TimeNow = $TimeRef;
}

$configdir = "${rundir}/config_files/";
$fullchan = sprintf "%s/fullchan.pl",$rundir;
open(jobfile, "< ${rundir}/channel_files.txt");
open(full,">$fullchan");
print full "#! /usr/bin/perl \n\n";
print full "\$copyfiles = \`cat ";
while(<jobfile>) {
    $line = $_;
    chomp($line);
    if($line =~ m|(.*) (.*) (.*) (.*)|)
    {
    ($job,$chanlist,$ifo,$fmtype) = ($1,$2,$3,$4);
    print full "$configdir$chanlist ";
}
}
print full "\> ${rundir}/channel_full.txt\`\; \n\n";
close(jobfile);
close(full);

$chmodit = sprintf "chmod +x ${rundir}/fullchan.pl";
system $chmodit;
$fullCommand = sprintf "${rundir}/fullchan.pl";
@fullResult = ();
@fullResult = `$fullCommand`;
chomp(@fullResult);

$replace = ":";
$replaceby = "_";
$ppfile = sprintf "%s/ligocampp",$jobDir;
$pathto = sprintf "${rundir}/results/";
$result = sprintf "Result";
open(jobfile, "< ${rundir}/channel_full.txt");
open(pp,">$ppfile");
print pp "#! /usr/bin/perl \n\n";
print pp "\$TimeNow = $TimeNowSave\;\n\n";
print pp "\$copyfiles1 = \`cat ";
while(<jobfile>) {
    $line = $_;
    chomp($line);
    if($line =~ m|(.*)|)
    {
    ($chanlist) = ($1);
    $chanlist =~ s/$replace/$replaceby/g;
    print pp "$pathto$result$TimeNowSave\_$chanlist.txt ";
}
}
print pp "\> $pathto$result$TimeNowSave.txt\`\; \n\n";
close(jobfile);

open(jobfile, "< ${rundir}/channel_full.txt");
print pp "\$deletefiles1 = \`rm -r ";
while(<jobfile>) {
    $line = $_;
    chomp($line);
    if($line =~ m|(.*)|)
    {
    ($chanlist) = ($1);
    $chanlist =~ s/$replace/$replaceby/g;
    print pp "$pathto$result$TimeNowSave\_$chanlist.txt ";
}
}
print pp "\`\; \n\n";

$disconn = sprintf "Disconnected";
$disconnnow = sprintf "Disconnected_now";
print pp "\$copyfiles2 = \`cat ";
close(jobfile);
open(jobfile, "< ${rundir}/channel_full.txt");
while(<jobfile>) {
    $line = $_;
    chomp($line);
    if($line =~ m|(.*)|)
    {
    ($chanlist) = ($1);
    $chanlist =~ s/$replace/$replaceby/g;
    print pp "$pathto$disconn$TimeNowSave\_$chanlist.txt ";
}
}
print pp "\> $pathto$disconnnow.txt\`\; \n\n";

print pp "\$deletefiles2 = \`rm -r ";
close(jobfile);
open(jobfile, "< ${rundir}/channel_full.txt");
while(<jobfile>) {
    $line = $_;
    chomp($line);
    if($line =~ m|(.*)|)
    {
    ($chanlist) = ($1);
    $chanlist =~ s/$replace/$replaceby/g;
    print pp "$pathto$disconn$TimeNowSave\_$chanlist.txt ";
}
}
print pp "\`\; \n\n";

$daqf = sprintf "DAQfailure";
$daqfnow = sprintf "DAQfailure_now";
print pp "\$copyfiles3 = \`cat ";
close(jobfile);
open(jobfile, "< ${rundir}/channel_full.txt");
while(<jobfile>) {
    $line = $_;
    chomp($line);
    if($line =~ m|(.*)|)
    {
    ($chanlist) = ($1);
    $chanlist =~ s/$replace/$replaceby/g;
    print pp "$pathto$daqf$TimeNowSave\_$chanlist.txt ";
}
}
print pp "\> $pathto$daqfnow.txt\`\; \n\n";

print pp "\$deletefiles3 = \`rm -r ";
close(jobfile);
open(jobfile, "< ${rundir}/channel_full.txt");
while(<jobfile>) {
    $line = $_;
    chomp($line);
    if($line =~ m|(.*)|)
    {
    ($chanlist) = ($1);
    $chanlist =~ s/$replace/$replaceby/g;
    print pp "$pathto$daqf$TimeNowSave\_$chanlist.txt ";
}
}
print pp "\`\; \n\n";
close(jobfile);


$disconnmail = sprintf "Disconnmail";
print pp "\$copyfiles4 = \`cat ";
open(jobfile, "< ${rundir}/channel_full.txt");
while(<jobfile>) {
    $line = $_;
    chomp($line);
    if($line =~ m|(.*)|)
    {
    ($chanlist) = ($1);
    $chanlist =~ s/$replace/$replaceby/g;
    print pp "$pathto$disconnmail$TimeNowSave\_$chanlist.txt ";
}
}
print pp "\> $pathto$disconnmail.txt\`\; \n\n";

print pp "\$deletefiles4 = \`rm -r ";
close(jobfile);
open(jobfile, "< ${rundir}/channel_full.txt");
while(<jobfile>) {
    $line = $_;
    chomp($line);
    if($line =~ m|(.*)|)
    {
    ($chanlist) = ($1);
    $chanlist =~ s/$replace/$replaceby/g;
    print pp "$pathto$disconnmail$TimeNowSave\_$chanlist.txt ";
}
}
print pp "\`\; \n\n";

$daqfailmail = sprintf "DAQfailmail";
print pp "\$copyfiles5 = \`cat ";
close(jobfile);
open(jobfile, "< ${rundir}/channel_full.txt");
while(<jobfile>) {
    $line = $_;
    chomp($line);
    if($line =~ m|(.*)|)
    {
    ($chanlist) = ($1);
    $chanlist =~ s/$replace/$replaceby/g;
    print pp "$pathto$daqfailmail$TimeNowSave\_$chanlist.txt ";
}
}
print pp "\> $pathto$daqfailmail.txt\`\; \n\n";

print pp "\$deletefiles5 = \`rm -r ";
close(jobfile);
open(jobfile, "< ${rundir}/channel_full.txt");
while(<jobfile>) {
    $line = $_;
    chomp($line);
    if($line =~ m|(.*)|)
    {
    ($chanlist) = ($1);
    $chanlist =~ s/$replace/$replaceby/g;
    print pp "$pathto$daqfailmail$TimeNowSave\_$chanlist.txt ";
}
}
print pp "\`\; \n\n";
close(jobfile);


$PathTo = sprintf "${rundir}/results";
print pp "\$Movehistfile = sprintf \"python $rundir\/Movehistory_files.py --run-dir \'$rundir\'\"\;\n";
print pp "system \$Movehistfile\; \n\n";
print pp "\$FindChanAlert = sprintf \"python $rundir\/FindChannelAlerts.py --file \'$PathTo\/Result\' --dir \'$pathto\' --name \'Result_sorted\' --cur-time \$TimeNow\"\;\n";
print pp "system \$FindChanAlert\; \n\n";
print pp "\$FindChanAlert2 = sprintf \"python $rundir\/FindChannelAlerts2.py --file \'$PathTo\/Result_sorted\' --dir \'$pathto\' --name \'Result_sorted_2_\' --cur-time \$TimeNow\"\;\n";
print pp "system \$FindChanAlert2\;\n\n";
print pp "\$copyfiles = sprintf \"python $rundir\/CopyFilestopublichtml.py --run-dir \'$rundir\' --pubhtml-dir \'$pubhtmldir\' --cur-time \$TimeNow\"\;\n";
print pp "system \$copyfiles\;\n\n";
print pp "\$MakeHTML = sprintf \"python $rundir\/LigoCamHtml.py --cur-time \$TimeNow --run-dir \'$rundir\' --pubhtml-dir \'$pubhtmldir\' --pub-url \'$url\' --cur-utctime $TimeNowUTC\"\;\n";
print pp "system \$MakeHTML\;\n\n";
print pp "\$editfile = sprintf \"python $rundir\/LigoCAMeditCalendar.py --cur-time \$TimeNow --ymdh-string $ymdh --hour-string $hour --month-string $month --pubhtml-dir \'$pubhtmldir\' --pub-url \'$url\' --year-string $year\"\;\n";
print pp "system \$editfile\;\n\n";
print pp "\$sendalertemail = sprintf \"${rundir}/send_email $TimeNowSave $TimeNowUTC\"\;\n";
print pp "system \$sendalertemail\;\n\n";
close(pp);

$subfilepp = sprintf "%s/condorpp.sub",$jobDir;
open(consubpp,">$subfilepp");
print consubpp "universe = local\n";
print consubpp "executable = $jobDir/ligocampp\n";
print consubpp "log = $scratchdir/ligocampp_$TimeNow.log\n";
print consubpp "error = $logsdir/ligocampp_$TimeNow.err\n";
print consubpp "output = $logsdir/ligocampp_$TimeNow.out\n";
print consubpp "priority = 20\n";
print consubpp "notification = error\n";
print consubpp "accounting_group_user = $user\n";
print consubpp "accounting_group = $group\n";
print consubpp "queue";
print consubpp "\n";
close(consubpp);

chdir "$jobDir";
$chmodit = sprintf "chmod +x ligocampp";
system $chmodit;
$condorCommand = sprintf "condor_submit_dag ligocam_analysis.dag";
@condorResult = ();
@condorResult = `$condorCommand`;
chomp(@condorResult);
