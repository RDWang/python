#!/bin/sh
../python-2.7.14/configure --prefix=`pwd`
make -j4
make install