from mendeley import Mendeley
import yaml

with open('config.yml') as f:
    config = yaml.load(f)

mendeley = Mendeley(config['clientId'], config['clientSecret'])
session = mendeley.start_client_credentials_flow().authenticate()

doi = raw_input('Enter a DOI: ')

doc = session.catalog.by_identifier(doi=doi, view='stats')
print '"%s" has %s readers.' % (doc.title, doc.reader_count)
