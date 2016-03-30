# Mendeley API Python Catalog Example #

This is a simple example of an application that consumes the [Mendeley](http://www.mendeley.com) API, using the [Python SDK](http://mendeley-python.readthedocs.org/).

For more information on the API, see the [developer portal](http://dev.mendeley.com).

## About the application ##

The application is a simple command-line script that retrieves the number of Mendeley users that have read a document with a given DOI.  It uses the client credentials flow, meaning that users don't have to log in to Mendeley to use the application.

## Prerequisites ##

Register your client at the [developer portal](http://dev.mendeley.com).  This will give you a client ID and secret. (You will not get very far without these!)

## How to install ##

1. Install [Python](https://www.python.org/) and [Pip](https://pip.pypa.io/en/latest/).
2. Run the following command to install dependencies:

        pip install -r requirements.txt

## How to run ##

Insert your API keys with one of these methods:

- **Config file method:** Rename the config.yml.example file to config.yml, and fill in your client ID and secret in this file.
- **Environment variable method:** Set the `MENDELEY_CLIENT_ID` and `MENDELEY_CLIENT_SECRET` environment variables in your shell context to the appropriate values.

Now run the example:

		python mendeley-catalog.py [DOI you want to look up]

## Build status ##

![Travis CI](https://travis-ci.org/Mendeley/mendeley-api-python-catalog-example.svg?branch=master)
