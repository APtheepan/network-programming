
from device_info import dnac
import requests

header = {'content-type':'application/json',
          'x-auth-token':''}


def login (dnac,port,username,password):
    url = 'https://{}:{}/dna/system/api/v1/auth/token'.format(dnac,port)
    token = requests.request('POST',url,auth = (username,password),verify=False).json()
    return token['Token']

#print(login(dnac['host'],dnac['port'],dnac['username'],dnac['password']))





if __name__ =='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('source_ip',help='Source IP Address')
    parser.add_argument('destination_ip',help='Destination IP Address')
    # A part of the code is not written here
    arg = parser.parse_args()
    source_ip = arg.source_ip
    destination_ip = arg.destination_ip

    print('system is running troubleshoot for')
    print('Source IP {}'.format(source_ip))
    print('Destination IP'.format(destination_ip))
    print('')

    token = login(login(dnac['host'],dnac['port'],dnac['username'],dnac['password']))


