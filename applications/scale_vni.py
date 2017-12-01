#!/usr/bin/env python
from dcnmtoolkit import Org, Partition, Network
from dcnmtoolkit import Session

# Change these
URL = 'http://10.255.176.8'
LOGIN = 'admin'
PASSWORD = 'cisco123'

orgs = [{'name':'org1', 'partitions': [
                                {'name': 'partition1',
                                  'networks': [{'name' : 'net101','segment': '101'},
                                               {'name' : 'net102','segment': '102'}]
                                 },
                                 {'name': 'partition2',
                                  'networks': [{'name': 'net103', 'segment': '103'}]
                                  }
                                ]

        },
        {'name': 'org2',  'partitions': [
                                     {'name': 'partition3',
                                      'networks': [{'name' : 'net104','segment': '104'},
                                                   {'name' : 'net105','segment': '105'},]
                                     },
                                     {'name': 'partition4',
                                      'networks': [{'name': 'net106', 'segment': '106'}]
                                      }
                                ]

        }
    ]



def create_network(data):
    session = Session(URL, LOGIN, PASSWORD)
    session.login()

    # create org
    print 'Creating org %s' % data['name']
    org = Org(data['name'])
    org.save(session)


    # create partitions
    for partition in data['partitions']:
        print 'Creating paritition %s' % partition['name']
        part = Partition(partition['name'], org)
        part.save(session)
        for network in partition['networks']:
            print 'Creating Network %s' % network['name']
            num = network['segment']
            gw = '{0}.{0}.{0}.1/24'.format(num)
            vni = '{0}{0}'.format(num)
            vlan = '2{}'.format(num)
            n = Network('net{}'.format(num), part)
            n.set_gateway(gw)
            n.segmentId = vni
            n.vlanId = vlan
            n.save(session)



def delete_network(data):
    session = Session(URL, LOGIN, PASSWORD)
    session.login()

    # create org

    org = Org(data['name'])

    # create partitions
    for partition in data['partitions']:

        part = Partition(partition['name'], org)
        part.save(session)
        for network in partition['networks']:
            print 'Deleting Network %s' % network['name']
            num = network['segment']
            vni = '{0}{0}'.format(num)
            n = Network('net{}'.format(num), part)
            n.segmentId = vni
            n.delete(session)
        print 'Deleting paritition %s' % partition['name']
        part.delete(session)
    print 'Deleting org %s' % data['name']
    org.delete(session)


for org in orgs:
    create_network(org)
