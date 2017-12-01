import requests
import json
import logging
from autoconfig import AutoConfigSettings

logging.getLogger(__name__)


class Session(object):

    def __init__(self, url, user, passwd):
        self.base_url = url
        self.user = user
        self.passwd = passwd
        self.headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json; charset=UTF-8'}
        self.token = None
        self.expiration_time = 1000000
        self.settings = None

    def login(self):
        url = self.base_url + '/rest/logon'
        payload = {'expirationTime': self.expiration_time}
        try:
            resp = requests.post(url, auth=(self.user, self.passwd), data=json.dumps(payload))
            if resp.ok:
                logging.info('Successfully logged into %s' % url)
            else:
                logging.error('Could not login to %s: Response: %s' % (url, resp.text))
            self.headers.update(json.loads(resp.text))
            return resp

        except requests.exceptions.ConnectionError:
            logging.error('Connection Timed out to %s' % url)

    @property
    def version(self):
        url = '/rest/dcnm-version'
        resp = self.get(url)
        return resp.json()['Dcnm-Version']

    def push_to_dcnm(self, url, data):
        url = self.base_url + url
        resp = requests.post(url, headers=self.headers, data=data)

        if not resp.ok:
            logging.info('Posting %s to %s' % (data, url))
        return resp

    def get(self, url):
        url = self.base_url + url
        resp = requests.get(url, headers=self.headers)
        if resp.ok:
            logging.info('Got %s. Received response: %s' % (url, resp.text))
        else:
            logging.error('Cloud not get %s. Received response: %s', url, resp.text)
        return resp


    def delete(self, url):
        url = self.base_url + url
        resp = requests.delete(url, headers=self.headers)
        if resp.ok:
            logging.info('Got %s. Received response: %s' % (url, resp.text))
        else:
            logging.error('Cloud not get %s. Received response: %s', url, resp.text)
        return resp

    def get_settings(self):
        obj = AutoConfigSettings.get(self)
        return obj

    def save_settings(self, obj):
        if isinstance(obj, AutoConfigSettings):
            resp = requests.put(self.base_url + '/auto-config/settings', headers=self.headers, data=obj.get_json())
            return resp
        else:
            raise TypeError()
