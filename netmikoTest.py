
from netmiko import ConnectHandler

router = {'device_type':'cisco.xr',
          'Host':'10.10.10.2',
          'user':'root',
          'pass':'cisco123'}

net_connection = ConnectHandler(ip = router['Host'],
                                username = router['user'],
                                password =  router['pass'],
                                device_type= router['device_type'])
cli_command = net_connection.send_command('sh ip int br')
print(cli_command)

