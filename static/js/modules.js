async function api(url, method = "GET", body = null) {
    const opts = { method, headers: { "Content-Type": "application/json" } };
    if (body) opts.body = JSON.stringify(body);
    const res = await fetch(url, opts);
    return res.json();
}


function showAlert(msg, type = "success") {
    const d = document.createElement("div");
    d.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 end-0 m-3`;
    d.style.zIndex = "9999";
    d.innerHTML = `${msg}<button type="button" class="btn-close" data-bs-dismiss="alert"></button>`;
    document.body.appendChild(d);
    setTimeout(() => d.remove(), 3000);
}


function formatTime(t) {
    if (!t) return "-";
    return t.substring(0, 5);
}


function shiftBadge(code) {
    const colors = { PAGI: "primary", SIANG: "info", MALAM: "dark", OFF: "secondary" };
    return `<span class="badge bg-${colors[code] || "secondary"}">${code}</span>`;
}
