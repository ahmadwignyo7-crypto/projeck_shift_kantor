from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from models.user import User
from controller.auth_store import load_users, log_audit, check_rate_limit, record_attempt
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        ip = request.remote_addr
        if not check_rate_limit(ip):
            error = "Terlalu banyak percobaan. Coba lagi dalam 1 menit."
            return render_template("login.html", error=error), 429
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        if not email or not password:
            error = "Email dan password wajib diisi."
            return render_template("login.html", error=error), 400
        users = load_users()
        user_data = users.get(email)
        valid = user_data and User.from_dict(user_data, email).check_password(password)
        if not valid:
            record_attempt(ip)
            log_audit(email, "FAILED", ip)
            error = "Email atau password salah."
            return render_template("login.html", error=error), 401
        user = User.from_dict(user_data, email)
        session.permanent = True
        session["user_id"] = email
        session["user_nama"] = user.nama
        session["user_role"] = user.role
        log_audit(email, "SUCCESS", ip)
        return redirect(url_for("page.dashboard"))
    return render_template("login.html", error=error)

@auth_bp.route("/logout", methods=["POST"])
def logout():
    log_audit(session.get("user_id", "unknown"), "LOGOUT", request.remote_addr)
    session.clear()
    return redirect(url_for("auth.login"))

@auth_bp.route("/session")
def check_session():
    if "user_id" in session:
        return jsonify({"logged_in": True, "user": {
            "email": session["user_id"],
            "nama": session["user_nama"],
            "role": session["user_role"],
        }})
    return jsonify({"logged_in": False}), 401
