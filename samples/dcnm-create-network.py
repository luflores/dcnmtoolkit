#!/usr/bin/env python
from dcnmtoolkit import Org, Partition, Network
from dcnmtoolkit import Session


try:
    from credentials import URL, LOGIN, PASSWORD
except ImportError:
    print
    print 'To run live tests, please create a credentials.py file with the following variables filled in:'
    print """
    URL = ''
    LOGIN = ''
    PASSWORD = ''
    """

def main():
    session = Session(URL, LOGIN, PASSWORD)
    session.login()

    test = Org('sample-org')
    session.push_to_dcnm(test.get_url(), test.get_json())

    p1 = Partition('sample', test)
    session.push_to_dcnm(p1.get_url(), p1.get_json())
    n1 = Network('net1', p1)
    n1.segmentId = 333
    n1.vlanId = n1.segmentId
    session.push_to_dcnm(n1.get_url(), n1.get_json())


if __name__ == "__main__":
    # execute only if run as a script
    main()