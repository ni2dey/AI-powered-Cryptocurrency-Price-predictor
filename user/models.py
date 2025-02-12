from flask import Flask, jsonify, request, redirect,session
from passlib.hash import pbkdf2_sha256
from .extension import db
import uuid

class User:
    def start_session(self,user):
        del user['password']
        session['logged_in']=True
        session['user']=user
        return jsonify(user),200

    def signup(self):
        user={
            "_id":uuid.uuid4().hex,
              "name":request.form.get('name'),
              "email":request.form.get('email'),
              "password":request.form.get('password')}
        
        user['password']=pbkdf2_sha256.encrypt(user['password'])

        if db.users.find_one({"email":user['email']}):
            return jsonify({"error":"Email address already in use"}),400
        
        if db.users.insert_one(user):
            return self.start_session(user)
        
        return jsonify({"error":"Signup failed"}),400

    def signout(self):
        session.clear()
        return redirect('/')


    def login(self):
        user=db.users.find_one({
            "email":request.form.get('email')
        })
        try:
            if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
                return self.start_session(user)
            return jsonify({"error": "Invalid login credentials"}), 401
        except ValueError:
            return jsonify({"error": "Password verification failed"}), 401
        except AttributeError:
            return jsonify({"error": "User does not exist"}), 401
        except Exception as e:
            return jsonify({"error": f"{e}"}), 500
        