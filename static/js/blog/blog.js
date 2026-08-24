function deleteBlog(blogId) {

    const confirmed = confirm(
        "Are you sure you want to delete this blog?"
    );

    if (!confirmed) {
        return;
    }

    const form =
        document.getElementById("deleteBlogForm");

    form.action =
        "/dashboard/blog/delete/" +
        blogId +
        "/";

    form.submit();
}


document.addEventListener(
    "DOMContentLoaded",
    function () {

        const title =
            document.getElementById("title");

        const slug =
            document.getElementById("slug");


        if (title && slug) {

            title.addEventListener(
                "input",
                function () {

                    if (!slug.dataset.edited) {

                        slug.value =
                            title.value
                                .toLowerCase()
                                .trim()
                                .replace(
                                    /[^a-z0-9\s-]/g,
                                    ""
                                )
                                .replace(
                                    /\s+/g,
                                    "-"
                                )
                                .replace(
                                    /-+/g,
                                    "-"
                                );

                    }

                }
            );


            slug.addEventListener(
                "input",
                function () {

                    slug.dataset.edited = "true";

                }
            );

        }


        const form =
            document.getElementById("blogForm");


        if (form) {

            form.addEventListener(
                "submit",
                function (event) {

                    const blogTitle =
                        title.value.trim();

                    const blogSlug =
                        slug.value.trim();


                    if (!blogTitle) {

                        event.preventDefault();

                        alert(
                            "Please enter blog title."
                        );

                        return;

                    }


                    if (!blogSlug) {

                        event.preventDefault();

                        alert(
                            "Please enter blog slug."
                        );

                    }

                }
            );

        }

    }
);