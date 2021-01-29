from ncclient.manager import Manager

import device_info
from ncclient import manager
import xmltodict
Open = open('filter-ietf-interfaces.xml')

def connect(router,addre, por, user, passw, boolien):

    with manager.connect(host=router[addre], port=router[por], username=router[user],
                            password=router[passw], hostkey_verify=boolien) as m:
        return m
#print("here are the capabilities")
#for capability in m.server_capabilities:
#    print(capability)


def getinfo(file):
    netconf_reply = file.get(Open)
    intf_detail = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
    intf_config = intf_detail['interfaces']['interface']
    intf_info   = intf_detail['interfaces-state']['interface']

    print("")
    print("Interface Details:")
    print("  Name: {}".format(intf_config["name"]["#text"]))
    print("  Description: {}".format(intf_config["description"]))
    print("  Type: {}".format(intf_config["type"]["#text"]))
    print("  MAC Address: {}".format(intf_info["phys-address"]))
    print("  Packets Input: {}".format(intf_info["statistics"]["in-unicast-pkts"]))
    print("  Packets Output: {}".format(intf_info["statistics"]["out-unicast-pkts"]))



getinfo(connect(device_info.ios_xe1 ,'address','port', 'username', 'password', False))

