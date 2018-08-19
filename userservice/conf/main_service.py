from flask import *
from flask_restful import *

from userservice.apis.login import Log_in
from userservice.apis.user import Users


import django
django.setup()
app = Flask(__name__)

api = Api(app, prefix='/userservice/')
api.add_resource(Users,'user/','user/<username>')
api.add_resource(Log_in,'login/','login/<token>')


if __name__ == '__main__':
    app.run(host='localhost',port=2010,debug=True)