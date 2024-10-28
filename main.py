# from flask import Flask, request, jsonify
# from flask_pymongo import PyMongo
# from bson import ObjectId

# app = Flask(__name__)
# app.config['MONGO_URI'] = "mongodb+srv://himeshsrivastava123:rk9RUCdC3aJsdqWA@cluster0.aqzjeb9.mongodb.net/Database_backend"
# mongodb = PyMongo(app).db

# @app.route("/", methods=['GET', 'POST'])
# def add_user():
#     if request.method == 'POST':
#           user={}
#           user['name']=request.json['name']
#           user['email']=request.json['email']
#           user['password']=request.json['password']
#           mongodb.Usersinfo.insert_one(user)
#           return jsonify({"message": "user added successfully"}), 201
#     elif request.method == 'GET':
#          users=mongodb.Usersinfo.find({})
#          userList=[]
#          for user in users:
#              users={
#                  "id":str(user['_id']),
#                  "name":user['name'],
#                  "email":user['email'],
#                  "password":user['password'],
#              }
#              userList.append(users)
#          return jsonify(userList), 200
      
# @app.route("/<string:id>", methods=["GET","PUT", "DELETE"])
# def user_operations(id):
#      if request.method == 'PUT':
#         mongoid=ObjectId(id)
#         update_fields = {}
#         if 'name' in request.json:
#             update_fields['name'] = request.json['name']
#         if 'email' in request.json:
#             update_fields['email'] = request.json['email']
#         if 'password' in request.json:
#             update_fields['password'] = request.json['password']

#         # Only perform an update if there are fields to update
#         if update_fields:
#             result = mongodb.Usersinfo.find_one_and_update(
#                 {"_id": mongoid},
#                 {"$set": update_fields},
#                 return_document=True
#             )
#             if result:
#                 return jsonify({"message": "User updated"}), 200
#             else:
#                 return jsonify({"error": "User not found"}), 404
#         else:
#             return jsonify({"error": "No fields provided for update"}), 400

#      elif request.method == "DELETE":
#         mongoid=ObjectId(id)
#         result = mongodb.Usersinfo.delete_one({"_id": mongoid})
#         if result.deleted_count > 0:
#             return jsonify({"message": "User deleted"}), 200
#      else:
#         mongoid=ObjectId(id) 
#         result = mongodb.Usersinfo.find_one({"_id": mongoid})
#         if result:
#                 # Format the result to make _id JSON serializable
#                 user = {
#                     "id": str(result["_id"]),
#                     "name": result["name"],
#                     "email": result["email"],
#                     "password": result["password"]
#                 }
#                 return jsonify(user), 200
#         else:
#                 return jsonify({"error": "User not found"}), 404
           
# if __name__ == '__main__':
#     app.run(debug=True)
from app import create_app

app = create_app()

@app.route('/')
def home():
    return "Welcome to the Contact App API!"  

if __name__ == "__main__":
    app.run(debug=True)
