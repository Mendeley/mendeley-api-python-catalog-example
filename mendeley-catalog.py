from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
import yaml

with open('config.yml') as f:
    config = yaml.load(f)

TOKEN_URL = 'https://api.mendeley.com/oauth/token'

oauth = OAuth2Session(client=BackendApplicationClient(config['clientId']), scope=['all'])
oauth.fetch_token(TOKEN_URL, auth=HTTPBasicAuth(config['clientId'], config['clientSecret']))

doi = raw_input('Enter a DOI: ')
rsp = oauth.get('https://api.mendeley.com/catalog', params={'doi': doi, 'view': 'stats'})

if not rsp.ok:
    print "Error getting document (status code %s)." % rsp.status_code
elif not rsp.json():
    print "Document not found."
else:
    doc = rsp.json()[0]
    print '"%s" has %s readers.' % (doc['title'], doc['reader_count'])