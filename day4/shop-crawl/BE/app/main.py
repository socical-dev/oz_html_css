from flask import Flask
from flask_cors import CORS
from user.routes.user_routes import user_routes
from product.routes.product_routes import product_routes
from crawler.routes.crawler_routes import crawler_routes

app = Flask(__name__)

# 모든 엔드포인트에 대해 CORS 허용
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# API 엔드포인트 등록
app.register_blueprint(user_routes, url_prefix="/api")
app.register_blueprint(product_routes, url_prefix="/api")
app.register_blueprint(crawler_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True, port=5000)