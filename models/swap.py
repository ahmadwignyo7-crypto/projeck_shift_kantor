from datetime import datetime, timezone


class SwapRequest:
    def __init__(self, requester, replacement, reason, swap_id=None):
        self.id = swap_id
        self.requester = requester
        self.replacement = replacement
        self.reason = reason
        self.status = "pending"
        self.requester_date = ""
        self.requester_shift = ""
        self.replacement_date = ""
        self.replacement_shift = ""
        self.document = ""
        self.approved_by = ""
        self.created_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "requester": self.requester,
            "replacement": self.replacement,
            "reason": self.reason,
            "status": self.status,
            "requester_date": self.requester_date,
            "requester_shift": self.requester_shift,
            "replacement_date": self.replacement_date,
            "replacement_shift": self.replacement_shift,
            "document": self.document,
            "approved_by": self.approved_by,
            "created_at": self.created_at,
        }

    @staticmethod
    def from_dict(data):
        swap = SwapRequest(
            requester=data.get("requester"),
            replacement=data.get("replacement"),
            reason=data.get("reason"),
            swap_id=data.get("id"),
        )
        swap.status = data.get("status", "pending")
        swap.requester_date = data.get("requester_date", "")
        swap.requester_shift = data.get("requester_shift", "")
        swap.replacement_date = data.get("replacement_date", "")
        swap.replacement_shift = data.get("replacement_shift", "")
        swap.document = data.get("document", "")
        swap.approved_by = data.get("approved_by", "")
        swap.created_at = data.get("created_at", swap.created_at)
        return swap
