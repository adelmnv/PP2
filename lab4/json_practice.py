import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

interface_data = []
for obj in data["imdata"]:
    obj_dict = {
        "dn" : obj["l1PhysIf"]["attributes"]["dn"],
        "descr" : obj["l1PhysIf"]["attributes"]["descr"],
        "speed" : obj["l1PhysIf"]["attributes"]["speed"],
        "mtu" : obj["l1PhysIf"]["attributes"]["mtu"]
    }
    interface_data.append(obj_dict)

print("Interface Status")
print("=" * 87)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 87)
for data in interface_data:
    print("{:<50} {:<20} {:<10} {:<10}".format(data["dn"], data["descr"], data["speed"], data["mtu"]))



#dn descr speed mtu