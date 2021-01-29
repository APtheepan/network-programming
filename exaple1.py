

import requests
import json
from pprint import pprint
# requests.packages.urllib3.disable_warnings(
#     requests.packages.urllib3.exceptions.InsecureRequestWarning
# )

"""
Modify these please
"""
url = "https://sbx-nxos-mgmt.cisco.com/ins"
switchuser = "admin"
switchpassword = "Admin_1234!"

myheaders = {"content-type": "application/yang-data+json"}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show vlan bri",
        "output_format": "json",
    }
}
response = requests.post(
    url,
    data=json.dumps(payload),
    headers=myheaders,
    auth=(switchuser, switchpassword),
    verify=False,
).json()

#pprint(response)

vlanlist = response['ins_api']['outputs']['output']['body']['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief']

for vlanid in vlanlist:
    print('this router vlanids are {}'.format(vlanid['vlanshowbr-vlanid']))