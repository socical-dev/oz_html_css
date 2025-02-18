from flask import Blueprint, request, jsonify
from flask_cors import CORS
from app.services.user_service import UserService

user_routes = Blueprint("user_routes", __name__)
CORS(user_routes)  # ✅ Blueprint에도 CORS 적용 (OPTIONS 필요 없음)

@user_routes.route("/users", methods=["POST"])
def register_user():
    """사용자 등록 API"""
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    name = data.get("name")

    if not email or not password or not name:
        return jsonify({"error": "모든 필드를 입력해야 합니다."}), 400

    result = UserService.register_user(email, password, name)
    if result:
        return jsonify({"message": "사용자 등록 성공!"}), 201
    return jsonify({"error": "사용자 등록 실패"}), 500

@user_routes.route("/users/<email>", methods=["GET"])
def get_user_info(email):
    """사용자 정보 조회 API"""
    user = UserService.get_user_info(email)
    if user:
        return jsonify({
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "created_at": user.created_at
        })
    return jsonify({"error": "사용자를 찾을 수 없습니다."}), 404
    
    