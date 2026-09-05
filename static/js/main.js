document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("menuToggle");
    const nav = document.getElementById("mainNav");

    if (toggle && nav) {
        toggle.addEventListener("click", function () {
            nav.classList.toggle("open");
        });

        nav.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", function () {
                nav.classList.remove("open");
            });
        });
    }

    // Bootstrap 5 owns the Contact Us modal. The small fallback below
    // only runs when Bootstrap JS is unavailable.
    const contactButton = document.querySelector('[data-bs-target="#contactModal"]');
    const contactModal = document.getElementById("contactModal");

    if (!contactButton || !contactModal) {
        return;
    }

    contactButton.addEventListener("click", function (event) {
        if (typeof bootstrap !== "undefined" && bootstrap.Modal) {
            return;
        }

        event.preventDefault();
        contactModal.classList.add("show");
        contactModal.style.display = "block";
        contactModal.setAttribute("aria-modal", "true");
        contactModal.removeAttribute("aria-hidden");
        document.body.classList.add("modal-open");

        let backdrop = document.getElementById("tsbd-contact-fallback-backdrop");
        if (!backdrop) {
            backdrop = document.createElement("div");
            backdrop.id = "tsbd-contact-fallback-backdrop";
            backdrop.className = "modal-backdrop fade show";
            document.body.appendChild(backdrop);
        }

        const closeButton = contactModal.querySelector('[data-bs-dismiss="modal"]');
        if (closeButton) {
            closeButton.addEventListener("click", function () {
                contactModal.classList.remove("show");
                contactModal.style.display = "none";
                contactModal.setAttribute("aria-hidden", "true");
                contactModal.removeAttribute("aria-modal");
                document.body.classList.remove("modal-open");
                if (backdrop) backdrop.remove();
            }, { once: true });
        }
    });
});
