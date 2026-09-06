document.addEventListener("DOMContentLoaded", function () {
    // Password toggle
    document.querySelectorAll(".toggle-password").forEach(function (btn) {
        btn.addEventListener("click", function () {
            var target = document.getElementById(this.dataset.target);
            if (!target) return;
            var icon = this.querySelector(".material-symbols-outlined");
            if (target.type === "password") {
                target.type = "text";
                icon.textContent = "visibility_off";
            } else {
                target.type = "password";
                icon.textContent = "visibility";
            }
        });
    });

    // Dark mode toggle
    var themeToggle = document.getElementById("themeToggle");
    var html = document.documentElement;
    var savedTheme = localStorage.getItem("theme") || "light";
    html.setAttribute("data-bs-theme", savedTheme);
    updateToggleIcon(savedTheme);

    if (themeToggle) {
        themeToggle.addEventListener("click", function () {
            var current = html.getAttribute("data-bs-theme");
            var next = current === "dark" ? "light" : "dark";
            html.setAttribute("data-bs-theme", next);
            localStorage.setItem("theme", next);
            updateToggleIcon(next);
        });
    }

    function updateToggleIcon(theme) {
        var icon = themeToggle
            ? themeToggle.querySelector(".material-symbols-outlined")
            : null;
        if (icon) {
            icon.textContent = theme === "dark" ? "light_mode" : "dark_mode";
        }
    }
});
