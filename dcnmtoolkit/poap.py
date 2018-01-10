import json


class Switch(object):
    def __init__(self, attributes=None):
        self.sw_attributes = attributes

    @property
    def attributes(self):
        return self.sw_attributes

    @property
    def details(self):
        if self.sw_attributes:
            details_keys = ['switchName', 'serialNumber', 'deviceType', 'mgmtIp',
                            'username', 'password', 'lanGroup', 'systemImageName',
                            'imageServerId', 'configServerId', 'publish']
            return {key: self.sw_attributes[key] for key in details_keys}
        else:
            return self.sw_attributes

    @details.setter
    def details(self, attributes):
        self.sw_attributes = dict.fromkeys(['switchName', 'serialNumber', 'deviceType', 'mgmtIp', 'username', 'password',
                                            'lanGroup', 'systemImageName', 'kickstartImageName', 'imageServerId',
                                            'configServerId', 'publish'])
        self.sw_attributes['deviceType'] = 'N9k'
        self.sw_attributes['publish'] = 'true'
        self.sw_attributes['configServerId'] = 1
        self.sw_attributes['imageServerId'] = 1
        for key, value in attributes.iteritems():
            if key in self.sw_attributes:
                self.sw_attributes[key] = value

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
    def __init__(self, attributes=None, params=None, template_name=None):
        self.template_name = template_name
        if params:
            self.params = (attributes, params)
        else:
            self.tmpl_attributes = attributes

    @property
    def attributes(self):
        return self.tmpl_attributes

    @property
    def params(self):
        if self.tmpl_attributes and 'templateNVPairs' in self.tmpl_attributes:
            template_details = {key: self.tmpl_attributes[key] for key in ['templateNVPairs', 'templateName']}
            template_params = json.loads(template_details.pop('templateNVPairs'))
            return template_params
        else:
            return self.tmpl_attributes

    @params.setter
    def params(self, val):
        try:
            attributes, params = val
        except ValueError:
            raise ValueError("Pass an sw_attributes, base_template")
        else:
            for key, value in attributes.iteritems():
                if key in params.keys():
                    params[key] = value
            self.tmpl_attributes = params

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
        def __init__(self, attributes=None, params=None, template_name=None):
            super(Switch, self).__init__()
            super(Template, self).__init__()
            self.details = attributes
            self.params = (attributes, params)
            self.template_name = template_name

        @property
        def definition(self):
            poap_definition = {'switchDetails': [self.details],
                                   'templateDetails': [{'templateName': self.template_name,
                                                        'templateParams': self.params}]}
            return poap_definition


