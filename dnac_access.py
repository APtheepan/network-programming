import sys
from device_info import dnac
import requests
from pprint import pprint
import urllib.request
import urllib.parse

header = {'content-type':'application/json',
          'x-auth-token':''}


def login (dnac,port,username,password):
    url = 'https://{}:{}/dna/system/api/v1/auth/token'.format(dnac,port)
    token = requests.request('POST',url,auth = (username,password),verify=False).json()
    return token['Token']

#print(login(dnac['host'],dnac['port'],dnac['username'],dnac['password']))

def networkDevices(dnac,token):

    url = 'https://{}/dna/intent/api/v1/network-device'.format(dnac)
    header['x-auth-token'] = token
    device = requests.request('GET',url,headers=header,verify=False)
    return device.json()['response']

def host_list(dnac,token,ip=None,mac=None,name=None):

    url = 'https://{}/api/v1/host'.format(dnac)
    header['x-auth-token'] = token
    filter=[]
    if ip != None:
        filter.append('hostIp={}'.format(ip))
    if mac != None:
        filter.append('hostMac={}'.format(mac))
    if name != None:
        filter.append('hostName={}'.format(name))

    if len(filter)>0:
        url +=  '?' + '&'.join(filter)

    hosts = requests.request('GET',url,headers = header,verify = False).json()
    return hosts['response']
def verify_single_host(host,ip):
    if len(host) == 0:
        print('ERROR: No host with ip address {} found'.format(ip))
        sys.exit(1)
    if len(host) >1:
        print('ERROR: many host can not have same ip address {} '.format(ip))
        sys.exit(1)

def print_host_details(host):

    if 'hostName' not in host.keys():
        host['hostName'] = 'unavailable'
    print('Host connectedNetworkDeviceId is {}'.format(host['connectedNetworkDeviceId']))
    if host['hostType'] == 'Wireless':
        print('Host connectedAPName is {}'.format(host['connectedAPName']))

    print('Host hostDeviceType is {}'.format(host['hostDeviceType']))

def network_device_list(dnac,token,id = None ):
    url = 'https://{}/dna/intent/api/v1/network-device'.format(dnac)
    header['x-auth-token'] = token
    if id != None:
        url = url + '/{}'.format(id)
    response = requests.request('GET',url,headers = header,verify = False ).json()
    return response['response']

def print_network_device_list(network_device):
    print("Device Hostname: {}".format(network_device["hostname"]))
    print("Management IP: {}".format(network_device["managementIpAddress"]))
    print("Device Location: {}".format(network_device["locationName"]))
    print("Device Type: {}".format(network_device["type"]))
    print("Platform Id: {}".format(network_device["platformId"]))
    print("Device Role: {}".format(network_device["role"]))
    print("Serial Number: {}".format(network_device["serialNumber"]))
    print("Software Version: {}".format(network_device["softwareVersion"]))
    print("Up Time: {}".format(network_device["upTime"]))
    print("Reachability Status: {}".format(network_device["reachabilityStatus"]))  # noqa: E501
    print("Error Code: {}".format(network_device["errorCode"]))
    print("Error Description: {}".format(network_device["errorDescription"]))


    print("")


def interface_details(dnac,token, id = None):
    url = 'https://{}/dna/intent/api/v1/interface'.format(dnac)
    header['x-auth-token'] = token
    if id != None:
        url = url + '/{}'.format(id)
    response = requests.request('GET',url,headers = header,verify = False).json()
    return response

def print_interface(interface):
    print("Port Name: {}".format(interface["portName"]))
    print("Interface Type: {}".format(interface["interfaceType"]))
    print("Admin Status: {}".format(interface["adminStatus"]))
    print("Operational Status: {}".format(interface["status"]))
    print("Media Type: {}".format(interface["mediaType"]))
    print("Speed: {}".format(interface["speed"]))
    print("Duplex Setting: {}".format(interface["duplex"]))
    print("Port Mode: {}".format(interface["portMode"]))
    print("Interface VLAN: {}".format(interface["vlanId"]))
    print("Voice VLAN: {}".format(interface["voiceVlan"]))


    print("")


def flow_analysis(dnac,token,sourceIP,destinationIp):
    url = "https://{}/dna/intent/api/v1/flow-analysis".format(dnac)
    header["x-auth-token"] = token
    body = {"destIP": destinationIp, "sourceIP": sourceIP}
    initial_response =requests.request('POST',url,headers = header,verify = False,json = body)
    
    print(initial_response.json())




if __name__ =='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('source_ip')
    parser.add_argument('destination_ip')
    # A part of the code is not written here
    arg = parser.parse_args()
    source_ip = arg.source_ip
    destination_ip = arg.destination_ip

    print('system is running troubleshoot for')
    print('Source IP {}'.format(source_ip))
    print('Destination IP {}'.format(destination_ip))
    print('')

    token = login(dnac['host'],dnac['port'],dnac['username'],dnac['password'])
    # devices = networkDevices(dnac['host'],token)
    # for device in devices:
    #     print('host name is {}'.format(device['hostname']))
    #     print('host family is {}'.format(device['family']))
    #     print('host mac address is {}'.format(device['macAddress']))
    #     print('host IP address is {}'.format(device['managementIpAddress']))
    #     print('')
    # source_host = host_list(dnac['host'],token,ip=source_ip)
    # destination_host =host_list(dnac['host'],token,ip=destination_ip)
    # verify_single_host(source_host,source_ip)
    # verify_single_host(destination_host,destination_ip)
    # pprint(source_host)
    # pprint(destination_host)
    #pprint(network_device_list(dnac['host'],token,'72dc1f0a-e4da-4ec3-a055-822416894dd5'))
    flow_analysis(dnac['host'],token,source_ip,destination_ip)





