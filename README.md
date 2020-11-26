# AutomationTTnode
甜糖自动收取星星推送微信
使用方法：server酱那张图可以看怎么获取自己的sckey（需要绑定微信，需要gihub账号登录，地址：http://sc.ftqq.com/）（有问题可以进群找三只松鼠问，有空就给你回答）
\n比如我把ttnodeConfig.py和sendTTnodeMSG.py两个文件放在了/root目录下
\n那么我先运行  python /root/ttnodeConfig.py      按照提示输入手机号码和验证码和sckey。
\n然后我再运行  python /root/sendTTnodeMSG.py   ,然后查看微信时候有消息推送。
\n有推送证明已经成功了。

op的请把下面的定时规则添加到计划任务。其它armbian或其它linux的请运行crontab -e 把下面的规则添加进去。
\n15 1 * * *的意思是每天的1点15分执行这个命令，可以自行修改时间。
\n15 1 * * * python /root/sendTTnodeMSG.py

以上命令由于环境不一样，命令不一样，如果提示python 命令找不到的，请把上面命令中的python改成python3

openwrt（f大）:这个固件是自带python环境的。（如果没有urlib3，请运行pip install urlib3或pip3 install urlib3）
armbian：需要自己安装python3和pip和urllib3，百度一般都能找得到。

运行date命令，查看一下系统时间和北京时间是否一致。不一致需要自己百度修改时区和时间。否则定时任务时间点不对。

感谢热心网友提供的armbian下搭建python3环境的命令：（热心网友小贤恩山ID：y2k008）
apt-get update && apt-get install -y python3-pip && pip3 install urllib3       #理论适用于具有apt安装包管理工具的所有linux。需要把系统时间改成和本地一样，不然定时任务时间对不上
复制代码
安装好环境了之后，就走上面的教程，上面教程的命令上面的需要把python改成python3
