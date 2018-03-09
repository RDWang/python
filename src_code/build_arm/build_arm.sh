#!/bin/bash
#配置嵌入式arm
../python-2.7.14/configure --prefix=`pwd` --host=arm-linux-gnueabihf --build=x86_64-linux-gnu  --enable-ipv6 --enable-shared ac_cv_file__dev_ptmx="yes" ac_cv_file__dev_ptc="no" STRIP=arm-linux-gnueabihf-strip 

#编译
make HOSTPYTHON=../build_pc/python HOSTPGEN=../build_pc/Parser/pgen BLDSHARED="arm-linux-gnueabihf-gcc -shared" CROSS_COMPILE=arm-linux-gnueabihf- CROSS_COMPILE_TARGET=yes HOSTARCH=arm-linux-gnueabihf BUILDARCH=x86_64-linux-gnu -j4

#安装
make -i install PYTHONPATH=../build_pc/ HOSTPYTHON=../build_pc/python BLDSHARED="arm-linux-gnueabihf-gcc -shared" CROSS_COMPILE=arm-linux-gnueabihf- CROSS_COMPILE_TARGET=yes prefix=`pwd`

#打包应用程序及文件
if test -d python2.7; then
	rm -fr python2.7
fi
mkdir python2.7
cp -fr bin python2.7/
cp -fr include python2.7/
cp -fr share python2.7/
cp -fr lib python2.7/
tar -cjf python2.7.tar.bz2 python2.7
cp -fr python2.7.tar.bz2 /tftpboot