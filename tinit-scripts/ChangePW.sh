#!/bin/sh


awk 'BEGIN {FS=","}
{
        if (FNR > 1)
        {
                for (col=1; col<=NF; col++)
                {
                        if (col==3)
                        {
                                printf "\042""1qa2ws3ed""\042"
                        }
			else if(col==4)
			{
                                printf "\042"2020123009"\072""00""\072""00""\042"
			}
			else if(col==5)
			{
                                printf "\042"2020123109"\072""00""\072""00""\042"
			}
                        else
                        {
                                printf $col
                        }
                        if (col<NF)
                        {
                                printf ","
                        }
                }
                printf "\n"
        }
        else
        {
                print $0
        }
}' /home/trade/tinit/perf/t_BrokerUserPassword.csv > t_BrokerUserPassword.csv.tmp

mv t_BrokerUserPassword.csv.tmp /home/trade/tinit/perf/t_BrokerUserPassword.csv
