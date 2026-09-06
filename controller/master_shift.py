from flask import Blueprint, request, jsonify, session, redirect, url_for
from models.shift import ShiftType
from controller.data_store import load_all, save_all, gen_id

master_bp = Blueprint("master", __name__)


def login_required():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return None


@master_bp.route("/api/shift-types", methods=["GET"])
def get_shift_types():
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    data = load_all("shift_types")
    result = [ShiftType.from_dict(v).to_dict() for v in data.values()]
    return jsonify(result)


@master_bp.route("/api/shift-types", methods=["POST"])
def add_shift_type():
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    req = request.get_json()
    data = load_all("shift_types")
    shift_id = gen_id(data)
    shift = ShiftType(
        code=req["code"],
        name=req["name"],
        start=req["start_time"],
        end=req["end_time"],
        color=req.get("color", "#0059bb"),
        shift_id=str(shift_id),
    )
    data[str(shift_id)] = shift.to_dict()
    save_all("shift_types", data)
    return jsonify(shift.to_dict()), 201


@master_bp.route("/api/shift-types/<shift_id>", methods=["PUT"])
def update_shift_type(shift_id):
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    req = request.get_json()
    data = load_all("shift_types")
    if shift_id not in data:
        return jsonify({"error": "not found"}), 404
    data[shift_id]["name"] = req.get("name", data[shift_id]["name"])
    data[shift_id]["start_time"] = req.get("start_time", data[shift_id]["start_time"])
    data[shift_id]["end_time"] = req.get("end_time", data[shift_id]["end_time"])
    data[shift_id]["color"] = req.get("color", data[shift_id]["color"])
    save_all("shift_types", data)
    return jsonify(data[shift_id])


@master_bp.route("/api/shift-types/<shift_id>", methods=["DELETE"])
def delete_shift_type(shift_id):
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    data = load_all("shift_types")
    if shift_id in data:
        del data[shift_id]
        save_all("shift_types", data)
    return jsonify({"ok": True})
