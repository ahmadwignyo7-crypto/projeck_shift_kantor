import os
from flask import Flask
from controller.auth import auth_bp
from controller.page import page_bp
from controller.module import mod_bp
from controller.roster import roster_bp
from controller.tukar_shift import swap_bp
from controller.master_shift import master_bp
from controller.rekap import rekap_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change")
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["PERMANENT_SESSION_LIFETIME"] = 1800

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(page_bp)
    app.register_blueprint(mod_bp)
    app.register_blueprint(roster_bp)
    app.register_blueprint(swap_bp)
    app.register_blueprint(master_bp)
    app.register_blueprint(rekap_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
