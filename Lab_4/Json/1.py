import json

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU ")
print("-------------------------------------------------- --------------------  ------  ------")
x = open('test.json')
y = json.load(x)
for i in y["imdata"]:
    print('{0:51} {1:20} {2:8} {3:6}'.format(i["l1PhysIf"]["attributes"]["dn"],i["l1PhysIf"]["attributes"]["descr"],i["l1PhysIf"]["attributes"]["fecMode"],i["l1PhysIf"]["attributes"]["mtu"]))
    