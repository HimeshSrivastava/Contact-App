from bson import ObjectId

class UserModel:
    @staticmethod
    def add_user(data):
        from . import mongo
        return mongo.db.Usersinfo.insert_one(data)

    @staticmethod
    def get_all_users():
        from . import mongo
        return list(mongo.db.Usersinfo.find())

    @staticmethod
    def get_user_by_id(user_id):
        from . import mongo
        return mongo.db.Usersinfo.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def update_user(user_id, data):
        from . import mongo
        return mongo.db.Usersinfo.find_one_and_update(
            {"_id": ObjectId(user_id)}, {"$set": data}, return_document=True
        )

    @staticmethod
    def delete_user(user_id):
        from . import mongo
        return mongo.db.Usersinfo.delete_one({"_id": ObjectId(user_id)})
