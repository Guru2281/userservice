import django

django.setup()
from userservice.db.Apps.models import Login_table as logins
from flask import jsonify, request
from flask_restful import Resource
from userservice.apis.user import *
from datetime import datetime


def get_login_dict(login):
    return {"login_time": login.login_time, "logout_time": login.logout_time, "token": login.token,
            "is_active": login.is_active, "device_id": login.device_id, 'user': get_user_dict(login.user)}

class Log_in(Resource):
    def get(self, token=None):
        if token:
            login = logins.objects.get(token=token)
            login_dict = get_login_dict(login)
            return jsonify({"login": login_dict})

        login = logins.objects.all()
        login_list = [get_login_dict(x) for x in login]
        return ({"login ": login_list})

    def post(self):
        data = request.get_json()

        user1 = users.objects.get(username=data['username'], password=data['password'])

        userForUsername = users.objects.get(username=data['username'])
        loginadd = logins.objects.create(user=userForUsername)
        login_dict = get_login_dict(loginadd)
        return jsonify({"login ": login_dict})

    def put(self,token=None):
       if(token):
            login=logins.objects.get(token=token)
            login.is_active=False
            login.logout_time=datetime.now()
            login.save()


    def delet(self,token):
        login = logins.objects.filter(token=token).delete()

        login_dict = {"token ":login}
        return jsonify({"User: ": login_dict})