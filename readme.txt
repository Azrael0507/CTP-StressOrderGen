工具说明：
工具用于进行CTP生产版本系统的压力测试，运行环境推荐为redhat/Centos 7.4及以上环境，release版本为二进制程序版本，非release版本为需要python3解释器的原始代码版本。

配置文件说明：
config.ini：
[network]
tradefront=tcp://192.168.88.101:51207 #CTP系统交易前置地址
[authinfo]
appid=client_test.0 #系统内可用的appid
authcode=UFHG9BMEL88G0ZPX #appid对应的认证码
[baseinfo]
brokerid=8080 #CTP系统的经纪公司编号
password=ctptest@123 #investorlist中所有投资者的统一登录密码
[ordercon]
exid=SHFE #报单交易所
instrid=ag2102 #报单合约
orprtype=2 #报单类型，基本不用修改
hedgeflag=1 #投机套保标识，基本不用修改，建议使用有投机交易编码的客户
limitprice=5375 #报单价格
volumetotorg=1 #报单手数
minvol=1 #最小手数
stopprice=0 #不用修改
volumecon=3 #3为一种错误的报单类型，可用于保送到交易所后错误返回，若需要成交，则将报单类型改为1
contingencon=1 #不用修改
[stressconfig]
insertfreq=0.002 #报单间隔秒，一个周期内，所以investorlist文件中的客户，每人报单一次，报单间隔时间后，进入下一个循环

investorlist.txt：
每行一个客户号，不支持注释功能，请特别注意


报单压力逻辑：
报单压力程序会读取investorlist的投资者号，用于登录报单，为了促成成交记录，奇数行的客户号会根据“买开”-》“卖平”-》“买开”的方式进行循环办单，偶数行的客户号会按照“卖开”-》“买平”-》“卖开”的循环方式进行报单。
因此建议配置偶数数量的投资者，保证所有投资者理论上都可以找到对手单，进行撮合成交

程序使用说明：
一切配置正常后，运行程序（config.ini与investorlist在同目录下）
第一步：
程序第一步会进行所有客户的session登录，出现'login end'说明所有客户全部登录完毕，键入回车进入下一步
第二步：
程序对所有登录客户，进行结算单确认操作，出现'settle confirm end'说明全部客户结算单确认完毕，进入回车进入下一步
第三步：
进入无限制的报单循环，使用ctrl+c停止报单，或者寻到pid杀死进程
(二进制版本执行方式：直接赋予执行权限，./执行；python版本执行方式：注意将当前目录加入LD_LIBRARY_PATH中，使用python3 main.py启动程序)