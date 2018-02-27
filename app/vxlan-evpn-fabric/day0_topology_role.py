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
    node_list = topology.__getattribute__('sw_attributes')['nodeList']

    for node in FABRIC:
        found_switch = filter(lambda attribute: attribute['displayName'] == node['switchName'], node_list)
        if found_switch:
            switch_id = found_switch[0]['id']
            url = '/fm/fmrest/topology/role/%s?newRole=%s' % (switch_id, node['role'])
            session.put(url, None)


if __name__ == "__main__":
    main(url=URL['url1'], cert='./dcnm_cert.pem')
