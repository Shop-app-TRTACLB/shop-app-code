from app.routes.user_routes import user_bp
from app.routes.item_routes import item_bp
from app.routes.basket_routes import basket_bp

def init_routes(app):
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(item_bp, url_prefix='/items')
    app.register_blueprint(basket_bp, url_prefix='/baskets')
