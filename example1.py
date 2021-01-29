__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

import device_info
from ncclient import manager


def connect(router,addre, por, user, passw, boolien):
    with manager.connect(host=router[addre], port=router[por], username=router[user],
                            password=router[passw], hostkey_verify=boolien) as m:
        print("here are the capabilities")
        for capability in m.server_capabilities:
            print(capability)






connect( device_info.ios_xe1 ,'address','port', 'username', 'password', False)
