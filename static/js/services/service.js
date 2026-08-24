document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("serviceForm");
    const id = document.getElementById("service_id");
    const name = document.getElementById("service_name");
    const details = document.getElementById("service_details");
    const status = document.getElementById("status");
    const title = document.getElementById("formTitle");
    const button = document.getElementById("saveButton");

    document.querySelectorAll(".edit-service").forEach(function (item) {
        item.addEventListener("click", function () {
            id.value = this.dataset.id;
            name.value = this.dataset.name;
            details.value = this.dataset.details;
            status.value = this.dataset.status;
            title.innerText = "Edit Service";
            button.innerText = "Update Service";
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    });

    document.getElementById("resetButton").addEventListener("click", function () {
        form.reset();
        id.value = "";
        status.value = "1";
        title.innerText = "Add Service";
        button.innerText = "Save Service";
    });
});
