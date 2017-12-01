#!/usr/bin/env python
from dcnmtoolkit import VTEP
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
    vteps = VTEP.get(session)
    data = []
    for v in vteps:
        data.append((v.switchid, v.ip, v.nve))
    template = "{0:19} {1:20} {2:15}"
    print(template.format("switchId", "ip", "NVE"))
    print(template.format("------", "-----------", "---"))
    for rec in data:
        print(template.format(*rec))


if __name__ == "__main__":
    # execute only if run as a script
    main()