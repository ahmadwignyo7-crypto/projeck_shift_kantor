from flask import Blueprint, request, jsonify, session, redirect, url_for
from models.swap import SwapRequest
from controller.data_store import load_all, save_all, gen_id

swap_bp = Blueprint("swap", __name__)


def login_required():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return None


@swap_bp.route("/api/swaps", methods=["GET"])
def get_swaps():
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    data = load_all("swaps")
    status = request.args.get("status", "")
    swaps = [SwapRequest.from_dict(v).to_dict() for v in data.values()]
    if status:
        swaps = [s for s in swaps if s["status"] == status]
    return jsonify(swaps)


@swap_bp.route("/api/swaps", methods=["POST"])
def add_swap():
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    req = request.get_json()
    data = load_all("swaps")
    swap_id = gen_id(data)
    swap = SwapRequest(
        requester=req["requester"],
        replacement=req["replacement"],
        reason=req["reason"],
        swap_id=str(swap_id),
    )
    swap.requester_date = req.get("requester_date", "")
    swap.requester_shift = req.get("requester_shift", "")
    swap.replacement_date = req.get("replacement_date", "")
    swap.replacement_shift = req.get("replacement_shift", "")
    data[str(swap_id)] = swap.to_dict()
    save_all("swaps", data)
    return jsonify(swap.to_dict()), 201


@swap_bp.route("/api/swaps/<swap_id>/approve", methods=["POST"])
def approve_swap(swap_id):
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    data = load_all("swaps")
    if swap_id not in data:
        return jsonify({"error": "not found"}), 404
    data[swap_id]["status"] = "approved"
    data[swap_id]["approved_by"] = session.get("user_nama", "admin")
    save_all("swaps", data)
    return jsonify(data[swap_id])


@swap_bp.route("/api/swaps/<swap_id>/reject", methods=["POST"])
def reject_swap(swap_id):
    err = login_required()
    if err:
        return jsonify({"error": "unauthorized"}), 401
    data = load_all("swaps")
    if swap_id not in data:
        return jsonify({"error": "not found"}), 404
    data[swap_id]["status"] = "rejected"
    save_all("swaps", data)
    return jsonify(data[swap_id])
