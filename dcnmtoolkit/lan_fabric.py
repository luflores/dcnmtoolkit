import json


class LANFabric(object):
    def __init__(self, attributes=None):
        self.lan_fabric_details = dict()
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = dict()
            self.attributes['templateNVPairs'] = None
            self.attributes['lastRecordUpdateTime'] = None
            self.attributes['templateName'] = None
            self.attributes['version'] = None
            self.attributes['poapDeviceId'] = None
            self.attributes['id'] = None
            self.attributes['templateContent'] = None

    def get_json(self):
        return json.dumps(self.attributes)

    def _generate_lan_fabric_details(self):
        self.lan_fabric_details = {
            key: self.attributes[key] for key in ['name', 'generalSetting', 'poolSetting']}
        return self.lan_fabric_details

    def get_details(self):
        return self._generate_lan_fabric_details()

    @classmethod
    def get(cls, session):
        url = '/rest/fabrics?detail=true'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls(attributes=i)
            resp.append(obj)
        return resp


mandatory = {
    "name": "Fab2",
    "description": "Fab2Desc",
    "generalSetting": {
        "fabricType":               "VXLANFabric",
        "deviceType":               "n9k",
        "provisionOption":          "DCNMTopDown",
        "asn":                      "655022",
        "vrfTemplate":              "Default_VRF",
        "networkTemplate":          "Default_Network",
        "vrfExtensionTemplate":     "Default_VRF_Extension",
        "networkExtensionTemplate": "Default_Network_Extension",
        "siteId":                   "22",
        "replicationOption":        "MulticastReplication",
        "multicastSetting": {
            "rpCount":                      "2",
            "multicastGroupAddress":    "239.1.1.0/25",
            "anycastAddress":           "10.2.0.254",
            "rps": [{"id": 1, "phantomAddress": "10.2.0.1"},
                    {"id": 2, "phantomAddress": "10.2.0.2"}]
            }
    },
    "poolSetting": {
        "segmentIdPool": [
            {
                "type":         "Default",
                "orchestrator": "Default",
                "range":        "30000-49999"
            }
        ],
        "partitionIdPool": [
            {
                "type":         "Default",
                "orchestrator": "Default",
                "range":        "50000-60000"
            }
        ],
        "vlanRanges": {
         "vrfVlanRange": "2000-2399",
         "networkVlanRange": "2400-2999",
         "dot1qRange": "2-511",
         "detectableVlanRanges": [
            {
               "mobilityDomainName": "md0",
               "detectableVlanRange": "default",
               "globalMobilityDomain": "true"
            }
         ]
      },
      "miscPool":[

      ]
   }
}

all_params = {
   "name": "Fab2",
   "description": "Fab2Desc",
   "generalSetting": {
      "fabricType": "VXLANFabric",
      "deviceType": "n9k",
      "provisionOption": "DCNMTopDown",
      "replicationOption": "MulticastReplication",
      "asn": "655022",
      "siteId": "222",
      "networkTemplate": "Default_Network",
      "vrfTemplate": "Default_VRF",
      "networkExtensionTemplate": "Default_Network_Extension",
      "vrfExtensionTemplate": "Default_VRF_Extension",
      "multicastSetting": {
         "multicastGroupAddress": "239.1.1.0/25",
         "rpCount": "2",
         "anycastAddress": "10.2.0.254",
         "rps": [
            {
               "id": "1",
               "phantomAddress": "10.2.0.1"
            },
            {
               "id": "2",
               "phantomAddress": "10.2.0.2"
            }
         ]
      }
   },
   "provisionSetting": {
      "amqpSetting": {
         "enableAMQP": "true",
         "server": "10.0.7.58:5672",
         "virtualHost": "/",
         "user": "admin",
         "password": "cisco.123",
         "exchangeName": "DCNMExchange"
      }
   },
   "poolSetting": {
      "segmentIdPool": [
         {
            "type": "Default",
            "range": "30000-49999",
            "orchestrator": "Default"
         }
      ],
      "partitionIdPool": [
         {
            "type": "Default",
            "range": "50000-60000",
            "orchestrator": "Default"
         }
      ],
      "vlanRanges": {
         "vrfVlanRange": "2000-2399",
         "networkVlanRange": "2400-2999",
         "detectableVlanRanges": [
            {
               "mobilityDomainName": "md0",
               "detectableVlanRange": "default",
               "globalMobilityDomain": "true"
            }
         ],
         "dot1qRange": "2-511"
      }
   },
   "borderSetting": {
      "enablePartitionExtension": "false",
      "routeTargetAsn": 65500,
      "loadBalanceAlgorithm": "RoundRobin",
      "redundancyFactor": 2
   }
}
