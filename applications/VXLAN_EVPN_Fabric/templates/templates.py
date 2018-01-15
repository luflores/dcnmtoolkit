
LAN_FABRIC_TMPL = \
    {
        'generalSetting': {
            'asn': None,
            'deviceType': 'n9k',
            'fabricType': 'VXLANFabric',
            'multicastSetting': {
                'anycastAddress': None,
                'multicastGroupAddress': None,
                'rpCount': '2',
                'rps': [
                    {
                        'id': '1',
                        'phantomAddress': None
                    },
                    {
                        'id': '2',
                        'phantomAddress': None
                    }
                ]
            },
            'networkExtensionTemplate': 'Default_Network_Extension',
            'networkTemplate': 'Default_Network',
            'provisionOption': 'DCNMTopDown',
            'replicationOption': 'MulticastReplication',
            'siteId': 3,
            'vrfExtensionTemplate': 'Default_VRF_Extension',
            'vrfTemplate': 'Default_VRF'
        },
        'name': None,
        'poolSetting': {
            'partitionIdPool': [
                {
                    'orchestrator': 'Default',
                    'range': '30030-30039',
                    'type': 'Default'
                },
                {
                    'orchestrator': 'L3PartitionID',
                    'range': '30003-30009',
                    'type': 'L3PartitionID'
                }
            ],
            'segmentIdPool': [
                {
                    'orchestrator': 'Default',
                    'range': '20200-20299',
                    'type': 'Default'
                },
                {
                    'orchestrator': 'L2SegmentID',
                    'range': '20100-20199',
                    'type': 'L2SegmentID'
                }
            ],
            'vlanRanges': {
                'detectableVlanRanges': [
                    {
                        'detectableVlanRange': 'default',
                        'globalMobilityDomain': 'true',
                        'mobilityDomainName': 'md0'
                    }
                ],
                'dot1qRange': '2-511',
                'networkVlanRange': '100-101,200-299',
                'vrfVlanRange': '3-9,30-39'
            }
        }
    }

POAP_LEAF_TMPL = \
    {
        'switchDetails': [
            {
                'switchName': None,
                'serialNumber': None,
                'deviceType': 'N9K',
                'mgmtIp': None,
                'username': None,
                'password': None,
                'lanGroup': None,
                'systemImageName': None,
                'kickstartImageName': '',
                'imageServerId': 1,
                'configServerId': 1,
                'publish': 'true'
            }
        ],
        'templateDetails': [
            {
                'templateName': 'IPFabric_N9K_Leaf_10_2_1_ST_1',
                'templateParams':
                    {
                        'SWITCH_NAME': None,
                        'ADMIN_USERNAME': None,
                        'ADMIN_PASSWORD': None,
                        'MANAGEMENT_VRF': 'management',
                        'MGMT_IP': None,
                        'MGMT_PREFIX': None,
                        'DEFAULT_GATEWAY': None,
                        'MGMT_V6IP': '',
                        'MGMT_V6PREFIX': '64',
                        'DEFAULT_V6GATEWAY': '',
                        'ENABLE_INBAND_MGMT_POAP': 'false',
                        'INBAND_PORT': '',
                        'INBAND_L3_INTF_IP': '',
                        'INBAND_L3_INTF_NEXTHOP_IP': '',
                        'DHCP_SERVER_IPADDR': '',
                        'DHCP2_SERVER_IPADDR': '',
                        'CONSOLE_TIMEOUT': '0',
                        'CONSOLE_SPEED': '9600',
                        'VTY_TIMEOUT': '0',
                        'IS_TOP_DOWN': 'true',
                        'ENABLE_SECURE_LDAP': 'false',
                        'LDAP_SERVER_IP': '',
                        'LDAP_SERVER_IPV6': '',
                        'LDAP_SERVER_NAME': '',
                        'LDAP2_SERVER_IP': '',
                        'LDAP2_SERVER_IPV6': '',
                        'LDAP2_SERVER_NAME': '',
                        'LDAP_USERNAME': 'reader',
                        'LDAP_PASSWORD': 'fabr1c',
                        'OU_BASE': 'dc=Default_LAN,dc=cisco,dc=com',
                        'LDAP_ENABLE_STRING': '',
                        'SNMP_SERVER_IP': '',
                        'SNMP2_SERVER_IP': '',
                        'AAA_TYPE': 'none',
                        'AAA_SERVER': '',
                        'AAA2_SERVER': '',
                        'AAA_SECRET': '',
                        'DNS_SERVER': '',
                        'DNS2_SERVER': '',
                        'SYSLOG_SERVER': '{\'SYSLOG_SERVER\':}',
                        'NTP_SERVER': '172.31.7.5',
                        'PRIMARY_NTP_SERVER': '172.31.7.5',
                        'TIMEZONE': 'PST -8 0',
                        'DST': 'PDT 1 Sunday March 02:00 1 Sunday November 02:00 60',
                        'ENABLE_NGOAM': 'true',
                        'LINK_STATE_ROUTING': 'ospf',
                        'IP_FABRIC_NET': 'auto',
                        'ipaddressstring': '',
                        'gen_address': '',
                        'LOOPBACK0_IP': None,
                        'LOOPBACK1_IP': None,
                        'LOOPBACK1_SECONDARY_IP': '',
                        'BGP_AS': None,
                        'BGP_RR_IP': None,
                        'BGP_RR_IP2': None,
                        'ANYCAST_MAC': None,
                        'REPLICATION_MODE': 'MulticastReplication',
                        'ANYCAST_RP_IP': None,
                        'RP_GROUP': None,
                        'ENABLE_VMTRACKER': 'false',
                        'VCENTER_CONNECTIONS': '{\'VCENTER_CONNECTIONS\':}',
                        'ENABLE_AUTO_PULL': 'false',
                        'ENABLE_EVB': 'false',
                        'MOBILITY_DOMAIN': 'md0',
                        'SYS_DYN_VLANS': '2500-3500',
                        'CORE_DYN_VLANS': '2500-2999',
                        'BREAKOUT_ARRAY': '{\'BREAKOUT_ARRAY\':}',
                        'FABRIC_INTERFACES': None,
                        'P2PFABRIC_INTERFACES': '{\'P2PFABRIC_INTERFACES\':}',
                        'FABRIC_INTERFACE_PREFIX': '',
                        'FEX_ARRAY': '{\'FEX_ARRAY\':}',
                        'FEX_BRINGUP': '290',
                        'IS_FEX_USED': '',
                        'HOST_INTERFACES': '',
                        'HOST_VLANS': 'all',
                        'ACCESS_PORTS': '{\'ACCESS_PORTS\':}',
                        'BPDUGUARD_INTERFACES': '',
                        'VPC_HOSTS': '{\'VPC_HOSTS\':}',
                        'PORT_CHANNEL_HOSTS': '{\'PORT_CHANNEL_HOSTS\':}',
                        'PC_MODE': 'on',
                        'UNUSED_INTERFACES': '',
                        'ONE_GIG_INTERFACES': '',
                        'ENABLE_VPC': 'false',
                        'VPC_DOMAIN_ID': '',
                        'AUTO_RECOVERY': '240',
                        'VPC_PEER_LINK_PORT_CHANNEL_NUMBER': '',
                        'VPC_PEER_LINK_IF_NAMES': '',
                        'VPC_PEER_LINK_VLAN': '',
                        'VPC_PEER_LINK_IP': '',
                        'VPC_PEER_LINK_PREFIX': '30',
                        'VPC_KEEP_ALIVE_INTF_OPT': 'management',
                        'VPC_KEEP_ALIVE_LOCAL_IP': '',
                        'VPC_KEEP_ALIVE_PEER_IP': '',
                        'KEEP_ALIVE_PREFIX': '',
                        'VPC_KEEP_ALIVE_INTF': '',
                        'KEEP_ALIVE_VRF': 'default'
                    }
            }
        ]
    }

POAP_SPINE_TMPL = \
    {
        'switchDetails': [
            {
                'switchName': None,
                'serialNumber': None,
                'deviceType': 'N9K',
                'mgmtIp': None,
                'username': None,
                'password': None,
                'lanGroup': None,
                'systemImageName': None,
                'kickstartImageName': '',
                'imageServerId': 1,
                'configServerId': 1,
                'publish': 'true'
            }
        ],
        'templateDetails': [
            {
                "templateName": "IPFabric_N9K_Spine_10_2_1_ST_1",
                "templateParams":
                    {
                        "SWITCH_NAME": None,
                        "ADMIN_USERNAME": None,
                        "ADMIN_PASSWORD": None,
                        "MANAGEMENT_VRF": "management",
                        "MGMT_IP": None,
                        "MGMT_PREFIX": "24",
                        "DEFAULT_GATEWAY": None,
                        "MGMT_V6IP": "",
                        "MGMT_V6PREFIX": "64",
                        "DEFAULT_V6GATEWAY": "",
                        "CONSOLE_TIMEOUT": "0",
                        "CONSOLE_SPEED": "9600",
                        "VTY_TIMEOUT": "0",
                        "SNMP_SERVER_IP": "",
                        "SNMP2_SERVER_IP": "",
                        "AAA_TYPE": "none",
                        "AAA_SERVER": "",
                        "AAA2_SERVER": "",
                        "AAA_SECRET": "",
                        "DNS_SERVER": "",
                        "DNS2_SERVER": "",
                        "SYSLOG_SERVER": "{\"SYSLOG_SERVER\":}",
                        "NTP_SERVER": "172.31.7.5",
                        "DHCP_SERVER_IPADDR": "",
                        "DHCP2_SERVER_IPADDR": "",
                        "PRIMARY_NTP_SERVER": "172.31.7.5",
                        "TIMEZONE": "PST -8 0",
                        "DST": "PDT 1 Sunday March 02:00 1 Sunday November 02:00 60",
                        "ENABLE_NGOAM": 'true',
                        "LINK_STATE_ROUTING": "ospf",
                        "IP_FABRIC_NET": "auto",
                        "ipaddressstring": "",
                        "gen_address": "",
                        "LOOPBACK0_IP": None,
                        "BGP_AS": "65501",
                        "BGP_RR_IP": None,
                        "BGP_RR_IP2": None,
                        "BGP_CLIENT_SUBNET": None,
                        "REPLICATION_MODE": "MulticastReplication",
                        "RP_GROUP": None,
                        "ANYCAST_RP_IP": None,
                        "RPARRAY_ASM": None,
                        "BREAKOUT_ARRAY": "{\"BREAKOUT_ARRAY\":}",
                        "FABRIC_INTERFACES": None,
                        "P2PFABRIC_INTERFACES": "{\"P2PFABRIC_INTERFACES\":}",
                        "FABRIC_INTERFACE_PREFIX": "30",
                        "UNUSED_INTERFACES": ""
                    }
            }
        ]
    }

POAP_LEAF_DCI_TMPL = \
    {
        'switchDetails': [
            {
                'switchName': None,
                'serialNumber': None,
                'deviceType': 'N9K',
                'mgmtIp': None,
                'username': None,
                'password': None,
                'lanGroup': None,
                'systemImageName': None,
                'kickstartImageName': '',
                'imageServerId': 1,
                'configServerId': 1,
                'publish': 'true'
            }
        ],
        'templateDetails': [
            {
                'templateName': 'IPFabric_N9K_Leaf_10_2_1_ST_1',
                'templateParams':
                    {
                        'SWITCH_NAME': None,
                        'ADMIN_USERNAME': None,
                        'ADMIN_PASSWORD': None,
                        'MANAGEMENT_VRF': 'management',
                        'MGMT_IP': None,
                        'MGMT_PREFIX': None,
                        'DEFAULT_GATEWAY': None,
                        'MGMT_V6IP': '',
                        'MGMT_V6PREFIX': '64',
                        'DEFAULT_V6GATEWAY': '',
                        'ENABLE_INBAND_MGMT_POAP': 'false',
                        'INBAND_PORT': '',
                        'INBAND_L3_INTF_IP': '',
                        'INBAND_L3_INTF_NEXTHOP_IP': '',
                        'DHCP_SERVER_IPADDR': '',
                        'DHCP2_SERVER_IPADDR': '',
                        'CONSOLE_TIMEOUT': '0',
                        'CONSOLE_SPEED': '9600',
                        'VTY_TIMEOUT': '0',
                        'IS_TOP_DOWN': 'true',
                        'ENABLE_SECURE_LDAP': 'false',
                        'LDAP_SERVER_IP': '',
                        'LDAP_SERVER_IPV6': '',
                        'LDAP_SERVER_NAME': '',
                        'LDAP2_SERVER_IP': '',
                        'LDAP2_SERVER_IPV6': '',
                        'LDAP2_SERVER_NAME': '',
                        'LDAP_USERNAME': 'reader',
                        'LDAP_PASSWORD': 'fabr1c',
                        'OU_BASE': 'dc=Default_LAN,dc=cisco,dc=com',
                        'LDAP_ENABLE_STRING': '',
                        'SNMP_SERVER_IP': '',
                        'SNMP2_SERVER_IP': '',
                        'AAA_TYPE': 'none',
                        'AAA_SERVER': '',
                        'AAA2_SERVER': '',
                        'AAA_SECRET': '',
                        'DNS_SERVER': '',
                        'DNS2_SERVER': '',
                        'SYSLOG_SERVER': '{\'SYSLOG_SERVER\':}',
                        'NTP_SERVER': '172.31.7.5',
                        'PRIMARY_NTP_SERVER': '172.31.7.5',
                        'TIMEZONE': 'PST -8 0',
                        'DST': 'PDT 1 Sunday March 02:00 1 Sunday November 02:00 60',
                        'ENABLE_NGOAM': 'true',
                        'LINK_STATE_ROUTING': 'ospf',
                        'IP_FABRIC_NET': 'auto',
                        'ipaddressstring': '',
                        'gen_address': '',
                        'LOOPBACK0_IP': None,
                        'LOOPBACK1_IP': None,
                        'LOOPBACK1_SECONDARY_IP': '',
                        'BGP_AS': None,
                        'BGP_RR_IP': None,
                        'BGP_RR_IP2': None,
                        'ANYCAST_MAC': None,
                        'REPLICATION_MODE': 'MulticastReplication',
                        'ANYCAST_RP_IP': None,
                        'RP_GROUP': None,
                        'ENABLE_VMTRACKER': 'false',
                        'VCENTER_CONNECTIONS': '{\'VCENTER_CONNECTIONS\':}',
                        'ENABLE_AUTO_PULL': 'false',
                        'ENABLE_EVB': 'false',
                        'MOBILITY_DOMAIN': 'md0',
                        'SYS_DYN_VLANS': '2500-3500',
                        'CORE_DYN_VLANS': '2500-2999',
                        'BREAKOUT_ARRAY': '{\'BREAKOUT_ARRAY\':}',
                        'FABRIC_INTERFACES': None,
                        'P2PFABRIC_INTERFACES': '{\'P2PFABRIC_INTERFACES\':}',
                        'P2PDCI_INTERFACES': None,
                        'FABRIC_INTERFACE_PREFIX': '',
                        'FEX_ARRAY': '{\'FEX_ARRAY\':}',
                        'FEX_BRINGUP': '290',
                        'IS_FEX_USED': '',
                        'HOST_INTERFACES': '',
                        'HOST_VLANS': 'all',
                        'ACCESS_PORTS': '{\'ACCESS_PORTS\':}',
                        'BPDUGUARD_INTERFACES': '',
                        'VPC_HOSTS': '{\'VPC_HOSTS\':}',
                        'PORT_CHANNEL_HOSTS': '{\'PORT_CHANNEL_HOSTS\':}',
                        'PC_MODE': 'on',
                        'UNUSED_INTERFACES': '',
                        'ONE_GIG_INTERFACES': '',
                        'ENABLE_VPC': 'false',
                        'VPC_DOMAIN_ID': '',
                        'AUTO_RECOVERY': '240',
                        'VPC_PEER_LINK_PORT_CHANNEL_NUMBER': '',
                        'VPC_PEER_LINK_IF_NAMES': '',
                        'VPC_PEER_LINK_VLAN': '',
                        'VPC_PEER_LINK_IP': '',
                        'VPC_PEER_LINK_PREFIX': '30',
                        'VPC_KEEP_ALIVE_INTF_OPT': 'management',
                        'VPC_KEEP_ALIVE_LOCAL_IP': '',
                        'VPC_KEEP_ALIVE_PEER_IP': '',
                        'KEEP_ALIVE_PREFIX': '',
                        'VPC_KEEP_ALIVE_INTF': '',
                        'KEEP_ALIVE_VRF': 'default'
                    }
            }
        ]
    }

POAP_SPINE_DCI_TMPL = \
    {
        'switchDetails': [
            {
                'switchName': None,
                'serialNumber': None,
                'deviceType': 'N9K',
                'mgmtIp': None,
                'username': None,
                'password': None,
                'lanGroup': None,
                'systemImageName': None,
                'kickstartImageName': '',
                'imageServerId': 1,
                'configServerId': 1,
                'publish': 'true'
            }
        ],
        'templateDetails': [
            {
                "templateName": "IPFabric_N9K_Spine_10_2_1_ST_1",
                "templateParams":
                    {
                        "SWITCH_NAME": None,
                        "ADMIN_USERNAME": None,
                        "ADMIN_PASSWORD": None,
                        "MANAGEMENT_VRF": "management",
                        "MGMT_IP": None,
                        "MGMT_PREFIX": "24",
                        "DEFAULT_GATEWAY": None,
                        "MGMT_V6IP": "",
                        "MGMT_V6PREFIX": "64",
                        "DEFAULT_V6GATEWAY": "",
                        "CONSOLE_TIMEOUT": "0",
                        "CONSOLE_SPEED": "9600",
                        "VTY_TIMEOUT": "0",
                        "SNMP_SERVER_IP": "",
                        "SNMP2_SERVER_IP": "",
                        "AAA_TYPE": "none",
                        "AAA_SERVER": "",
                        "AAA2_SERVER": "",
                        "AAA_SECRET": "",
                        "DNS_SERVER": "",
                        "DNS2_SERVER": "",
                        "SYSLOG_SERVER": "{\"SYSLOG_SERVER\":}",
                        "NTP_SERVER": "172.31.7.5",
                        "DHCP_SERVER_IPADDR": "",
                        "DHCP2_SERVER_IPADDR": "",
                        "PRIMARY_NTP_SERVER": "172.31.7.5",
                        "TIMEZONE": "PST -8 0",
                        "DST": "PDT 1 Sunday March 02:00 1 Sunday November 02:00 60",
                        "ENABLE_NGOAM": 'true',
                        "LINK_STATE_ROUTING": "ospf",
                        "IP_FABRIC_NET": "auto",
                        "ipaddressstring": "",
                        "gen_address": "",
                        "LOOPBACK0_IP": None,
                        "BGP_AS": "65501",
                        "BGP_RR_IP": None,
                        "BGP_RR_IP2": None,
                        "BGP_CLIENT_SUBNET": None,
                        "REPLICATION_MODE": "MulticastReplication",
                        "RP_GROUP": None,
                        "ANYCAST_RP_IP": None,
                        "RPARRAY_ASM": None,
                        "BREAKOUT_ARRAY": "{\"BREAKOUT_ARRAY\":}",
                        "FABRIC_INTERFACES": None,
                        'P2PDCI_INTERFACES': None,
                        "P2PFABRIC_INTERFACES": "{\"P2PFABRIC_INTERFACES\":}",
                        "FABRIC_INTERFACE_PREFIX": "30",
                        "UNUSED_INTERFACES": ""
                    }
            }
        ]
    }