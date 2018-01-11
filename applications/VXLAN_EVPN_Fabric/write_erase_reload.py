from credentials import URL, CERT, LOGIN, PASSWORD
from fabric_data import FABRIC
from dcnmtoolkit import Session
import logging
import json

logging.getLogger(__name__)


def yes_no(answer):
    yes = ['yes', 'y', 'ye', ]
    no = ['no', 'n', ''
          ]

    while True:
        choice = raw_input(answer).lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print "Please respond with 'yes' or 'no'\n"


def main(url=None, cert=None):
    """My Main"""
    session = Session(url, LOGIN, PASSWORD, logging_lvl='INFO', verify=cert)
    session.login()

    kaboom = yes_no('Do you want to write erase the fabric: ')

    if kaboom:
        for switch in FABRIC:
            print 'Write Erase / Reload %s' % switch["serialNumber"]
            del_switch(session, switch["serialNumber"])


def del_switch(session, serial_number):
    url = '/rest/poap/switch-definitions/reload/%s' % serial_number
    resp = session.post(url, None)
    logging.info('HTTP POST response %s' % resp)


if __name__ == "__main__":
    main(url=URL['url2'], cert=CERT['cert2'])

