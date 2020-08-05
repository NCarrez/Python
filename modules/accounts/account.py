import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if( not (file_path in sys.path)):
    sys.path.append(file_path)

from keys import master_app_key
from encryption import cryption
import security 


class account():
    def __init__(self, username, password, authorizations):
        self.username = username
        self.password = password
        self.authorizations = authorizations
    def __str__(self):
        res = '' + self.username + '\t' + self.password + '\t' + self.authorizations
        return res
    def isEqual(self, username, password):
        tmp_user = cryption(self.username)
        tmp_password = cryption(self.password)
        return (tmp_user == username and tmp_password == password)
    def checkAuth(self, authorization):
        tmp_auth = cryption(self.authorizations)
        tmp_auth = tmp_auth.split('\t')
        return (authorization in tmp_auth)
    def get_username(self, app_key):
        if(security.check_caller_authorization()):
            if cryption(app_key) == master_app_key:
                return cryption(self.username)
        return self.username
    def get_password(self, app_key):
        if(security.check_caller_authorization()):
            if cryption(app_key) == master_app_key:
                return cryption(self.password)
        return self.password