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

    template = "{0:8} {1:10} {2:15} {3:15} {4:15}"
    for v in vteps:
        data = []
        vnis = v.get_vnis(session)
        print "NVE VNI's for switch %s" % vnis[0].switchname
        print "=" * 80
        print ""
        template = "{0:10} {1:10} {2:10} {3:20} {4:10} {5:10} {6:10}"
        print(template.format("Interface", 'Status', "VNI", "Multicast-Group", "Vlan", "SwitchID","Peers"))
        print(template.format("-" * 10, "-" * 10, "-"* 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10))

        for v in vnis:
            data.append((v.nve, v.status, v.vni, v.mcast, v.Vlan, v.switchid, v.peers(session)))

        for rec in data:
            print(template.format(*rec))

        print ""

if __name__ == "__main__":
    # execute only if run as a script
    main()