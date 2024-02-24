import json

with open('sample-data.json') as file:
    json_object = json.load(file)

print(
    "=======================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------")

imdata = json_object.get("imdata", [])
for i in imdata[:3]:
    l1_phys_if = i.get("l1PhysIf", {}).get("attributes", {})
    dn = l1_phys_if.get("dn", "")
    descr = l1_phys_if.get("descr", "")
    speed = l1_phys_if.get("speed", "")
    mtu = l1_phys_if.get("mtu", "")
    print("{0:50} {1:20} {2:7} {3:6}".format(dn, descr, speed, mtu))