from dcnmtoolkit import (Session, Org, Partition, Network, VTEP, VNI, Profile, CablePlan,
                         AutoConfigSettings, ConfigTemplate, Server, SwitchDefinition, PoapTemplate)

import unittest
import json

try:
    from credentials import URL, LOGIN, PASSWORD
except ImportError:
    print
    print 'To run live tests, please create a credentials.py file with the following variables filled in:'
    print """
    URL = ''
    LOGIN = ''
    PASSWORD = ''
    """
TEST_VNI = '11001100'
TEST_MCAST = '225.4.0.2'

MAX_RANDOM_STRING_SIZE = 20


class OfflineTests(unittest.TestCase):

    def test_create_valid_org(self):
        """
        Test basic Org creation
        """
        org = Org(name='testorg')
        data = '{"organizationName": "testorg"}'

        self.assertIsInstance(org, Org)
        self.assertEqual(org.get_json(), data)

    def test_create_org_from_json(self):
        """
        Test basic Org creation
        """
        data = '{"organizationName": "testorg-json"}'
        org = Org._from_json(json.loads(data))


        self.assertIsInstance(org, Org)
        self.assertEqual(org.get_json(), data)

    def test_create_valid_partition(self):
        org = Org(name='testorg')
        part = Partition('test-partition', org)
        self.assertIsInstance(part, Partition)

    def test_create_profile(self):
        p = Profile()
        self.assertIsInstance(p,Profile)

class LiveTestReadOnly(unittest.TestCase):
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_login(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_get_orgs(self):
        orgs = Org.get(self.session())
        self.assertIsInstance(orgs, list)

    def test_get_profiles(self):
        profiles = Profile.get(self.session())
        self.assertIsInstance(profiles, list)


class VXLANReadOnlyTests(unittest.TestCase):

    @property
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_get_vteps(self):
        vteps = VTEP.get(self.session)
        self.assertIsInstance(vteps, list)
        self.assertIsInstance(vteps[0], VTEP)


    def test_get_vnis_for_switch(self):
        vteps = VTEP.get(self.session)
        for vtep in vteps:
            vnis = vtep.get_vnis(self.session)
            self.assertIsInstance(vnis, list)
            has_vni = hasattr(vnis[0], 'vni')
            self.assertTrue(has_vni)

    def test_get_vnis_by_vni(self):
        vnis = VTEP.get(self.session, vni=TEST_VNI)
        has_vni = hasattr(vnis[0], 'vni')
        self.assertTrue(has_vni)

    def test_get_vnis_by_mcast(self):
        vnis = VTEP.get(self.session, mcast=TEST_MCAST)
        has_vni = hasattr(vnis[0], 'vni')
        self.assertTrue(has_vni)
        self.assertIsInstance(vnis, list)

    def test_get_vtep_table(self):
        vteps = VTEP.get(self.session)

        template = "{0:8} {1:10} {2:15} {3:15} {4:15}"
        for v in vteps:
            data = []
            vnis = v.get_vnis(self.session)
            print "NVE VNI's for switch %s" % vnis[0].switchname
            print "=" * 80
            print ""
            template = "{0:10} {1:10} {2:10} {3:20} {4:10} {5:10} {6:10}"
            print(template.format("Interface", 'Status', "VNI", "Multicast-Group", "Vlan", "SwitchID","Peers"))
            print(template.format("-" * 10, "-" * 10, "-"* 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10))

            for v in vnis:
                data.append((v.nve, v.status, v.vni, v.mcast, v.Vlan, v.switchid, v.peers(self.session)))

            for rec in data:
                print(template.format(*rec))

            print ""


class ProfileReadOnlyTests(unittest.TestCase):

    @property
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_get_profiles(self):
        profiles = Profile.get(self.session)
        self.assertIsInstance(profiles, list)

    def test_get_profiles_by_name(self):
        name='vrf-common-evpn'
        profile= Profile.get(self.session, name=name)
        self.assertEqual(str(profile), name)

    def test_get_profile_attributes(self):
        profiles = Profile.get(self.session)
        testprofile = profiles[0]

        for method in dir(profiles[0]):
            if method.startswith('get_'):
                a = getattr(testprofile, method)
                a()

    def test_set_profile_attributes(self):
        profiles = Profile.get(self.session)
        testprofile = profiles[0]

        for method in dir(profiles[0]):
            if method.startswith('set_'):
                a = getattr(testprofile, method)
                a('foo')


class AutoConfigReadWriteTests(unittest.TestCase):

    @property
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_001_create_org(self):
        testorg = Org('unittesting')
        resp = testorg.save(self.session)
        self.assertTrue(resp.ok)

    def test_002_create_partition(self):
        testorg = Org('unittesting')
        testpartition = Partition('p1', testorg)
        resp = testpartition.save(self.session)
        self.assertTrue(resp.ok)

    def test_003_create_network(self):
        testorg = Org('unittesting')
        testpartition = Partition('p1', testorg)
        n1 = Network('net1', testpartition)
        n1.segmentId = 333
        n1.vlanId = n1.segmentId
        n1.set_gateway('10.10.10.2/24')
        n1.vlanId = '124'
        n1.segmentId = '124'
        n1.segmentId = '124'
        resp = n1.save(self.session)



    def test_004_get_partitions(self):
        testorg = Org('unittesting')
        partitions = Partition.get(self.session, testorg)
        self.assertIsInstance(partitions, list)

    def test_005_get_networks(self):
        testorg = Org('unittesting')
        testpartition = Partition('p1', testorg)
        nets = Network.get(self.session, testpartition)
        self.assertIsInstance(nets, list)




    def test_006_delete_network(self):
        testorg = Org('unittesting')
        testpartition = Partition('p1', testorg)
        n1 = Network('net1', testpartition)
        n1.segmentId = 333
        n1.vlanId = n1.segmentId
        n1.set_gateway('10.10.10.2/24')
        n1.vlanId = '124'
        n1.segmentId = '124'
        n1.segmentId = '124'
        resp = n1.delete(self.session)


    def test_007_delete_partition(self):
        testorg = Org('unittesting')
        testpartition = Partition('p1', testorg)
        resp = testpartition.delete(self.session)
        self.assertTrue(resp.ok)

    def test_008_delete_org(self):
        testorg = Org('unittesting')
        resp = testorg.delete(self.session)
        self.assertTrue(resp.ok)

class ConfigReadOnlyTests(unittest.TestCase):

    @property
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_get_config_templates(self):
        templates = ConfigTemplate.get(self.session)
        self.assertIsInstance(templates, list)

    def test_get_template_by_name(self):
        template_name = 'IPFabric_VDC_BorderLeaf_v01'
        template = ConfigTemplate.get(self.session, name=template_name)
        self.assertEqual(template.get_name(), template_name)

    def test_create_blank_template(self):
        t = ConfigTemplate()
        self.assertIsInstance(t, ConfigTemplate)

    def test_get_template_attributes(self):
        templates = ConfigTemplate.get(self.session)
        self.assertIsInstance(templates, list)
        testtemplate = templates[0]

        for method in dir(testtemplate):
            if method.startswith('get_'):
                a = getattr(testtemplate, method)
                a()

    def test_set_template_attributes(self):
        templates = ConfigTemplate.get(self.session)
        testtemplate = templates[0]

        for method in dir(testtemplate):
            if method.startswith('set_'):
                a = getattr(testtemplate, method)
                a('foo')


class CablePlanReadOnlyTests(unittest.TestCase):

    @property
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_create_cable_plan(self):
        cp = CablePlan()
        self.assertIsInstance(cp, CablePlan)

    def test_get_cableplans(self):
        cps = CablePlan.get(self.session)
        self.assertIsInstance(cps, list)
        print "Cable Plans Received"
        for cp in cps:
            print 'Switch {} port {} connected to switch {} port {}'.format(
                                                                    cp.attributes['sourceSwitch'],
                                                                    cp.attributes['sourcePort'],
                                                                    cp.attributes['destSwitch'],
                                                                    cp.attributes['destPort'])
        self.assertIsInstance(cps[0], CablePlan)


    def test_get_cableplan_attributes(self):
        cps = CablePlan.get(self.session)
        testcp = cps[0]

        for method in dir(testcp):
            if method.startswith('get_'):
                a = getattr(testcp, method)
                a()

    def test_set_cableplan_attributes(self):
        cps = CablePlan.get(self.session)
        testcp = cps[0]

        for method in dir(testcp):
            if method.startswith('set_'):
                a = getattr(testcp, method)
                a('foo')


class PoapReadOnlyTests(unittest.TestCase):

    @property
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_create_server(self):
        server = Server()
        self.assertIsInstance(server, Server)

    def test_get_servers(self):
        servers = Server.get(self.session)
        self.assertIsInstance(servers, list)
        self.assertIsInstance(servers[0], Server)


    def test_get_server_attributes(self):
        servers = Server.get(self.session)
        testserver = servers[0]

        for method in dir(testserver):
            if method.startswith('get_'):
                a = getattr(testserver, method)
                a()

    def test_set_server_attributes(self):
        servers = Server.get(self.session)
        testserver = servers[0]

        for method in dir(testserver):
            if method.startswith('set_'):
                a = getattr(testserver, method)
                a('foo')


    def test_create_switchdef(self):
        switchdef = SwitchDefinition()
        self.assertIsInstance(switchdef, SwitchDefinition)

    def test_get_switchdefs(self):
        defs = SwitchDefinition.get(self.session)
        self.assertIsInstance(defs, list)
        self.assertIsInstance(defs[0], SwitchDefinition)


    def test_get_switchdef_attributes(self):
        switchdefs = SwitchDefinition.get(self.session)
        testdef = switchdefs[0]

        for method in dir(testdef):
            if method.startswith('get_'):
                a = getattr(testdef, method)
                a()

    def test_set_switchdef_attributes(self):
        switchdefs = SwitchDefinition.get(self.session)
        testdef = switchdefs[0]

        for method in dir(testdef):
            if method.startswith('set_'):
                a = getattr(testdef, method)
                a('foo')


    def test_get_poap_templates(self):
        poaptemplates = PoapTemplate.get(self.session)

        self.assertIsInstance(poaptemplates, list)
        self.assertIsInstance(poaptemplates[0], PoapTemplate)

    def create_poap_template(self):
        pt = PoapTemplate()


    def test_get_poap_template_attributes(self):
        testobjs = PoapTemplate.get(self.session)
        testobj = testobjs[0]

        for method in dir(testobj):
            if method.startswith('get_'):
                a = getattr(testobj, method)
                a()

    def test_set_poap_template_attributes(self):
        testobjs = PoapTemplate.get(self.session)
        testobj = testobjs[0]

        for method in dir(testobj):
            if method.startswith('set_'):
                a = getattr(testobj, method)
                a('foo')


class SessionTests(unittest.TestCase):

    @property
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_get_version(self):
        session = self.session
        ver = session.version
        print "DCNM Version is %s" % ver
        self.assertIsInstance(ver, unicode)

    def test_get_settings(self):
        ac = self.session.get_settings()
        self.assertIsInstance(ac, AutoConfigSettings)

    def test_bad_url(self):
        url = '/this/is/bogus'
        resp = self.session.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_create_blank_autoconfig(self):
        ac = AutoConfigSettings()
        self.assertIsInstance(ac, AutoConfigSettings)

    def test_get_auto_config_settings(self):
        settings = AutoConfigSettings.get(self.session)
        self.assertIsInstance(settings, AutoConfigSettings)

    def test_get_autoconfig_attributes(self):
        settings = AutoConfigSettings.get(self.session)

        for method in dir(settings):
            if method.startswith('get_'):
                a = getattr(settings, method)
                a()

    def test_set_autoconfig_attributes(self):
        settings = AutoConfigSettings.get(self.session)

        for method in dir(settings):
            if method.startswith('set_'):
                a = getattr(settings, method)
                a('foo')


if __name__ == '__main__':
    readonly = unittest.TestSuite()
    readonly.addTest(LiveTestReadOnly)
    readonly.addTest(ProfileReadOnlyTests)
    readonly.addTest(CablePlanReadOnlyTests)
    readonly.addTest(SessionTests)
    readonly.addTest(ConfigReadOnlyTests)
    readonly.addTest(PoapReadOnlyTests)
    readonly.addTest(VXLANReadOnlyTests)
    readwrite = unittest.TestSuite()
    readwrite.addTest(AutoConfigReadWriteTests)

    offline = unittest.TestSuite()
    offline.addTest(unittest.makeSuite(OfflineTests))

    full = unittest.TestSuite([readonly, readwrite, offline])

    # Add tests to this suite while developing the tests
    # This allows only these tests to be run
    develop = unittest.TestSuite()

    unittest.main(defaultTest='full')
