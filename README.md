# Mendeley API Python Catalog Example #

This is a simple example of an application that consumes the [Mendeley](http://www.mendeley.com) API.  For more information on the API, see the [developer portal](http://dev.mendeley.com).

## About the application ##

The application is a simple command-line script that retrieves the number of Mendeley users that have read a document with a given DOI.  It uses the client credentials flow, meaning that users don't have to log in to Mendeley to use the application.

Authenticated HTTP requests are handled by [Requests](http://docs.python-requests.org/) and [OAuthLib](https://oauthlib.readthedocs.org/).

## How to run ##

1. Install [Python](https://www.python.org/) and [Pip](https://pip.pypa.io/en/latest/).
2. Run the following command to install dependencies:

        pip install -r requirements.txt

3. Register your client at the [developer portal](http://dev.mendeley.com).  This will give you a client ID and secret.
4. Set the environment variables MENDELEY_CLIENT_ID and MENDELEY_CLIENT_SECRET to your client ID and secret respectively.
5. Run the example:

		python mendeley-catalog.py
