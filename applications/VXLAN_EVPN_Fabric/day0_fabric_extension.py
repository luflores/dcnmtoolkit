from credentials import URL, CERT, LOGIN, PASSWORD
from fabric_data import FABRIC_EXTENSION
from dcnmtoolkit import Session
import logging
import json

logging.getLogger(__name__)


def main(url=None, cert=None):
    """My Main"""
    session = Session(url, LOGIN, PASSWORD, logging_lvl='INFO', verify=cert)
    session.login()

    add_fab_ext(session)
    # del_fab_ext(session)


def add_fab_ext(session):
    for extension in FABRIC_EXTENSION:
        url = '/rest/top-down/fabrics/%s/vrf-extension' % extension['sourceFabric']
        resp = session.post(url, json.dumps(extension))
        logging.info('HTTP POST response %s' % resp)


def del_fab_ext(session):
    fabric_ext = dict()
    fabric_ext_keys = dict.fromkeys(['sourceFabric', 'sourceSwitch', 'sourcePort', 'destFabric', 'destSwitch',
                                     'destPort', 'extensionType'])
    for extension in FABRIC_EXTENSION:
        for key, value in extension.iteritems():
            if key in fabric_ext_keys:
                fabric_ext[key] = value
        url = '/rest/top-down/fabrics/%s/vrf-extension' % fabric_ext['sourceFabric']
        resp = session.delete(url, json.dumps(fabric_ext))
        logging.info('HTTP POST response %s' % resp)


if __name__ == "__main__":
    main(url=URL['url2'], cert=CERT['cert2'])
