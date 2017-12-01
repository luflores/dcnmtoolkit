import json
class CablePlan(object):
    def __init__(self, attributes=None):
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = dict()
            self.attributes['sourceType'] = None
            self.attributes['sourceSwitch'] = None
            self.attributes['destSwitch'] = None
            self.attributes['destType'] = None
            self.attributes['sourcePort'] = None
            self.attributes['destPort'] = None

    def set_sourceType(self, val):
        self.attributes['sourceType'] = val

    def get_sourceType(self):
        return self.attributes['sourceType']

    def set_sourceSwitch(self, val):
        self.attributes['sourceSwitch'] = val

    def get_sourceSwitch(self):
        return self.attributes['sourceSwitch']

    def set_destSwitch(self, val):
        self.attributes['destSwitch'] = val

    def get_destSwitch(self):
        return self.attributes['destSwitch']

    def set_destType(self, val):
        self.attributes['destType'] = val

    def get_destType(self):
        return self.attributes['destType']

    def set_sourcePort(self, val):
        self.attributes['sourcePort'] = val

    def get_sourcePort(self):
        return self.attributes['sourcePort']

    def set_destPort(self, val):
        self.attributes['destPort'] = val

    def get_destPort(self):
        return self.attributes['destPort']

    def get_json(self):
        return json.dumps(self.attributes)


    @classmethod
    def get(cls, session):
        url = '/rest/cable-plans/discovery'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls(attributes=i)
            resp.append(obj)
        return resp
