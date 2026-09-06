from flask import Blueprint, request, jsonify, session, redirect, url_for
from models.employee import Employee
from models.shift import ShiftAssignment
from controller.data_store import load_all, save_all, gen_id

roster_bp = Blueprint("roster", __name__)


def login_required():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return None


@roster_bp.route("/api/employees", methods=["GET"])
def get_employees():
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    data = load_all("employees")
    employees = [Employee.from_dict(v).to_dict() for v in data.values()]
    return jsonify(employees)


@roster_bp.route("/api/employees", methods=["POST"])
def add_employee():
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    req = request.get_json()
    data = load_all("employees")
    emp_id = gen_id(data)
    emp = Employee(
        nama=req["nama"], nip=req["nip"], nik=req["nik"],
        department=req["department"], position=req["position"],
        emp_id=str(emp_id),
    )
    data[str(emp_id)] = emp.to_dict()
    save_all("employees", data)
    return jsonify(emp.to_dict()), 201


@roster_bp.route("/api/assignments", methods=["GET"])
def get_assignments():
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    data = load_all("assignments")
    result = [ShiftAssignment.from_dict(v).to_dict() for v in data.values()]
    return jsonify(result)


@roster_bp.route("/api/assignments", methods=["POST"])
def add_assignment():
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    req = request.get_json()
    data = load_all("assignments")
    assign_id = gen_id(data)
    assign = ShiftAssignment(
        employee_id=req["employee_id"],
        date=req["date"],
        shift_code=req["shift_code"],
        assign_id=str(assign_id),
    )
    data[str(assign_id)] = assign.to_dict()
    save_all("assignments", data)
    return jsonify(assign.to_dict()), 201


@roster_bp.route("/api/assignments/<assign_id>", methods=["DELETE"])
def delete_assignment(assign_id):
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    data = load_all("assignments")
    if assign_id in data:
        del data[assign_id]
        save_all("assignments", data)
    return jsonify({"ok": True})
