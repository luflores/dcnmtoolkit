import json

class Server(object):
    def __init__(self, attributes=None):
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = dict()
            self.attributes['userName'] = None
            self.attributes['hostName'] = None
            self.attributes['protocol'] = None
            self.attributes['lastUpdateTime'] = None
            self.attributes['url'] = None
            self.attributes['path'] = None
            self.attributes['serverName'] = None
            self.attributes['password'] = None
            self.attributes['id'] = None

    def set_userName(self, val):
        self.attributes['userName'] = val

    def get_userName(self):
        return self.attributes['userName']

    def set_hostName(self, val):
        self.attributes['hostName'] = val

    def get_hostName(self):
        return self.attributes['hostName']

    def set_protocol(self, val):
        self.attributes['protocol'] = val

    def get_protocol(self):
        return self.attributes['protocol']

    def set_lastUpdateTime(self, val):
        self.attributes['lastUpdateTime'] = val

    def get_lastUpdateTime(self):
        return self.attributes['lastUpdateTime']

    def set_url(self, val):
        self.attributes['url'] = val

    def get_url(self):
        return self.attributes['url']

    def set_path(self, val):
        self.attributes['path'] = val

    def get_path(self):
        return self.attributes['path']

    def set_serverName(self, val):
        self.attributes['serverName'] = val

    def get_serverName(self):
        return self.attributes['serverName']

    def set_password(self, val):
        self.attributes['password'] = val

    def get_password(self):
        return self.attributes['password']

    def set_id(self, val):
        self.attributes['id'] = val

    def get_id(self):
        return self.attributes['id']

    def get_json(self):
        return json.dumps(self.attributes)


    @classmethod
    def get(cls, session):
        url = '/rest/poap/servers'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls(attributes=i)
            resp.append(obj)
        return resp

class SwitchDefinition(object):
    def __init__(self, attributes=None):
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = dict()
            self.attributes['username'] = None
            self.attributes['fmServerIp'] = None
            self.attributes['lastConfigServerUpdateTime'] = None
            self.attributes['lastPeerDeviceBindingUpdateTime'] = None
            self.attributes['lanGroup'] = None
            self.attributes['lastPublishStatusUpdateTime'] = None
            self.attributes['switchName'] = None
            self.attributes['isAdminContext'] = None
            self.attributes['id'] = None
            self.attributes['syncStateReason'] = None
            self.attributes['lastBootStatusUpdateTime'] = None
            self.attributes['templateName'] = None
            self.attributes['kickstartImageName'] = None
            self.attributes['poapDeviceCreationTime'] = None
            self.attributes['lastConfigUpdateTime'] = None
            self.attributes['deviceType'] = None
            self.attributes['syncState'] = None
            self.attributes['switchStatus'] = None
            self.attributes['virtualDeviceContextNum'] = None
            self.attributes['imageServerId'] = None
            self.attributes['lastImageUpdateTime'] = None
            self.attributes['lastRecordUpdateTime'] = None
            self.attributes['taskId'] = None
            self.attributes['tier'] = None
            self.attributes['password'] = None
            self.attributes['bootStatus'] = None
            self.attributes['mgmtIp'] = None
            self.attributes['systemImageName'] = None
            self.attributes['serialNumber'] = None
            self.attributes['publishStatus'] = None
            self.attributes['configServerId'] = None

    def set_username(self, val):
        self.attributes['username'] = val

    def get_username(self):
        return self.attributes['username']

    def set_fmServerIp(self, val):
        self.attributes['fmServerIp'] = val

    def get_fmServerIp(self):
        return self.attributes['fmServerIp']

    def set_lastConfigServerUpdateTime(self, val):
        self.attributes['lastConfigServerUpdateTime'] = val

    def get_lastConfigServerUpdateTime(self):
        return self.attributes['lastConfigServerUpdateTime']

    def set_lastPeerDeviceBindingUpdateTime(self, val):
        self.attributes['lastPeerDeviceBindingUpdateTime'] = val

    def get_lastPeerDeviceBindingUpdateTime(self):
        return self.attributes['lastPeerDeviceBindingUpdateTime']

    def set_lanGroup(self, val):
        self.attributes['lanGroup'] = val

    def get_lanGroup(self):
        return self.attributes['lanGroup']

    def set_lastPublishStatusUpdateTime(self, val):
        self.attributes['lastPublishStatusUpdateTime'] = val

    def get_lastPublishStatusUpdateTime(self):
        return self.attributes['lastPublishStatusUpdateTime']

    def set_switchName(self, val):
        self.attributes['switchName'] = val

    def get_switchName(self):
        return self.attributes['switchName']

    def set_isAdminContext(self, val):
        self.attributes['isAdminContext'] = val

    def get_isAdminContext(self):
        return self.attributes['isAdminContext']

    def set_id(self, val):
        self.attributes['id'] = val

    def get_id(self):
        return self.attributes['id']

    def set_syncStateReason(self, val):
        self.attributes['syncStateReason'] = val

    def get_syncStateReason(self):
        return self.attributes['syncStateReason']

    def set_lastBootStatusUpdateTime(self, val):
        self.attributes['lastBootStatusUpdateTime'] = val

    def get_lastBootStatusUpdateTime(self):
        return self.attributes['lastBootStatusUpdateTime']

    def set_templateName(self, val):
        self.attributes['templateName'] = val

    def get_templateName(self):
        return self.attributes['templateName']

    def set_kickstartImageName(self, val):
        self.attributes['kickstartImageName'] = val

    def get_kickstartImageName(self):
        return self.attributes['kickstartImageName']

    def set_poapDeviceCreationTime(self, val):
        self.attributes['poapDeviceCreationTime'] = val

    def get_poapDeviceCreationTime(self):
        return self.attributes['poapDeviceCreationTime']

    def set_lastConfigUpdateTime(self, val):
        self.attributes['lastConfigUpdateTime'] = val

    def get_lastConfigUpdateTime(self):
        return self.attributes['lastConfigUpdateTime']

    def set_deviceType(self, val):
        self.attributes['deviceType'] = val

    def get_deviceType(self):
        return self.attributes['deviceType']

    def set_syncState(self, val):
        self.attributes['syncState'] = val

    def get_syncState(self):
        return self.attributes['syncState']

    def set_switchStatus(self, val):
        self.attributes['switchStatus'] = val

    def get_switchStatus(self):
        return self.attributes['switchStatus']

    def set_virtualDeviceContextNum(self, val):
        self.attributes['virtualDeviceContextNum'] = val

    def get_virtualDeviceContextNum(self):
        return self.attributes['virtualDeviceContextNum']

    def set_imageServerId(self, val):
        self.attributes['imageServerId'] = val

    def get_imageServerId(self):
        return self.attributes['imageServerId']

    def set_lastImageUpdateTime(self, val):
        self.attributes['lastImageUpdateTime'] = val

    def get_lastImageUpdateTime(self):
        return self.attributes['lastImageUpdateTime']

    def set_lastRecordUpdateTime(self, val):
        self.attributes['lastRecordUpdateTime'] = val

    def get_lastRecordUpdateTime(self):
        return self.attributes['lastRecordUpdateTime']

    def set_taskId(self, val):
        self.attributes['taskId'] = val

    def get_taskId(self):
        return self.attributes['taskId']

    def set_tier(self, val):
        self.attributes['tier'] = val

    def get_tier(self):
        return self.attributes['tier']

    def set_password(self, val):
        self.attributes['password'] = val

    def get_password(self):
        return self.attributes['password']

    def set_bootStatus(self, val):
        self.attributes['bootStatus'] = val

    def get_bootStatus(self):
        return self.attributes['bootStatus']

    def set_mgmtIp(self, val):
        self.attributes['mgmtIp'] = val

    def get_mgmtIp(self):
        return self.attributes['mgmtIp']

    def set_systemImageName(self, val):
        self.attributes['systemImageName'] = val

    def get_systemImageName(self):
        return self.attributes['systemImageName']

    def set_serialNumber(self, val):
        self.attributes['serialNumber'] = val

    def get_serialNumber(self):
        return self.attributes['serialNumber']

    def set_publishStatus(self, val):
        self.attributes['publishStatus'] = val

    def get_publishStatus(self):
        return self.attributes['publishStatus']

    def set_configServerId(self, val):
        self.attributes['configServerId'] = val

    def get_configServerId(self):
        return self.attributes['configServerId']

    def get_json(self):
        return json.dumps(self.attributes)


    @classmethod
    def get(cls, session):
        url = '/rest/poap/switch-definitions'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls(attributes=i)
            resp.append(obj)
        return resp

class PoapTemplate(object):
    def __init__(self, attributes=None):
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

    def set_templateNVPairs(self, val):
        self.attributes['templateNVPairs'] = val

    def get_templateNVPairs(self):
        return self.attributes['templateNVPairs']

    def set_lastRecordUpdateTime(self, val):
        self.attributes['lastRecordUpdateTime'] = val

    def get_lastRecordUpdateTime(self):
        return self.attributes['lastRecordUpdateTime']

    def set_templateName(self, val):
        self.attributes['templateName'] = val

    def get_templateName(self):
        return self.attributes['templateName']

    def set_version(self, val):
        self.attributes['version'] = val

    def get_version(self):
        return self.attributes['version']

    def set_poapDeviceId(self, val):
        self.attributes['poapDeviceId'] = val

    def get_poapDeviceId(self):
        return self.attributes['poapDeviceId']

    def set_id(self, val):
        self.attributes['id'] = val

    def get_id(self):
        return self.attributes['id']

    def set_templateContent(self, val):
        self.attributes['templateContent'] = val

    def get_templateContent(self):
        return self.attributes['templateContent']

    def get_json(self):
        return json.dumps(self.attributes)


    @classmethod
    def get(cls, session):
        url = '/rest/poap/templates?detail=true'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls(attributes=i)
            resp.append(obj)
        return resp

