document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("serviceForm");
    const id = document.getElementById("service_id");
    const name = document.getElementById("service_name");
    const details = document.getElementById("service_details");
    const status = document.getElementById("status");
    const title = document.getElementById("formTitle");
    const button = document.getElementById("saveButton");
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

            title.innerText = "Edit Service";
            button.innerText = "Update Service";
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    });

    reset.addEventListener("click", function () {
        form.reset();
        id.value = "";
        status.value = "1";
        title.innerText = "Add Service";
        button.innerText = "Save Service";
    });
});
