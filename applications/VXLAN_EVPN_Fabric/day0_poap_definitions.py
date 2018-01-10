import json
from credentials import URL, CERT, LOGIN, PASSWORD
from fabric_data import FABRIC
from dcnmtoolkit import Session, POAPDefinition
from templates import POAP_LEAF_TMPL, POAP_SPINE_TMPL, POAP_SPINE_DCI_TMPL, POAP_LEAF_DCI_TMPL
import logging

logging.getLogger(__name__)


def main(url=None, cert=None):
    """My Main"""
    poap_url = '/rest/poap/definitions'
    template_name = None
    params = None
    session = Session(url, LOGIN, PASSWORD, logging_lvl='INFO', verify=cert)
    session.login()

    for node in FABRIC:
        if node['tier'] is 'Spine':
            template_name = 'IPFabric_N9K_Spine_10_2_1_ST_1_TAG'
            params = POAP_SPINE_TMPL['templateDetails'][0]['templateParams']
        elif node['tier'] is 'DatacenterCore':
            template_name = 'IPFabric_N9K_Spine_10_2_1_ST_1_TAG_DCI'
            params = POAP_SPINE_DCI_TMPL['templateDetails'][0]['templateParams']
        elif node['tier'] is 'BorderGateway':
            template_name = 'IPFabric_N9K_Leaf_10_2_1_ST_1_TAG_DCI'
            params = POAP_LEAF_DCI_TMPL['templateDetails'][0]['templateParams']
        elif node['tier'] is 'Leaf' or node['tier'] is 'BorderLeaf':
            template_name = 'IPFabric_N9K_Leaf_10_2_1_ST_1_TAG'
            params = POAP_LEAF_TMPL['templateDetails'][0]['templateParams']

        if params and template_name:
            poap = POAPDefinition(attributes=node, params=params, template_name=template_name)
            resp = session.post(poap_url, json.dumps(poap.definition))
            logging.info('HTTP POST response %s' % resp)
            # print json.dumps(poap.definition, indent=4)


if __name__ == "__main__":
    main(url=URL['url2'], cert=CERT['cert2'])
