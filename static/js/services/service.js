document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("serviceForm");
    const id = document.getElementById("service_id");
    const name = document.getElementById("service_name");
    const details = document.getElementById("service_details");
    const status = document.getElementById("status");
    const title = document.getElementById("formTitle");
    const button = document.getElementById("saveButton");
<<<<<<< HEAD
    const reset = document.getElementById("resetButton");

    document.querySelectorAll(".edit-service").forEach(function (item) {
        item.addEventListener("click", function () {
            id.value = this.dataset.id || "";
            name.value = this.dataset.name || "";
            details.value = this.dataset.details || "";
            status.value = this.dataset.status || "1";

            for (let n = 1; n <= 5; n++) {
                const point = document.getElementById("point_" + n);
                const description = document.getElementById("point_" + n + "_description");
                if (point) point.value = this.dataset["point" + "-" + n] || "";
                if (description) description.value = this.dataset["point" + "-" + n + "-description"] || "";
            }

=======

    document.querySelectorAll(".edit-service").forEach(function (item) {
        item.addEventListener("click", function () {
            id.value = this.dataset.id;
            name.value = this.dataset.name;
            details.value = this.dataset.details;
            status.value = this.dataset.status;
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de
            title.innerText = "Edit Service";
            button.innerText = "Update Service";
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    });

<<<<<<< HEAD
    reset.addEventListener("click", function () {
=======
    document.getElementById("resetButton").addEventListener("click", function () {
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de
        form.reset();
        id.value = "";
        status.value = "1";
        title.innerText = "Add Service";
        button.innerText = "Save Service";
    });
});
