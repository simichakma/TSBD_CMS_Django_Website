function deleteProduct(productId) {

    const confirmed = confirm(
        "Are you sure you want to delete this product?"
    );

    if (!confirmed) {
        return;
    }

    const form = document.getElementById(
        "deleteProductForm"
    );

    form.action =
        "/dashboard/products/delete/" +
        productId +
        "/";

    form.submit();
}


document.addEventListener(
    "DOMContentLoaded",
    function () {

        const form =
            document.getElementById("productForm");

        if (form) {

            form.addEventListener(
                "submit",
                function (event) {

                    const name =
                        document
                        .getElementById("product_name")
                        .value
                        .trim();

                    if (!name) {

                        event.preventDefault();

                        alert(
                            "Please enter product name."
                        );

                    }

                }
            );

        }

    }
);