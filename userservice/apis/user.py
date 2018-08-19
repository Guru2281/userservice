import django

django.setup()

from userservice.db.Apps.models import User_table as users
from flask import jsonify, request
from flask_restful import Resource

django.setup()


def get_user_dict(user):
    return {"userName ": user.username, "firstName ": user.first_name, "middleName": user.middle_name,
            "lastName": user.last_name, "gender": user.gender, "phoneNo": user.phone,
            "city": user.city}


class Users(Resource):
    def get(self, username=None):
        if username:
            user = users.objects.get(username=username)
            user_dict = {"Userid: ": user.username, "password: ": user.password}
            return jsonify({"user": user_dict})

        user = users.objects.all()
        user_list = [get_user_dict(x) for x in user]
        return ({"Users ": user_list})

    def post(self):
        data = request.get_json()
        useradd = users(username=data['username'], password=data['password'], first_name=data['fname'],
                        middle_name=data['mname'], last_name=data['lname'], gender=data['gender'], phone=data['phone'],
                        city=data['city'])
        useradd.save()
        user_dict = get_user_dict(useradd)
        return jsonify({"users ": user_dict})

    def put(self, username):
        data = request.get_json()
        if username:
            user = users.objects.get(username=username)
            user.first_name = data['newname']
            user_dict = get_user_dict(user)

            return jsonify({"User: ": user_dict})

    def delete(self):
        data = request.get_json()
        user = users.objects.filter(username=data['username']).delete()

        user_dict = {"Name ": data['username'] + " deleted"}
        return jsonify({"User: ": user_dict})






