#!/bin/bash

#base info
path=`./getcfg.sh base_dir`/`./getcfg.sh directory_name`
iplist=`cat iplist|grep -v '#'|uniq -i`


#start iplist
start()
{
	echo "starting Stress tools!"
	echo -e "\n"
	for srv in $iplist
	do
		echo "starting ${srv}"
		ssh $srv "cd $path; nohup ./stressordergen &> /dev/null &"
	done
	echo -e "\n"
	echo "starting tools complete"
}

stop()
{
	echo "stoping Stress tools!"
	echo -e "\n"
	for srv in $iplist
	do
		echo "stoping ${srv}"
		ssh $srv "ps -ef | grep stressordergen | grep -v grep | awk '{print \$2}' | xargs -I {} kill -9 {}"
	done
	echo -e "\n"
	echo "stoping Stress tools complete"
}

show()
{
	echo "show tools status:"
	echo -e "\n"
	for srv in $iplist
	do
		echo "process pid on $srv:"
		ssh $srv "ps -ef | grep stressordergen | grep -v grep | awk '{print \$2}'"
	done
	echo -e "\n"
}

#makedir iplist
makedir()
{
	echo "making remote base path!"
	echo -e "\n"
	for srv in $iplist
	do
		echo "make path in ${srv}"
		ssh $srv "mkdir -p $path"
	done
	echo -e "\n"
	echo "making remote base path complete"
	echo -e "\n"
}

#deploy iplist
deploy()
{
	echo "deploy remote Tools!"
	echo -e "\n"
	for srv in $iplist
	do
		echo "*********scp file to ${srv} ******************"
		scp $path/* $srv:$path
	done
	echo -e "\n"
	echo "deploy remote Tools complete"
	echo -e "\n"
}

menu()
{

while [ 1=1 ]
do
	echo "******************************************"
	echo "**********CTP-StressGenOrder**************"
	echo "******************************************"
	
	echo -e "\n"
	echo "1.Start Stress Process"
	echo "2.Stop Stress Process"
	echo "3.Show Stress Process"
	echo -e "\n"

	echo -e "\n"
	echo "5.deploy Stress Tools"
	echo -e "\n"

	echo -e "\n"
	echo "0.Quit to Shell"
	echo -e "\n"

	echo "******************************************"
	echo "**********thank you for using*************"
	echo "******************************************"

	read -p "please enter your section:" sec

	case $sec in
		"1")
			start
			read -p "press Enter to continue" voidray
			clear
			;;
		"2")
			stop
			read -p "press Enter to continue" voidray
			clear
			;;
		"3")
			show
			read -p "press Enter to continue" voidray
			clear
			;;
		"5")
			makedir
			deploy
			read -p "press Enter to continue" voidray
			clear
			;;
		"0")
			clear
			exit
			read -p "press Enter to continue" voidray
			clear
			;;
		*)
			echo "Don't be hurry~~~~~"
			read -p "press Enter to continue" voidray
			clear
			;;
	esac

done

}

#main {function}
clear
echo $iplist
menu
