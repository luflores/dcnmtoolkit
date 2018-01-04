from credentials import URL, CERT, LOGIN, PASSWORD
from fabric_data import FABRIC
from dcnmtoolkit import Session, Topology
import logging

logging.getLogger(__name__)


def main(url=None, cert=None):
    """My Main"""
    session = Session(url, LOGIN, PASSWORD, logging_lvl='INFO', verify=cert)
    session.login()

    topology = Topology.get(session)
    node_list = topology.__getattribute__('attributes')['nodeList']
    fabric_tiers = ['BorderLeaf', 'DatacenterCore', 'Spine', 'Leaf', 'BorderGateway']
    all_switch_definitions = list()
    for fabric_tier in fabric_tiers:
        for sw in FABRIC[fabric_tier]:
            all_switch_definitions.append(sw)

    roles = ['spine', 'leaf', 'border', 'border gateway']
    for role in roles:
        for result in filter(lambda attribute: attribute['newRole'] == role, all_switch_definitions):
            found_switch = filter(lambda attribute: attribute['displayName'] == result['switchName'], node_list)
            if found_switch:
                switch_id = found_switch[0]['id']
                url = '/fm/fmrest/topology/role/%s?newRole=%s' % (switch_id, result['newRole'])
                # logging.info('%s(%s)--role-->%s' % (result['switchName'], switch_id, result['newRole']))
                resp = session.update_dcnm(url, None)
                logging.info('HTTP POST response %s' % resp)


if __name__ == "__main__":
    main(url=URL['url2'], cert=CERT['cert2'])
