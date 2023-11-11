import os
import tempfile
import json
from flask import Flask, request, jsonify
import random

app = Flask(__name__)


family_members_jackson = [
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Jackson",
        "age": 33,
        "lucky_numbers": [7, 13, 22]
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Jackson",
        "age": 35,
        "lucky_numbers": [10, 14, 3]
    },
    {
        "id": 3,
        "first_name": "Jimmy",
        "last_name": "Jackson",
        "age": 5,
        "lucky_numbers": [1]
    }
]


family = family_members_jackson.copy()


@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(family)

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    for member in family:
        if member["id"] == member_id:
            return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404

@app.route('/member', methods=['POST'])
def add_member():
    data = request.json
    if "id" not in data:
        data["id"] = random.randint(10000000, 99999999)
    family.append(data)
    return jsonify(data), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    for members in family:
        if members["id"] == member_id:
            family.remove(members)
            return jsonify({"done": True}), 200
    return jsonify({"error": "Member not found"}), 404

if __name__ == '__main__':
    app.run()
