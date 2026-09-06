from flask import Blueprint, render_template, redirect, url_for, session, request
from models.user import User
from controller.auth_store import load_users, save_users

page_bp = Blueprint("page", __name__)


def login_required():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return None


@page_bp.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("page.dashboard"))
    return redirect(url_for("auth.login"))


@page_bp.route("/dashboard")
def dashboard():
    err = login_required()
    if err:
        return err
    return render_template("dashboard.html",
        nama=session["user_nama"], role=session["user_role"])


@page_bp.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        nama = request.form.get("nama", "").strip()
        if not email or not password or not nama:
            error = "Semua field wajib diisi."
            return render_template("register.html", error=error), 400
        users = load_users()
        if email in users:
            error = "Email sudah terdaftar."
            return render_template("register.html", error=error), 409
        user = User(email=email, nama=nama)
        user.set_password(password)
        users[email] = user.to_dict()
        save_users(users)
        return redirect(url_for("auth.login"))
    return render_template("register.html", error=error)
