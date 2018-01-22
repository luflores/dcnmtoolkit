from credentials import URL, CERT, LOGIN, PASSWORD
from dcnmtoolkit import Session
import logging
import json
import ipaddress
import math

logging.getLogger(__name__)


def main(url=None, cert=None):
    """My Main"""
    session = Session(url, LOGIN, PASSWORD, logging_lvl='INFO', verify=cert)
    session.login()
    special_keys = ["vrfTemplateConfig", "networkTemplateConfig"]
    ipv4_base = u'1.0.0.1'
    ipv6_base = u'c5c0::1'
    fabrics = ['3', '4']

    overlay = {
        "fabric": "Fab2",
        "vrfExtensionTemplate": "Default_VRF_Extension",
        "vrfId": "30001",
        "vrfName": "OVERLAY1",
        "vrfTemplate": "Default_VRF",
        "vrfTemplateConfig": {
            "asn": "65502",
            "nveId": 1,
            "vrfName": "OVERLAY1",
            "vrfSegmentId": "30001",
            "vrfVlanId": 2
        }
    }
    for fabric in fabrics:
        mcast_grp = '239.255.25' + fabric + '.0'
        for network_id in range(101, 106):
            network_params = {
                "fabric": 'Fab' + str(fabric),
                "networkExtensionTemplate": "Default_Network_Extension",
                "networkId": "20" + str(network_id),
                "networkName": "Network" + str(network_id),
                "networkTemplate": "Default_Network",
                "networkTemplateConfig": {
                    "dhcpServerAddr1": "",
                    "enableIR": False,
                    "gatewayIpAddress": str(ipaddress.IPv4Address(ipv4_base) + 65536 * network_id) + '/22',
                    "gatewayIpV6Address": str(ipaddress.IPv6Address(ipv6_base) + int(math.pow(256, 12)) * network_id) + '/64',
                    "intfDescription": "",
                    "isLayer2Only": False,
                    "mcastGroup": mcast_grp,
                    "mtu": "",
                    "networkName": "Network" + str(network_id),
                    "nveId": 1,
                    "segmentId": "20" + str(network_id),
                    "suppressArp": False,
                    "vlanId": network_id,
                    "vrfDhcp": "",
                    "vrfName": "OVERLAY1"
                },
                "vrf": "OVERLAY1"
            }
            network_params['networkTemplateConfig'] = json.dumps(network_params['networkTemplateConfig'])
            url = '/rest/top-down/fabrics/%s/networks' % ('Fab' + str(fabric))
            resp = session.post(url, json.dumps(network_params))
            if not resp.ok:
                print json.dumps(json.loads(resp.content), indent=4)
            logging.info('HTTP POST response %s' % resp)
            # print json.dumps(network_params, indent=4, sort_keys=True)


if __name__ == "__main__":
    main(url=URL['url1'], cert=CERT['cert1'])
