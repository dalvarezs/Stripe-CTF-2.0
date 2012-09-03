#!/usr/bin/env python
#
# Welcome to the Secret Safe!
#
# - users/users.db stores authentication info with the schema:
#
# CREATE TABLE users (
#   id VARCHAR(255) PRIMARY KEY AUTOINCREMENT,
#   username VARCHAR(255),
#   password_hash VARCHAR(255),
#   salt VARCHAR(255)
# );
#
# - For extra security, the dictionary of secrets lives
#   data/secrets.json (so a compromise of the database won't
#   compromise the secrets themselves)

import hashlib
import os

password='a';
salt='b';
password_hash='c';
calculated_hash = hashlib.sha256(password + salt)
print calculated_hash.hexdigest()
if calculated_hash.hexdigest() != password_hash:
    print "That's not the password for \n"
else:
    print "password ok"

