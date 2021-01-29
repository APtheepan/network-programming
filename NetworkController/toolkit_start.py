
from device_info import apic
from acitoolkit.acitoolkit import *

print(dir())

# in ACI(apic) controller, a session should be created first
session = Session(apic['host'],apic['username'],apic['password'])
# check whether connection is created
# print(session.login())
# print(session.logged_in())

# tenants in the controller could be obtained by quarrying the controller

#tenants = Tenant.get(session)
#print(type(tenants))
data = Tenant('tenant_theepan')
session.push_to_apic(data.get_url(),data.get_json())
data.get_url()
data.get_json()