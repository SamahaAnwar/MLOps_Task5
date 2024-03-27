from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client["App"]
collection = db["users"]

@app.route('/add_user', methods=['POST'])

def add_user():
    data = request.json
    name = data['name']
    email = data['email']
    
    user = {"name": name, "email": email}
    collection.insert_one(user)
    
    return jsonify({"message": "User added successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
