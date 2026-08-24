document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("menuToggle");
    const nav = document.getElementById("mainNav");

    if (toggle && nav) {
        toggle.addEventListener("click", function () {
            nav.classList.toggle("open");
        });
    }

    document.querySelectorAll("#mainNav a").forEach(function (link) {
        link.addEventListener("click", function () {
            nav.classList.remove("open");
        });
    });
});
