#!/bin/bash
#����pythonӦ�ó��򼰿��ļ�
cd /tmp
tftp -g -r python2.7.tar.bz2 192.168.51.231
tar -xjf python2.7.tar.bz2 
cd 

#����ִ��pythonǰ�Ļ�������
export PYTHONPATH=/tmp/python2.7/lib/python2.7
export PYTHONHOME=/tmp/python2.7
export PATH=$PATH:/tmp/python2.7/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/tmp/python2.7/lib

#ִ��pythonӦ�ó���
python