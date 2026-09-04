document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("projectForm");
    const id = document.getElementById("project_id");
    const name = document.getElementById("project_name");
    const service = document.getElementById("service_id");
    const details = document.getElementById("project_details");
    const damoLink = document.getElementById("damo_link");
    const status = document.getElementById("project_status");
    const image = document.getElementById("image");
    const preview = document.getElementById("imagePreview");
    const previewBox = document.getElementById("previewBox");
    const currentImage = document.getElementById("currentImage");
    const currentImageBox = document.getElementById("currentImageBox");
    const title = document.getElementById("projectFormTitle");
    const cardTitle = document.getElementById("formCardTitle");
    const button = document.getElementById("projectSaveButton");
    const reset = document.getElementById("projectResetButton");

    // Modal এর Element (যদি Bootstrap Modal ব্যবহার করেন)
    const modalElement = document.getElementById("editProjectModal");
    let editModal = null;
    if (modalElement && typeof bootstrap !== "undefined") {
        editModal = new bootstrap.Modal(modalElement);
    }

    document.querySelectorAll(".edit-project").forEach(function (item) {
        item.addEventListener("click", function () {
            // ১. Form Input গুলোতে Data সেট করা
            id.value = this.dataset.id;
            name.value = this.dataset.name;
            service.value = this.dataset.service || "";
            details.value = this.dataset.details;
            
            // demoLink / damoLink সেট করা
            if (damoLink) {
                damoLink.value = this.dataset.damo || "";
            }
            
            status.value = this.dataset.status;

            // ২. Modal থাকলে তা Open করা
            if (editModal) {
                editModal.show();
            }

            // ৩. Title এবং Button Text পরিবর্তন
            if (title) title.innerText = "Edit Project";
            if (cardTitle) cardTitle.innerText = "Edit Project";
            if (button) {
                button.innerText = "Update Project";
                button.classList.remove("btn-success");
                button.classList.add("btn-primary");
            }

            // ৪. Image Preview Handling
            if (this.dataset.image) {
                currentImage.src = this.dataset.image;
                currentImageBox.classList.remove("d-none");
            } else {
                currentImageBox.classList.add("d-none");
                currentImage.src = "";
            }

            previewBox.classList.add("d-none");
            preview.src = "";

            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    });

    image.addEventListener("change", function () {
        const file = this.files[0];
        if (!file) return;

        if (!file.type.startsWith("image/")) {
            alert("Please select an image file.");
            this.value = "";
            previewBox.classList.add("d-none");
            return;
        }

        preview.src = URL.createObjectURL(file);
        previewBox.classList.remove("d-none");
    });

    reset.addEventListener("click", function () {
        form.reset();
        id.value = "";
        if (damoLink) damoLink.value = "";
        status.value = "1";

        if (title) title.innerText = "Add Project";
        if (cardTitle) cardTitle.innerText = "Project Form";
        if (button) {
            button.innerText = "Save Project";
            button.classList.remove("btn-primary");
            button.classList.add("btn-success");
        }

        currentImage.src = "";
        preview.src = "";
        currentImageBox.classList.add("d-none");
        previewBox.classList.add("d-none");
    });

    form.addEventListener("submit", function (event) {
        if (!name.value.trim()) {
            event.preventDefault();
            alert("Please enter Project Name.");
            name.focus();
            return;
        }

        if (!service.value) {
            event.preventDefault();
            alert("Please select a Service.");
            service.focus();
            return;
        }

        button.disabled = true;
        button.innerText = id.value ? "Updating..." : "Saving...";
    });
});