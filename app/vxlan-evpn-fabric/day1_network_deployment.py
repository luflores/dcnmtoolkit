from credentials import URL, CERT, LOGIN, PASSWORD
from dcnmtoolkit import Session
import logging
import json
import ipaddress
import math
from fabric_data import FABRIC, EXTENSION_VALUES
from collections import defaultdict

logging.getLogger(__name__)
'''

TODO ******** Need to Make this a Class ***********

FABRIC Example Dict Row

P2PDCI_INTERFACES and SYSLOG_SERVER MOst be json.dumps and include as a string. And then the payload can be json.dumps

[
    {
        "ADMIN_PASSWORD": "cisco.123", 
        "ADMIN_USERNAME": "admin", 
        "ANYCAST_RP_IP": "10.250.21.252", 
        "BGP_AS": "65502", 
        "BGP_CLIENT_SUBNET": "10.250.20.0/24", 
        "BGP_RR_IP": "10.250.20.67", 
        "BGP_RR_IP2": "10.250.20.68", 
        "DEFAULT_GATEWAY": "10.0.7.1", 
        "FABRIC_INTERFACES": "e1/05-06", 
        "Fab": "Fab2", 
        "LINK_STATE_ROUTING": "ospf", 
        "LOOPBACK0_IP": "10.250.20.66", 
        "MGMT_IP": "10.0.7.34", 
        "MGMT_PREFIX": "24", 
        "P2PDCI_INTERFACES": {
                                  "P2PDCI_INTERFACES": [
                                      {
                                          "IF_NAME": "e1/01", 
                                          "MTU": "9216"
                                      }, 
                                      {
                                          "IF_NAME": "e1/02", 
                                          "MTU": "9216"
                                      }, 
                                      {
                                          "IF_NAME": "e1/03", 
                                          "MTU": "9216"
                                      }, 
                                      {
                                          "IF_NAME": "e1/04", 
                                          "MTU": "9216"
                                      }
                                  ]
                             }, 
        "RPARRAY_ASM": "{{RP1,10.250.20.67},{RP2,10.250.20.68}}", 
        "RP_GROUP": "239.255.252.0/25", 
        "SWITCH_NAME": "sn2001", 
        "SYSLOG_SERVER": {
                              "SYSLOG_SERVER": [
                                  {
                                      "SYSLOG_SERVER_IP": "10.0.7.60", 
                                      "SYSLOG_SEV": "5"
                                  }, 
                                  {
                                      "SYSLOG_SERVER_IP": "10.0.7.61", 
                                      "SYSLOG_SEV": "5"
                                  }
                              ]
                          }, 
        "lanGroup": 3, 
        "mgmtIp": "10.0.7.34", 
        "password": "cisco.123", 
        "role": "border gateway", 
        "serialNumber": "FOX2114P3LK", 
        "switchName": "sn2001", 
        "systemImageName": "nxos.7.0.3.I7.2.bin", 
        "tier": "DatacenterCore", 
        "username": "admin"
    }
]

'''


def parse_range(astr):
    result = set()
    for part in astr.split(','):
        x = part.split('-')
        result.update(range(int(x[0]), int(x[-1]) + 1))
    return sorted(result)


def build_vrf(session, _fabric, asn, vrf='OVERLAY1', l3vni=1):
    overlay = {
        "fabric": _fabric,
        "vrfExtensionTemplate": "Default_VRF_Extension",
        "vrfId": "3" + format(l3vni, '05d'),
        "vrfName": vrf,
        "vrfTemplate": "Default_VRF",
        "vrfTemplateConfig": {
            "asn": asn,
            "nveId": 1,
            "vrfName": vrf,
            "vrfSegmentId": "3" + format(l3vni, '05d'),
            "vrfVlanId": 3
        }
    }
    overlay['vrfTemplateConfig'] = json.dumps(overlay['vrfTemplateConfig'])
    # print json.dumps(overlay, indent=4)
    url = '/rest/top-down/fabrics/%s/vrfs' % _fabric
    resp = session.post(url, json.dumps(overlay))
    if not resp.ok:
        print json.loads(resp.content)['localizedMessage']
    logging.info('Received response: %s' % resp.status_code)


def build_networks(session, _fabric, vrf, networks, bum, ipv4_base=u'1.0.0.1', ipv4_mask='/22', ipv4_oct=65536,
                   ipv6_base=u'c5c0:1::1', ipv6_mask='/64', ipv6_oct=10, suppress_arp=False, network_id_offset=0):
    networks = parse_range(networks)
    for network_id in networks:
        vlan_id = network_id
        network_id = network_id - network_id_offset
        network_params = {
            "fabric": _fabric,
            "networkExtensionTemplate": "Default_Network_Extension",
            "networkId": "2" + format(vlan_id, '05d'),
            "networkName": "Network" + str(vlan_id),
            "networkTemplate": "Default_Network",
            "networkTemplateConfig": {
                "dhcpServerAddr1": "",
                "enableIR": False,
                "gatewayIpAddress": str(ipaddress.IPv4Address(ipv4_base) + ipv4_oct * network_id) + ipv4_mask,
                "gatewayIpV6Address": str(ipaddress.IPv6Address(ipv6_base) + int(math.pow(256, ipv6_oct)) * network_id) + ipv6_mask,
                "intfDescription": "",
                "isLayer2Only": False,
                "mcastGroup": bum,
                "mtu": "",
                "networkName": "Network" + str(vlan_id),
                "nveId": 1,
                "segmentId": "2" + format(vlan_id, '05d'),
                "suppressArp": suppress_arp,
                "vlanId": vlan_id,
                "vrfDhcp": "",
                "vrfName": vrf
            },
            "vrf": "OVERLAY1"
        }
        network_params['networkTemplateConfig'] = json.dumps(network_params['networkTemplateConfig'])
        # print json.dumps(network_params, indent=4)
        url = '/rest/top-down/fabrics/%s/networks' % _fabric
        resp = session.post(url, json.dumps(network_params))
        if not resp.ok:
            print json.loads(resp.content)['localizedMessage']
        logging.info('Received response: %s' % resp.status_code)


def attach_network(session, vlan, _fabric, _switches, vpc=False, deployment=True, extension_values=""):
    network_attach = []
    if not vpc:
        for switch in _switches:
            switch_base = {"fabric": _fabric,
                           "networkName": "Network" + str(vlan),
                           "serialNumber": switch,
                           "vlan": str(vlan),
                           "dot1QVlan": 1,
                           "untagged": False,
                           "deployment": deployment,
                           "switchPorts": "",
                           "detachSwitchPorts": "",
                           "extensionValues": extension_values
                           }
            network_attach.append({"networkName": "Network" + str(vlan), "lanAttachList": [switch_base]})

    if vpc:
        for vpc_domain, vpc_switches, in _switches.iteritems():
            lan_attach_list = []
            for vpc_switch in vpc_switches:
                vpc_switch_base = {"fabric": _fabric,
                                   "networkName": "Network" + str(vlan),
                                   "serialNumber": vpc_switch,
                                   "vlan": str(vlan),
                                   "dot1QVlan": 1,
                                   "untagged": False,
                                   "deployment": deployment,
                                   "switchPorts": "",
                                   "detachSwitchPorts": "",
                                   "extensionValues": extension_values
                                   }
                lan_attach_list.append(vpc_switch_base)
            network_attach.append({"networkName": "Network" + str(vlan), "lanAttachList": lan_attach_list})

    url = '/rest/top-down/fabrics/%s/networks/attachments' % _fabric
    resp = session.post(url, json.dumps(network_attach))
    if not resp.ok:
        print json.loads(resp.content)['localizedMessage']
    logging.info('Received response: %s' % resp.status_code)
    # print json.dumps(network_attach, indent=4, sort_keys=True)


def deploy_network(session, network, _fabric):
        url = '/rest/top-down/fabrics/%s/networks/deployments' % _fabric
        resp = session.post(url, json.dumps({"networkNames": ("Network" + str(network))}))
        if not resp.ok:
            print json.loads(resp.content)['localizedMessage']
        logging.info('Received response: %s' % resp.status_code)
        # print "BOOM!! I Deployed Network %s" % network


def get_vpc_switches(_fabric):
    _vpc_switches = defaultdict(list)
    for node in FABRIC:
        if node['tier'] == 'Leaf':
            if node['VPC_DOMAIN_ID'] and node['Fab'] == _fabric:
                _vpc_switches[node['VPC_DOMAIN_ID']].append(node["serialNumber"])
    return _vpc_switches


def get_border_gateways(_fabric):
    _border_gateway = []
    for node in FABRIC:
        if node['tier'] == 'BorderGateway' and node['Fab'] == _fabric:
            _border_gateway.append(node["serialNumber"])
    return _border_gateway


def attach_and_deploy(session, _fabric, networks, topology="all", deployment=True):
    networks = parse_range(networks)
    border_gateway = get_border_gateways(_fabric)
    vpc_switches = get_vpc_switches(_fabric)
    for network in networks:
        if topology == "all" or topology == "vpc":
            attach_network(session, network, _fabric, vpc_switches, vpc=True, deployment=deployment)
        if topology == "all" or topology == "bgw":
            attach_network(session, network, _fabric, border_gateway, extension_values=json.dumps(EXTENSION_VALUES),
                           deployment=deployment)
        deploy_network(session, network, _fabric)


def main(url=None, cert=None):
    """My Main"""
    session = Session(url, LOGIN, PASSWORD, logging_lvl='INFO', verify=cert)
    session.login()

    # build_vrf(session, "Fab2", 65502)
    # build_vrf(session, "Fab3", 65503)
    # build_vrf(session, "Fab4", 65504)
    # build_networks(session, "Fab2", 'OVERLAY1', '101-300', 101-300', "239.255.252.1")
    # build_networks(session, "Fab3", 'OVERLAY1', '101-300', 101-300', "239.255.253.1")
    # build_networks(session, "Fab4", 'OVERLAY1', '101-300', 101-300', "239.255.254.1")
    attach_and_deploy(session, "Fab3", '101-132', topology='all', deployment=True)
    attach_and_deploy(session, "Fab4", '101-132', topology='all', deployment=True)
    attach_and_deploy(session, "Fab3", '133-250', topology='vpc', deployment=False)
    attach_and_deploy(session, "Fab4", '251-300', topology='vpc', deployment=False)

    # build_networks(session, "Fab3", 'OVERLAY1', '3000-3002', "239.255.253.1",
    #                ipv4_base=u'1.1.0.1', ipv4_mask='/25', ipv4_oct=256,
    #                ipv6_base=u'fdc5:1f55:71a7:0::1', ipv6_mask='/64', ipv6_oct=8,
    #                network_id_offset=3000)
    #
    # build_networks(session, "Fab4", 'OVERLAY1', '3500-3502', "239.255.253.1",
    #                ipv4_base=u'1.1.0.1', ipv4_mask='/25', ipv4_oct=256,
    #                ipv6_base=u'fdc5:1f55:71a7:0::1', ipv6_mask='/64', ipv6_oct=8,
    #                network_id_offset=3500)
    #
    # attach_and_deploy(session, "Fab3", '3000-3002', topology='vpc', deployment=True)



if __name__ == "__main__":
    main(url=URL['url1'], cert=CERT['cert1'])

