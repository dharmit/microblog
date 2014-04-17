#!flask/bin/python
# This script downgrades the version of the database to one version lower than
# current version.

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQL_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQL_MIGRATE_REPO, v - 1)
print "Current database version: " + \
       str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
