from flask import Blueprint, render_template, redirect, url_for, session

mod_bp = Blueprint("mod", __name__)


def login_required():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return None


@mod_bp.route("/roster")
def roster():
    err = login_required()
    if err:
        return err
    return render_template("roster.html")


@mod_bp.route("/tukar-shift")
def tukar_shift():
    err = login_required()
    if err:
        return err
    return render_template("tukar-shift.html")


@mod_bp.route("/master-shift")
def master_shift():
    err = login_required()
    if err:
        return err
    return render_template("master-shift.html")


@mod_bp.route("/rekap")
def rekap():
    err = login_required()
    if err:
        return err
    return render_template("rekap.html")
