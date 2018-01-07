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


class Switch(object):
    def __init__(self, attributes=None):
        self.attributes = dict()
        if attributes:
            self.attributes = attributes

    @property
    def details(self):
        details_keys = ['switchName', 'serialNumber', 'deviceType', 'mgmtIp',
                        'username', 'password', 'lanGroup', 'systemImageName',
                        'imageServerId', 'configServerId', 'publish']
        return {key: self.attributes[key] for key in details_keys}

    @details.setter
    def details(self, attributes):
        self.attributes = dict.fromkeys(['switchName', 'serialNumber', 'deviceType', 'mgmtIp', 'username', 'password',
                                         'lanGroup', 'systemImageName', 'kickstartImageName', 'imageServerId',
                                         'configServerId', 'publish'])
        self.attributes['deviceType'] = 'N9k'
        self.attributes['publish'] = 'true'
        self.attributes['configServerId'] = 1
        self.attributes['deviceType'] = 1
        for key, value in attributes.iteritems():
            if key in self.attributes:
                self.attributes[key] = value

    @classmethod
    def get(cls, session):
        url = '/rest/poap/switch-definitions'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls(attributes=i)
            resp.append(obj)
        return resp


class Template(object):
    def __init__(self, attributes=None):
        self.attributes = dict()
        if attributes:
            self.attributes = attributes

    @property
    def params(self):
        if 'templateNVPairs' in self.attributes:
            template_details = {key: self.attributes[key] for key in ['templateNVPairs', 'templateName']}
            template_params = json.loads(template_details.pop('templateNVPairs'))
            return template_params
        else:
            return self.attributes

    @params.setter
    def params(self, val):
        try:
            attributes, params = val
        except ValueError:
            raise ValueError("Pass an attributes, base_template")
        else:
            for key, value in attributes.iteritems():
                if key in params.keys():
                    params[key] = value
            self.attributes = params

    @classmethod
    def get(cls, session):
        url = '/rest/poap/templates?detail=true'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls(attributes=i)
            resp.append(obj)

        return resp


class POAPDefinition(Switch, Template):
    pass

