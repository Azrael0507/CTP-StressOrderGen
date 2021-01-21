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
autoprocess=0 #是否自动执行，回避所有步骤中的暂停，1为完全自动，用于远程部署；0为非自动，用于本地观察调试

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


tinit-scripts:
用于修改CTP初始化csv文件的脚本工具，放置到tinit的trade用户下即可使用,两个脚本基于上期技术相关脚本基础上进行修改
ChangeTradingAccount.sh：修改全客户可用资金，确保压测有充足资金支持
ChangePW.sh：修改客户密码、最后密码修改时间、最后登录时间（密码修改为：1qa2ws3ed，也调整了最后密码修改时间与最后登录时间，防止出现首次登录密码需要修改的问题）

multitools:
本脚本包实现多台部署、查看、启动以及暂停功能，以下为部署脚本包注意事项：
1、建议机制放置在配置完毕的ctp config主机的trade用户目录下，方便通过信任关系直接访问其他机器
2、调整menu.cfg，其中base_dir为脚本包自身所在目录，而directory_name为脚本包文件夹下，分发工具的文件夹名字，以实例代码为例，进行程序分发时，实际是将本地的 /home/trade/multitools/651-release/目录分发出去
3、调整iplist，其中可以写config机器可以直接访问的机器名字，也可以配置可以直接访问的ip地址
4、调整范例651-release目录下的config.ini文件与investorlist.txt文件，其中特别注意config.ini中的autoprocess需要配置为1，表示自动执行，不用人工干预
5、本版本建议压测策略为，将config.ini中的前置地址配置为127.0.0.1的本地环回地址，工具分别分发到每台front机器上，可以实现对每台front机器自身的压力测试功能
6、项目release界面提供单独版本测试工具下载，以及651版本的多台部署工具下载