from mendeley import Mendeley
import yaml
import os

config_file = 'config.yml'

config = {}

if os.path.isfile(config_file): 
    with open('config.yml') as f:
        config = yaml.load(f)
else:
    config['clientId'] = os.environ.get('MENDELEY_CLIENT_ID')
    config['clientSecret'] = os.environ.get('MENDELEY_CLIENT_SECRET')

mendeley = Mendeley(config['clientId'], config['clientSecret'])
session = mendeley.start_client_credentials_flow().authenticate()

doi = raw_input('Enter a DOI: ')

doc = session.catalog.by_identifier(doi=doi, view='stats')
print '"%s" has %s readers.' % (doc.title, doc.reader_count)
