from credentials import URL, CERT, LOGIN, PASSWORD
from fabric_data import UNDERLAY_FABRIC_EXTENSION, OVERLAY_FABRIC_EXTENSION
from dcnmtoolkit import Session
import logging
import json
import time

logging.getLogger(__name__)


def main(url=None, cert=None):
    """My Main"""
    session = Session(url, LOGIN, PASSWORD, logging_lvl='INFO', verify=cert)
    session.login()

    add_fab_ext(session)
    # del_fab_ext(session)


def add_fab_ext(session):
    for underlay in UNDERLAY_FABRIC_EXTENSION:
        url = '/rest/top-down/fabrics/%s/vrf-extension' % underlay['sourceFabric']
        session.post(url, json.dumps(underlay))
        time.sleep(10)

    for overlay in OVERLAY_FABRIC_EXTENSION:
        url = '/rest/top-down/fabrics/%s/vrf-extension' % overlay['sourceFabric']
        session.post(url, json.dumps(overlay))
        time.sleep(10)


def del_fab_ext(session):
    fabric_ext = dict()
    fabric_ext_keys = dict.fromkeys(['sourceFabric', 'sourceSwitch', 'sourcePort', 'destFabric', 'destSwitch',
                                     'destPort', 'extensionType'])
    for underlay in UNDERLAY_FABRIC_EXTENSION:
        for key, value in underlay.iteritems():
            if key in fabric_ext_keys:
                fabric_ext[key] = value
        url = '/rest/top-down/fabrics/%s/vrf-extension' % fabric_ext['sourceFabric']
        session.delete(url, json.dumps(fabric_ext))
        # time.sleep(10)

    for overlay in OVERLAY_FABRIC_EXTENSION:
        for key, value in overlay.iteritems():
            if key in fabric_ext_keys:
                fabric_ext[key] = value
        url = '/rest/top-down/fabrics/%s/vrf-extension' % fabric_ext['sourceFabric']
        session.delete(url, json.dumps(fabric_ext))
        # time.sleep(10)


if __name__ == "__main__":
    main(url=URL['url1'], cert=CERT['cert1'])


'''s[s.find("(")+1:s.find(")")]'''