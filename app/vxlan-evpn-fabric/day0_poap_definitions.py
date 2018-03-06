import json
from credentials import URL, CERT, LOGIN, PASSWORD
from fabric_data import FABRIC
from dcnmtoolkit import Session, POAPDefinition
from templates import POAP_LEAF_TMPL, POAP_SPINE_TMPL, POAP_SPINE_DCI_TMPL, \
    POAP_LEAF_DCI_TMPL
import logging

logging.getLogger(__name__)


def main(url=None, cert=None):
    """My Main"""
    update = False
    poap_url = '/rest/poap/definitions'
    template_name = None
    params = None
    session = Session(url, LOGIN, PASSWORD, logging_lvl='INFO', verify=cert)
    session.login()

    for node in FABRIC:
        if node['tier'] is 'Spine':
            template_name = 'LF_Spine'
            params = POAP_SPINE_TMPL['templateDetails'][0]['templateParams']
        elif node['tier'] is 'DatacenterCore':
            template_name = 'LF_DCCore'
            params = POAP_SPINE_DCI_TMPL['templateDetails'][0]['templateParams']
        elif node['tier'] is 'BorderGateway':
            template_name = 'LF_BorderGateway'
            params = POAP_LEAF_DCI_TMPL['templateDetails'][0]['templateParams']
        elif node['tier'] is 'Leaf' or node['tier'] is 'BorderLeaf':
            template_name = 'LF_Leaf'
            params = POAP_LEAF_TMPL['templateDetails'][0]['templateParams']

        if params and template_name:
            poap = POAPDefinition(attributes=node, params=params, template_name=template_name)
            # print json.dumps(poap.definition, indent=4)
            if update:
                session.put(poap_url, json.dumps(poap.definition))
            else:
                session.post(poap_url, json.dumps(poap.definition))


if __name__ == "__main__":
    main(url=URL['url1'], cert=CERT['cert1'])
