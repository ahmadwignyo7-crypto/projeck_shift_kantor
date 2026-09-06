from flask import Blueprint, render_template, redirect, url_for, session, jsonify
from controller.data_store import load_all

mod_bp = Blueprint("mod", __name__)


def login_required():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return None


def load_module_data():
    return {
        "employees": load_all("employees"),
        "shift_types": load_all("shift_types"),
        "assignments": load_all("assignments"),
        "swaps": load_all("swaps"),
        "attendance": load_all("attendance"),
    }


@mod_bp.route("/roster")
def roster():
    err = login_required()
    if err:
        return err
    data = load_module_data()
    return render_template("roster.html", **data)


@mod_bp.route("/tukar-shift")
def tukar_shift():
    err = login_required()
    if err:
        return err
    data = load_module_data()
    return render_template("tukar-shift.html", **data)


@mod_bp.route("/master-shift")
def master_shift():
    err = login_required()
    if err:
        return err
    data = load_module_data()
    return render_template("master-shift.html", **data)


@mod_bp.route("/rekap")
def rekap():
    err = login_required()
    if err:
        return err
    data = load_module_data()
    return render_template("rekap.html", **data)
