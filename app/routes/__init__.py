from app.routes.auth_route import auth_bp
from app.routes.search_route import search_bp
from app.routes.heat_route import heat_bp

def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(heat_bp)