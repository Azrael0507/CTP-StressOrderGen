awk 'BEGIN {FS=","}
{
        if (FNR > 1)
        {
                for (col=1; col<=NF; col++)
                {
                        if (col==5 || col==6)
                        {
                                printf "\042"20000000000.00"\042"
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
}' /home/trade/tinit/perf/t_TradingAccount.csv > t_TradingAccount.csv.tmp

mv t_TradingAccount.csv.tmp /home/trade/tinit/perf/t_TradingAccount.csv
