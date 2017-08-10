#!/bin/sh

####### Change to point yours #######

OBS=LHO
SUBSYS=PEM
BASEDIR=test/ligocam_test/LigoCAM
SCRATCH_DIR=/usr1/dtalukder/log/ligocam

#####################################

RUN_DIR=${HOME}/${BASEDIR}/${SUBSYS}
PUBHTML_DIR=${HOME}/public_html/${BASEDIR}/${SUBSYS}
mkdir -p $RUN_DIR
mkdir -p $PUBHTML_DIR
mkdir -p $SCRATCH_DIR
mkdir -p $RUN_DIR/{jobs,cache,config_file,ref_files,results}
mkdir -p $RUN_DIR/images/{TS,ASD}

GIT_DIR=$(pwd)/GIT
mkdir -p $GIT_DIR
git clone https://github.com/dipongkar/ligocam $GIT_DIR

cp -r $GIT_DIR/ligocam/*.py $RUN_DIR
cp -r $GIT_DIR/bin/LigoCAM $RUN_DIR
cp -r $GIT_DIR/etc/{dag.pl,send_email} $RUN_DIR
cp -r $GIT_DIR/etc/config_files/${SUBSYS}/${OBS}/channelList*.txt $RUN_DIR/config_file
cp -r $GIT_DIR/etc/config_files/${SUBSYS}/${OBS}/channel_files.txt $RUN_DIR
cp -r $GIT_DIR/share/{DAQfailure_default.txt,Disconnected_default.txt} $RUN_DIR/results

cp -r $GIT_DIR/share/calendar $PUBHTML_DIR
mkdir -p $PUBHTML_DIR/{status,pages}
mkdir -p $PUBHTML_DIR/images/{TS,ASD}
cp -r $GIT_DIR/share/{css,js} $PUBHTML_DIR
cp -r $GIT_DIR/share/{css,js} $PUBHTML_DIR/pages
cp -r $GIT_DIR/share/{css,js} $PUBHTML_DIR/status
