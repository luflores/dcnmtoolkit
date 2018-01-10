

class Topology(object):
    def __init__(self, attributes=None):
        self.sw_attributes = attributes

    @classmethod
    def get(cls, session):
        url = '/fm/fmrest/topology?detail=true'
        ret = session.get(url)
        obj = cls(attributes=ret.json())
        return obj
