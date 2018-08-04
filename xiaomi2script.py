import json

scripts = open("/tmp/scripts.txt", "w")
with open("/tmp/device.json",'r') as load_f:
    datas = json.load(load_f)
    monitors = datas["Monitors"]
    for monitor in monitors:
        print(monitor)
        print(monitor, file=scripts)
        object = monitors[monitor]
        keyValues = object["KeyValues"]
        for keyValue in keyValues:
            print("  " + keyValue["key"] + ":")
            print("    sequence:")
            print("      - service: remote.send_command")
            print("        data_template:")
            print("          entity_id: remote.ir_remote")
            print("          command: \"raw:" + keyValue["value"] + "\"")
            print("  " + keyValue["key"] + ":", file=scripts)
            print("    sequence:", file=scripts)
            print("      - service: remote.send_command", file=scripts)
            print("        data_template:", file=scripts)
            print("          entity_id: remote.ir_remote", file=scripts)
            print("          command: \"raw:" + keyValue["value"] + "\"", file=scripts)