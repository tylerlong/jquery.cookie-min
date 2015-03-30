import json
from fabric.api import local

def update():
    local('rm *.js')
    local('wget https://github.com/carhartl/jquery-cookie/archive/master.zip')
    local('unzip master.zip && rm master.zip')
    latest_version = json.loads(open('jquery-cookie-master/bower.json').read())['version']
    local('cp jquery-cookie-master/src/jquery.cookie.js .')
    local('rm -rf jquery-cookie-master')
    print 'latest version: {0}'.format(latest_version)
