from flask import Blueprint, request, jsonify, session, redirect, url_for
from models.attendance import Attendance
from controller.data_store import load_all, save_all, gen_id

rekap_bp = Blueprint("rekap", __name__)


def login_required():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return None


@rekap_bp.route("/api/attendance", methods=["GET"])
def get_attendance():
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    data = load_all("attendance")
    emp_filter = request.args.get("employee_id", "")
    date_filter = request.args.get("date", "")
    result = [Attendance.from_dict(v).to_dict() for v in data.values()]
    if emp_filter:
        result = [a for a in result if a["employee_id"] == emp_filter]
    if date_filter:
        result = [a for a in result if a["date"] == date_filter]
    return jsonify(result)


@rekap_bp.route("/api/attendance", methods=["POST"])
def add_attendance():
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    req = request.get_json()
    data = load_all("attendance")
    att_id = gen_id(data)
    att = Attendance(
        employee_id=req["employee_id"],
        date=req["date"],
        shift_code=req["shift_code"],
        att_id=str(att_id),
    )
    att.check_in = req.get("check_in", "")
    att.check_out = req.get("check_out", "")
    att.status = req.get("status", "Tepat Waktu")
    att.overtime_hours = req.get("overtime_hours", 0)
    data[str(att_id)] = att.to_dict()
    save_all("attendance", data)
    return jsonify(att.to_dict()), 201


@rekap_bp.route("/api/attendance/<att_id>", methods=["PUT"])
def update_attendance(att_id):
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    req = request.get_json()
    data = load_all("attendance")
    if att_id not in data:
        return jsonify({"error": "not found"}), 404
    data[att_id]["check_in"] = req.get("check_in", data[att_id]["check_in"])
    data[att_id]["check_out"] = req.get("check_out", data[att_id]["check_out"])
    data[att_id]["status"] = req.get("status", data[att_id]["status"])
    data[att_id]["overtime_hours"] = req.get("overtime_hours", data[att_id]["overtime_hours"])
    save_all("attendance", data)
    return jsonify(data[att_id])
