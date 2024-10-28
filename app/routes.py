from flask import Blueprint, request, jsonify
from .models import UserModel

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/", methods=["GET", "POST"])
def manage_users():
    if request.method == "POST":
        user = {
            "name": request.json.get("name"),
            "email": request.json.get("email"),
            "password": request.json.get("password"),
        }
        UserModel.add_user(user)
        return jsonify({"message": "User added successfully"}), 201

    elif request.method == "GET":
        users = UserModel.get_all_users()
        user_list = [{"id": str(user["_id"]), "name": user["name"], "email": user["email"], "password": user["password"]} for user in users]
        return jsonify(user_list), 200

@user_bp.route("/<string:id>", methods=["GET", "PUT", "DELETE"])
def user_operations(id):
    if request.method == "GET":
        user = UserModel.get_user_by_id(id)
        if user:
            return jsonify({"id": str(user["_id"]), "name": user["name"], "email": user["email"], "password": user["password"]}), 200
        else:
            return jsonify({"error": "User not found"}), 404

    elif request.method == "PUT":
        update_data = {k: v for k, v in request.json.items() if k in {"name", "email", "password"}}
        if update_data:
            result = UserModel.update_user(id, update_data)
            if result:
                return jsonify({"message": "User updated"}), 200
            else:
                return jsonify({"error": "User not found"}), 404
        return jsonify({"error": "No fields provided for update"}), 400

    elif request.method == "DELETE":
        result = UserModel.delete_user(id)
        if result.deleted_count > 0:
            return jsonify({"message": "User deleted"}), 200
        return jsonify({"error": "User not found"}), 404
