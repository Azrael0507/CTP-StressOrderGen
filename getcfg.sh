#!/bin/bash
#Usage: ./getcfg.sh {parameter}

# Error Code:
# 1:menu.cfg not exist
# 2:menu.cfg exist repeated parameter
# 3:usage error
# 4:unknow parameter

#检查配置文件是否存在
if [ ! -f menu.cfg ]
then
	echo "menu.cfg not exist!"
	exit 1
fi

#检查配置文件是否正常
rep_cnt=` cat menu.cfg|awk -F= '{print $1}'|tr -s '\n'|uniq -d|wc -l`
rep=` cat menu.cfg|awk -F= '{print $1}'|tr -s '\n'|uniq -d`
if [[ $rep_cnt -ne 0 ]]
then
	echo "menu.cfg exist repeated parameter '$rep'"
	exit 2
fi

#检查用法是否正确
if [[ $1 = "" ]]
then
	echo "Usage: ./getcfg.sh {parameter}"
	exit 3
fi

n=0
IFS='='
while read k v
do
	if [[ $k = $1 ]]
	then
		n=`expr $n + 1`
		echo $v
	fi
done < menu.cfg

#echo $n
if [[ $n -eq 0 ]]
then
	echo "unknow parameter '$1'"
	exit 4
fi
