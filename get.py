from pysnmp.hlapi import *
from os import *
import index
import oid

ip = index.resp

g = errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
    CommunityData('public'),
    UdpTransportTarget((ip, 161)),
    ContextData(),
    ObjectType(ObjectIdentity(oid.Descr)),
    ObjectType(ObjectIdentity(oid.UpTime)),
    ObjectType(ObjectIdentity(oid.Contact)),
    ObjectType(ObjectIdentity(oid.Number)),
    ObjectType(ObjectIdentity(oid.OperStatus)),
    ObjectType(ObjectIdentity(oid.Forwarding)),
    ObjectType(ObjectIdentity(oid.InReceives)),
    ObjectType(ObjectIdentity(oid.CurrentEstab)),

               ),

)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:

    print (g)
