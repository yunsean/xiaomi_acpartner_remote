from miio import AirConditioningCompanion, DeviceException
import time

xiaomi = AirConditioningCompanion("192.168.2.237", "1111bee4474f0fa15e2e1c970c78c34e")


print(xiaomi.status())
while True:
    print(xiaomi.send("start_ir_learn", [30]))
    loop = 0
    while xiaomi.send("get_ir_learn_result", []) == ['(null)'] and loop < 15:
        time.sleep(1)
        loop = loop + 1
    if loop >= 15:
        continue
    ir_code = "".join(xiaomi.send("get_ir_learn_result", []))
    if ir_code:
        code_list = list(ir_code)
        code_list[14:26] = '94701FFF96FF'
        sub = ir_code[34:36]
        check = hex(int(sub, 16)-68)[2:]
        if len(check)==1:
            check = '0'+check
        code_list[33:36] = '7'+check
        ir_code = ''.join(code_list)
        print(ir_code)