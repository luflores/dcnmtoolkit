import json
from credentials import URL, CERT, LOGIN, PASSWORD
from fabric_data import FABRIC_DEVICE_DEF
from dcnmtoolkit import Session, POAPDefinition
import logging
import requests

requests.packages.urllib3.disable_warnings()

logging.getLogger(__name__)


def main(url=None, cert=None):
    """My Main"""
    update = False
    # session = Session(url, LOGIN, PASSWORD, logging_lvl='INFO', verify=cert)
    session = Session(url, LOGIN, PASSWORD, logging_lvl='INFO', verify=False)
    session.login()

    for fabric, device_definitions in FABRIC_DEVICE_DEF.iteritems():
        url = '/rest/control/fabrics/' + fabric + '/inventory/poap'
        if update:
            session.put(url, json.dumps(device_definitions))
        else:
            session.post(url, json.dumps(device_definitions))


if __name__ == "__main__":
    main(url=URL['url4'], cert=CERT['cert1'])
