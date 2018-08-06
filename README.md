
1、custom_components/remote:

The xiaomi air condition partner remote platform allows you to send IR commands from your Xiaomi Air Condition partner.

Please follow the instructions on Retrieving the Access Token to get the API token to use in the configuration.yaml file.

Configuring the Platform
To add a Xiaomi Air Condition partner to your installation, add the following to your configuration.yaml file:

remote:
  - platform: xiaomi_miio
    host: 192.168.42.42
    token: YOUR_TOKEN
CONFIGURATION VARIABLES
host
(string)(Required)The IP of your remote.

token
(string)(Required)The API token of your remote.

name
(string)(Optional)The name of your remote.

slot
(int)(Optional)The slot used to save learned command.

Default value: 1

timeout
(int)(Optional)Timeout for learning a new command.

Default value: 30

hidden
(boolean)(Optional)Hide the entity from UI. There is currently no reason to show the entity in UI as turning it off or on does nothing.

Default value: true

commands
(map)(Optional)

command
(list)(Required)A list of commands as raw (learned command) or pronto hex code.

Other configures same as Xiaomi IR Remote:
https://www.home-assistant.io/components/remote.xiaomi_miio/

2、readkey.py
通过Python的方式让空调伴侣学习遥控码，不过我是把整个python-miio的工程
下载到本地来运行的，直接pip3安装的好像有问题，求python高手指点。
本文件与主题无直接关系，非技术人员请忽略。

3、xiaomi2script.py
借楼保存一下，这个是将从手机上拷贝的米家的空调遥控码转换为小米万能遥控能使用的script使用的一个脚本，请忽略。

