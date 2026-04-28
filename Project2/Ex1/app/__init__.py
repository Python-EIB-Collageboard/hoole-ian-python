from flask import Flask

def create_app():
    app = Flask(__name__)
    from .products.routes import product_bp
    app.register_blueprint(product_bp)
    return app