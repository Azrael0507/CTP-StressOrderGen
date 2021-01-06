#!/bin/sh

g++ -shared -std=c++11 -fPIC  thosttraderapi_wrap.cxx -I./ -I/usr/include/python3.6m -L. -lthosttraderapi_se -o _thosttraderapi.so
