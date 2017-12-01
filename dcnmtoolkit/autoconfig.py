import json
import json
import logging


class BaseObject(object):

    def get_json(self):
        return json.dumps(self._generate_attributes())

class Org(BaseObject):
    def __init__(self, name):
        self.organizationName = name

    def _generate_attributes(self):
        attributes = dict()
        attributes['organizationName'] = self.organizationName
        return attributes
    #
    # def _get_url_extension(self):
    #     return '/%s' % self.organizationName


    def get_url(self):
        return '/rest/auto-config/organizations'

    def get_json(self):
        return json.dumps(self._generate_attributes())
    #
    # @classmethod
    # def _get_parent_url(cls):
    #     return '/rest/auto-config/organizations'

    @classmethod
    def _from_json(cls, item):
        obj = cls(item['organizationName'])
        return obj


    @classmethod
    def get(cls, session):
        url = '/rest/auto-config/organizations?detail=True'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls._from_json(i)
            resp.append(obj)
        return resp


    def save(self, session):
        resp = session.push_to_dcnm(self.get_url(), self.get_json())
        return resp

    def delete(self, session):
        resp = session.delete(self.get_url() + '/%s' % self.organizationName)
        return resp

class Partition(BaseObject):
    def __init__(self, name, parent, profile='vrf-common-evpn'):
        self.organizationName = parent.organizationName
        self.partitionName = name
        self.vrfName = self.organizationName + ":" + self.partitionName
        self.vrfProfileName = profile

    def _generate_attributes(self):
        attributes = dict()
        attributes['organizationName'] = self.organizationName
        attributes['partitionName'] = self.partitionName
        attributes['vrfName'] = self.vrfName
        attributes['vrfProfileName'] = self.vrfProfileName
        return attributes

    @classmethod
    def _from_json(cls, item, parent):
        obj = cls(item['partitionName'], parent)

        return obj

    def get_url(self):
        return '/rest/auto-config/organizations/%s/partitions' % (self.organizationName)


    def save(self, session):
        resp = session.push_to_dcnm(self.get_url(), self.get_json())
        return resp


    def delete(self, session):
        resp = session.delete(self.get_url() + '/%s' % (self.partitionName))
        return resp

    @classmethod
    def get(cls, session, parent):
        url = parent.get_url() + '/%s/partitions?detail=true' % parent.organizationName
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls._from_json(i, parent)
            resp.append(obj)
        return resp


class Network(BaseObject):
    def __init__(self, name, parent, profile='defaultNetworkEvpnProfile', mobilityDomainId='md0'):
        self.networkName = name
        self.organizationName = parent.organizationName
        self.partitionName = parent.partitionName
        self.vrfName = parent.vrfName
        self.vlanId = None
        self.segmentId = None
        self.profileName = profile
        self.mobilityDomainId = mobilityDomainId
        self.configargs = ''
        self.gateway = ''
        self.netmaskLength = ''

    @property
    def configArg(self):
        arg = '$vlanId=%s;' \
              '$segmentId=%s;' \
              '$vrfName=%s:%s;'  \
              '$gatewayIpAddress=%s;'  \
              '$netMaskLength=%s;'  \
              '$dhcpServerAddr=;' \
              '$vrfDhcp=;' \
              '$gatewayIpv6Address=;' \
              '$prefixLength=;' \
              '$mtuValue=;' % (self.vlanId, self.segmentId, self.organizationName, self.partitionName, self.gateway,
                               self.netmasklength)

              #'$include_vrfSegmentId=50000'
        return arg


    def set_gateway(self, gw):
        gateway = gw.split('/')[0]
        self.gateway = gateway
        mask = gw.split('/')[1]
        self.netmasklength = mask

    def save(self, session):
        resp = session.push_to_dcnm(self.get_url(), self.get_json())
        return resp



    def _generate_attributes(self):
        attributes = dict()
        attributes['organizationName'] = self.organizationName
        attributes['partitionName'] = self.partitionName
        attributes['vrfName'] = self.vrfName
        attributes['networkName'] = self.networkName
        attributes['vlanId'] = self.vlanId
        attributes['segmentId'] = self.segmentId
        attributes['profileName'] = self.profileName
        attributes['mobilityDomainId'] = self.mobilityDomainId
        attributes['configArg'] = self.configArg
        attributes['netmaskLength'] = self.netmasklength
        attributes['gateway'] = self.gateway

        return attributes

    def get_url(self):
        return '/rest/auto-config/organizations/%s/partitions/%s/networks' % (self.organizationName,
                                                                              self.partitionName)

    @classmethod
    def get(cls, session, parent):
        url = parent.get_url() + '/%s/networks?detail=true' % parent.partitionName
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls.from_json(i, parent)
            resp.append(obj)
        return resp


    def save(self, session):
        resp = session.push_to_dcnm(self.get_url(), self.get_json())
        return resp


    def delete(self, session):
        resp = session.delete(self.get_url() + '/segment/%s' % (self.segmentId))
        return resp

    @classmethod
    def from_json(cls, item, parent):
        obj = cls(item['networkName'], parent)
        return obj


class Profile(object):
    def __init__(self, attributes=None):
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = dict()
            self.attributes['profileSubType'] = None
            self.attributes['configCommands'] = None
            self.attributes['profileType'] = None
            self.attributes['description'] = None
            self.attributes['profileName'] = None
            self.attributes['forwardingMode'] = None
            self.attributes['editable'] = None
            self.attributes['modifyTimestamp'] = None

    def set_profileSubType(self, val):
        self.attributes['profileSubType'] = val

    def get_profileSubType(self):
        return self.attributes['profileSubType']

    def set_configCommands(self, val):
        self.attributes['configCommands'] = val

    def get_configCommands(self):
        return self.attributes['configCommands']

    def set_profileType(self, val):
        self.attributes['profileType'] = val

    def get_profileType(self):
        return self.attributes['profileType']

    def set_description(self, val):
        self.attributes['description'] = val

    def get_description(self):
        return self.attributes['description']

    def set_profileName(self, val):
        self.attributes['profileName'] = val

    def get_profileName(self):
        return self.attributes['profileName']

    def set_forwardingMode(self, val):
        self.attributes['forwardingMode'] = val

    def get_forwardingMode(self):
        return self.attributes['forwardingMode']

    def set_editable(self, val):
        self.attributes['editable'] = val

    def get_editable(self):
        return self.attributes['editable']

    def set_modifyTimestamp(self, val):
        self.attributes['modifyTimestamp'] = val

    def get_modifyTimestamp(self):
        return self.attributes['modifyTimestamp']

    def get_json(self):
        return json.dumps(self.attributes)

    @classmethod
    def get(cls, session, name=None):
        if name:
            url = '/rest/auto-config/profiles/%s' % name
            ret = session.get(url)
            obj = cls(attributes=ret.json())
            return obj
        else:
            url = '/rest/auto-config/profiles?detail=true'
            ret = session.get(url)
            resp = []
            for i in ret.json():
                obj = cls(attributes=i)
                resp.append(obj)
            return resp

    def __str__(self):
        return self.get_profileName()

class AutoConfigSettings(object):
    def __init__(self, attributes=None):
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = dict()
            self.attributes['vrfName'] = None
            self.attributes['isSelectiveHA'] = None
            self.attributes['useLocalDhcp'] = None
            self.attributes['ldapPassWord'] = None
            self.attributes['xmppGroup'] = None
            self.attributes['xmppResponseTimeout'] = None
            self.attributes['xmppSearch'] = None
            self.attributes['xmppUserName'] = None
            self.attributes['amqpExchangeName'] = None
            self.attributes['isTopDown'] = None
            self.attributes['globalAnycastGatewayMAC'] = None
            self.attributes['isHA'] = None
            self.attributes['coreDynamicVlans'] = None
            self.attributes['translateVlans'] = None
            self.attributes['enableAmqpNotification'] = None
            self.attributes['ldapUserName'] = None
            self.attributes['xmppPassWord'] = None
            self.attributes['globalMobilityDomain'] = None
            self.attributes['dhcpPrimarySubnet'] = None
            self.attributes['amqpPort'] = None
            self.attributes['xmppServer'] = None
            self.attributes['amqpServer'] = None
            self.attributes['enableSecureLDAP'] = None
            self.attributes['systemDynamicVlans'] = None
            self.attributes['partitionIdRange'] = None
            self.attributes['selectiveHAFeature'] = None
            self.attributes['segmentIdRange'] = None
            self.attributes['ldapServer'] = None
            self.attributes['amqpPassWord'] = None
            self.attributes['amqpUserName'] = None
            self.attributes['amqpVirtualHost'] = None

    def set_vrfName(self, val):
        self.attributes['vrfName'] = val

    def get_vrfName(self):
        return self.attributes['vrfName']

    def set_isSelectiveHA(self, val):
        self.attributes['isSelectiveHA'] = val

    def get_isSelectiveHA(self):
        return self.attributes['isSelectiveHA']

    def set_useLocalDhcp(self, val):
        self.attributes['useLocalDhcp'] = val

    def get_useLocalDhcp(self):
        return self.attributes['useLocalDhcp']

    def set_ldapPassWord(self, val):
        self.attributes['ldapPassWord'] = val

    def get_ldapPassWord(self):
        return self.attributes['ldapPassWord']

    def set_xmppGroup(self, val):
        self.attributes['xmppGroup'] = val

    def get_xmppGroup(self):
        return self.attributes['xmppGroup']

    def set_xmppResponseTimeout(self, val):
        self.attributes['xmppResponseTimeout'] = val

    def get_xmppResponseTimeout(self):
        return self.attributes['xmppResponseTimeout']

    def set_xmppSearch(self, val):
        self.attributes['xmppSearch'] = val

    def get_xmppSearch(self):
        return self.attributes['xmppSearch']

    def set_xmppUserName(self, val):
        self.attributes['xmppUserName'] = val

    def get_xmppUserName(self):
        return self.attributes['xmppUserName']

    def set_amqpExchangeName(self, val):
        self.attributes['amqpExchangeName'] = val

    def get_amqpExchangeName(self):
        return self.attributes['amqpExchangeName']

    def set_isTopDown(self, val):
        self.attributes['isTopDown'] = val

    def get_isTopDown(self):
        return self.attributes['isTopDown']

    def set_globalAnycastGatewayMAC(self, val):
        self.attributes['globalAnycastGatewayMAC'] = val

    def get_globalAnycastGatewayMAC(self):
        return self.attributes['globalAnycastGatewayMAC']

    def set_isHA(self, val):
        self.attributes['isHA'] = val

    def get_isHA(self):
        return self.attributes['isHA']

    def set_coreDynamicVlans(self, val):
        self.attributes['coreDynamicVlans'] = val

    def get_coreDynamicVlans(self):
        return self.attributes['coreDynamicVlans']

    def set_translateVlans(self, val):
        self.attributes['translateVlans'] = val

    def get_translateVlans(self):
        return self.attributes['translateVlans']

    def set_enableAmqpNotification(self, val):
        self.attributes['enableAmqpNotification'] = val

    def get_enableAmqpNotification(self):
        return self.attributes['enableAmqpNotification']

    def set_ldapUserName(self, val):
        self.attributes['ldapUserName'] = val

    def get_ldapUserName(self):
        return self.attributes['ldapUserName']

    def set_xmppPassWord(self, val):
        self.attributes['xmppPassWord'] = val

    def get_xmppPassWord(self):
        return self.attributes['xmppPassWord']

    def set_globalMobilityDomain(self, val):
        self.attributes['globalMobilityDomain'] = val

    def get_globalMobilityDomain(self):
        return self.attributes['globalMobilityDomain']

    def set_dhcpPrimarySubnet(self, val):
        self.attributes['dhcpPrimarySubnet'] = val

    def get_dhcpPrimarySubnet(self):
        return self.attributes['dhcpPrimarySubnet']

    def set_amqpPort(self, val):
        self.attributes['amqpPort'] = val

    def get_amqpPort(self):
        return self.attributes['amqpPort']

    def set_xmppServer(self, val):
        self.attributes['xmppServer'] = val

    def get_xmppServer(self):
        return self.attributes['xmppServer']

    def set_amqpServer(self, val):
        self.attributes['amqpServer'] = val

    def get_amqpServer(self):
        return self.attributes['amqpServer']

    def set_enableSecureLDAP(self, val):
        self.attributes['enableSecureLDAP'] = val

    def get_enableSecureLDAP(self):
        return self.attributes['enableSecureLDAP']

    def set_systemDynamicVlans(self, val):
        self.attributes['systemDynamicVlans'] = val

    def get_systemDynamicVlans(self):
        return self.attributes['systemDynamicVlans']

    def set_partitionIdRange(self, val):
        self.attributes['partitionIdRange'] = val

    def get_partitionIdRange(self):
        return self.attributes['partitionIdRange']

    def set_selectiveHAFeature(self, val):
        self.attributes['selectiveHAFeature'] = val

    def get_selectiveHAFeature(self):
        return self.attributes['selectiveHAFeature']

    def set_segmentIdRange(self, val):
        self.attributes['segmentIdRange'] = val

    def get_segmentIdRange(self):
        return self.attributes['segmentIdRange']

    def set_ldapServer(self, val):
        self.attributes['ldapServer'] = val

    def get_ldapServer(self):
        return self.attributes['ldapServer']

    def set_amqpPassWord(self, val):
        self.attributes['amqpPassWord'] = val

    def get_amqpPassWord(self):
        return self.attributes['amqpPassWord']

    def set_amqpUserName(self, val):
        self.attributes['amqpUserName'] = val

    def get_amqpUserName(self):
        return self.attributes['amqpUserName']

    def set_amqpVirtualHost(self, val):
        self.attributes['amqpVirtualHost'] = val

    def get_amqpVirtualHost(self):
        return self.attributes['amqpVirtualHost']

    def get_json(self):
        return json.dumps(self.attributes)


    @classmethod
    def get(cls, session):
        url = '/rest/auto-config/settings'
        ret = session.get(url)
        obj = cls(attributes=ret.json())
        return obj
