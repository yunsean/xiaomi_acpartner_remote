### 主要功能

实现通过空调伴侣控制其他电器。

### 设置方法

* 将xiaomi_acpartner_remote拷贝到home assistant配置目录下的custom_components目录中；
* 添加空调伴侣红外遥控器的的设置项：

``` yaml
remote:
  - platform: xiaomi_acpartner_remote
    host: 192.168.2.xxx
    token: YOUR_TOKEN
    name: "Bedroom Remote"
    slot: 30
    timeout: 30
    hidden: false
```

  - 配置script，实现指定脚本发送红外遥控码控制电器，例子如下：

``` yaml
script:
  bedroom_letv_power:  #红外序列
    sequence:
      - service: remote.send_command
        data_template:
          entity_id: remote.bedroom_remote
          command: "FE00000000000094701FFF96FF08002427080033003B00AA00DC01BD038C1031138854101012120010121002100210010202100202020101110210110110120202101206531715"
      - delay:
          seconds: 1
      - service: remote.send_command
        data_template:
          entity_id: remote.bedroom_remote
          command: "FE00000000000094701FFF96FF0A0027270d000C00320039004000A500DF01C4038810DF13DB76212214242222242124222422222424222424221222212421222124242434223428751908751983"
      - delay:
          seconds: 3
      - service: remote.send_command
        data_template:
          entity_id: remote.bedroom_remote
          command: "FE00000000000094701FFF96FF090024270900310038004000AA00DC01B70389102B13886511111313111103101311131111131301111301231111101103010311131303031764180D"    
  bedroom_letv_switch:  #单独的红外按键
    sequence:
      - service: remote.send_command
        data_template:
          entity_id: remote.bedroom_remote
          command: "FE00000000000094701FFF96FF090024270900310038004000AA00DC01B70389102B13886511111313111103101311131111131301111301231111101103010311131303031764180D"  
```

* 可使用script实现模拟开关，请参考小米万能遥控：https://www.home-assistant.io/components/remote.xiaomi_miio/

### readkey.py使用
通过Python的方式让空调伴侣学习遥控码
* 首先安装miio组件

``` shell
pip3 install python-miio
```

* 使用方法

``` shell
python readkey.py
```

 (注意，如果你的系统中同时存在python2和python3，你可能得使用python3 readkey.py)
然后每次按下一个按键，将显示一行输出，输出内容即是下方所需要的红外码（忽略多余的['ok']行）
比如：

``` shell
C:\Data>python readkey.py
<AirConditioningCompanionStatus power=on, load_power=784, air_condition_model=01
0505770001179701, model_format=1, device_type=5,air_condition_brand=577,air_cond
ition_remote=11797,state_format=1,air_condition_configuration=11311AA1,led=False
, target_temperature=26, swing_mode=SwingMode.Off, fan_speed=FanSpeed.Auto, mode
=OperationMode.Cool>
['ok']
['ok']
FE00000000000094701FFF96FF0600AC278e0035003E00AD01C60348138843020200000000000200
02020000000000000002000000000000020000000200020000000000000000000000000000000004
00000000000000020000000000000000000000000000000000000000000100000000000000020000
00010000000000010100000100010101000202010101000104010101010100010102010201010201
01010101000101010101010000010101010101010101020101020102010201010101010100020001
01057D
['ok']
FE00000000000094701FFF96FF080026270a003600AC00DE01C603861032138825C7430000010100
0001000100010000010100010101010000000000000000010101010542074206C1
['ok']
['ok']
```

#### xiaomi2script.py使用
将从手机上拷贝的米家的空调遥控码转换为小米万能遥控能使用的script使用的一个脚本

