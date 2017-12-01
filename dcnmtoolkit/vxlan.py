__author__ = 'kecorbin'

class VXLANBaseObject(object):
    pass


class VNI(VXLANBaseObject):
    def __init__(self):
        self.status = None
        self.nve = None
        self.switchname = None
        self.mcast = None
        self.switchid = None
        self.Vlan = None
        self.vni = None


    @classmethod
    def from_json(cls, item):
        obj = cls()
        obj.status = item.get('Vni Status', 'None')
        obj.nve = item.get('Nve Interface', 'None')
        obj.switchname = item.get('Switch Name', 'None')
        obj.mcast = item.get('Multicast Address', 'None')
        obj.switchid = item.get('Switch id', 'None')
        obj.Vlan = item.get('Vlan', None)#item['Vlan']
        obj.vni = item.get('Vni', 'None')
        return obj

    def peers(self, session):
        url = '/rest/topology/switches/vxlan/peers?switch-id=%s&vni=%s' % (self.switchid, self.vni)
        resp = session.get(url)
        return resp.json()


class VTEP(VXLANBaseObject):

    def __init__(self, ip=None):
        self.ip = None
        self.switchid = None
        self.nve = None

    @classmethod
    def _get(cls, session, url):
        ret = session.get(url)
        resp = []
        if ('vni' in url) or ('multicast' in url):
            for i in ret.json():
                obj = VNI.from_json(i)
                resp.append(obj)
        else:
            for i in ret.json():
                obj = cls._from_json(i)
                resp.append(obj)
        return resp

    @classmethod
    def get(cls, session, vni=None, mcast=None):
        if vni:
            url = '/rest/topology/switches/vxlan?vni=%s' % str(vni)

        elif mcast:
            url = '/rest/topology/switches/vxlan?multicast-address=%s' % mcast

        else:
            url = '/rest/topology/switches/vxlan/vteps?detail=true'
        resp = cls._get(session, url)
        return resp


    def get_vnis(self, session):
        url = '/rest/topology/switches/vxlan?switch-id=%s' % self.switchid
        resp = []
        ret = session.get(url)

        for i in ret.json():
            obj = VNI.from_json(i)
            resp.append(obj)
        return resp

    @classmethod
    def _from_json(cls, item):
        obj = cls()
        obj.ip = item['Vtep Ip']
        obj.nve = item['Nve Interface']
        obj.switchid = item['Switch Id']
        return obj
