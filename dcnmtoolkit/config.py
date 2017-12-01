import json

class ConfigTemplate(object):
    def __init__(self, attributes=None):
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = dict()
            self.attributes['templateType'] = None
            self.attributes['supportedPlatforms'] = None
            self.attributes['description'] = None
            self.attributes['parameters'] = None
            self.attributes['userDefined'] = None
            self.attributes['timestamp'] = None
            self.attributes['published'] = None
            self.attributes['instanceClassId'] = None
            self.attributes['name'] = None
            self.attributes['fileName'] = None

    def set_templateType(self, val):
        self.attributes['templateType'] = val

    def get_templateType(self):
        return self.attributes['templateType']

    def set_supportedPlatforms(self, val):
        self.attributes['supportedPlatforms'] = val

    def get_supportedPlatforms(self):
        return self.attributes['supportedPlatforms']

    def set_description(self, val):
        self.attributes['description'] = val

    def get_description(self):
        return self.attributes['description']

    def set_parameters(self, val):
        self.attributes['parameters'] = val

    def get_parameters(self):
        return self.attributes['parameters']

    def set_userDefined(self, val):
        self.attributes['userDefined'] = val

    def get_userDefined(self):
        return self.attributes['userDefined']

    def set_timestamp(self, val):
        self.attributes['timestamp'] = val

    def get_timestamp(self):
        return self.attributes['timestamp']

    def set_published(self, val):
        self.attributes['published'] = val

    def get_published(self):
        return self.attributes['published']

    def set_instanceClassId(self, val):
        self.attributes['instanceClassId'] = val

    def get_instanceClassId(self):
        return self.attributes['instanceClassId']

    def set_name(self, val):
        self.attributes['name'] = val

    def get_name(self):
        return self.attributes['name']

    def set_fileName(self, val):
        self.attributes['fileName'] = val

    def get_fileName(self):
        return self.attributes['fileName']

    def get_json(self):
        return json.dumps(self.attributes)


    @classmethod
    def get(cls, session, name=None):
        url = '/fmrest/config/templates?detail=true'
        if name:

            url = '/fmrest/config/templates/%s?detail=true' % name
            ret = session.get(url)
            obj = cls(attributes=ret.json())
            return obj

        else:
            ret = session.get(url)
            resp = []
            for i in ret.json():
                obj = cls(attributes=i)
                resp.append(obj)
            return resp