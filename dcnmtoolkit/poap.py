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

    @classmethod
    def get(cls, session):
        url = '/rest/poap/servers'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls(attributes=i)
            resp.append(obj)
        return resp


class SwitchDetails(object):
    def __init__(self, attributes=None, switch_details=None, definitions=None):
        self.attributes = dict()
        self.switch_details = dict()
        if attributes and switch_details:
            self.switch_details = switch_details
            self.attributes = attributes
        elif definitions:
            self.switch_details['switchName'] = None
            self.switch_details['serialNumber'] = None
            self.switch_details['deviceType'] = 'N9K'
            self.switch_details['mgmtIp'] = None
            self.switch_details['username'] = None
            self.switch_details['password'] = None
            self.switch_details['lanGroup'] = None
            self.switch_details['systemImageName'] = None
            self.switch_details['kickstartImageName'] = ''
            self.switch_details['imageServerId'] = 1
            self.switch_details['configServerId'] = 1
            self.switch_details['publish'] = 'true'
            for key, value in definitions.iteritems():
                if key in self.switch_details:
                    self.switch_details[key] = value
            self.attributes = self.switch_details
        else:
            print '''
                Please read Switch definitions from DCNM using get method
                or provide {key:value} to build sw details
                '''

    def get_attributes(self):
        return self.attributes

    def get_details(self):
        return self.switch_details

    @classmethod
    def get(cls, session):
        url = '/rest/poap/switch-definitions'
        ret = session.get(url)
        resp = []
        switch_details_keys = ['switchName', 'serialNumber', 'deviceType', 'mgmtIp',
                               'username', 'password', 'lanGroup', 'systemImageName',
                               'imageServerId', 'configServerId', 'publishStatus']
        for i in ret.json():
            switch_details = {key: i[key] for key in switch_details_keys}
            obj = cls(attributes=i, switch_details=switch_details)
            resp.append(obj)
        return resp


class TemplateDetails(object):
    def __init__(self, attributes=None, template_params=None, definitions=None):
        self.attributes = dict()
        self.template_params = dict()
        if attributes and template_params:
            self.attributes = attributes
            self.template_params = template_params
        elif definitions and template_params:
            self.template_params = template_params
            for key, value in definitions.iteritems():
                if key in self.template_params:
                    self.template_params[key] = value
            self.attributes = self.template_params

    def get_attributes(self):
        return self.attributes

    def get_details(self):
        return self.template_params

    @classmethod
    def get(cls, session):
        url = '/rest/poap/templates?detail=true'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            if 'templateNVPairs' in i:
                template_details = {key: i[key] for key in ['templateNVPairs', 'templateName']}
                template_details['templateParams'] = json.loads(template_details.pop('templateNVPairs'))
                obj = cls(attributes=i, template_params=template_details)
            else:
                obj = cls(attributes=i, template_params=i)
            resp.append(obj)

        return resp


class POAPDefinition(SwitchDetails, TemplateDetails):
    pass
