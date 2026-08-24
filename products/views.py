from django.core.files.storage import default_storage
from django.conf import settings
from django.db import connection
from django.shortcuts import redirect, render


def _image_url(image):
    if not image:
        return ""
    image = str(image).strip()
    
    if image.startswith(("http://", "https://", "/")):
        return image
    if image.startswith("media/"):
        return "/" + image
        
    if "products/" in image or image.startswith("products/"):
        return f"{settings.MEDIA_URL}{image}"
        
    return f"{settings.MEDIA_URL}products/{image}"


def product_list(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, product_name, product_details, image, status
            FROM tsbd_products
            ORDER BY id DESC
        """)
        products = cursor.fetchall()

    products = [
        {
            "id": row[0],
            "product_name": row[1],
            "product_details": row[2] or "",
            "image": row[3] or "",
            "image_url": _image_url(row[3]),
            "status": row[4],
        }
        for row in products
    ]

    return render(request, "products/product_list.html", {"products": products})


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("product_name", "").strip()
        details = request.POST.get("product_details", "").strip()
        status = 1 if request.POST.get("status") == "1" else 0
        image = request.FILES.get("image")

        if name:
            image_path = default_storage.save("products/" + image.name, image) if image else ""
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO tsbd_products
                        (product_name, product_details, image, status)
                    VALUES (%s, %s, %s, %s)
                """, [name, details, image_path, status])
            return redirect("product-list")

    return render(request, "products/product_form.html")


def edit_product(request, product_id):
    if request.method == "POST":
        name = request.POST.get("product_name", "").strip()
        details = request.POST.get("product_details", "").strip()
        status = 1 if request.POST.get("status") == "1" else 0
        image = request.FILES.get("image")

        with connection.cursor() as cursor:
            cursor.execute("SELECT image FROM tsbd_products WHERE id=%s", [product_id])
            old = cursor.fetchone()

        image_path = old[0] if old else ""
        if image:
            if image_path and str(image_path).startswith("products/"):
                default_storage.delete(image_path)
            image_path = default_storage.save("products/" + image.name, image)

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE tsbd_products
                SET product_name=%s, product_details=%s, image=%s, status=%s
                WHERE id=%s
            """, [name, details, image_path, status, product_id])

        return redirect("product-list")

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, product_name, product_details, image, status
            FROM tsbd_products WHERE id=%s
        """, [product_id])
        product = cursor.fetchone()

    return render(request, "products/product_form.html", {
        "product": product,
        "product_image_url": _image_url(product[3]) if product else "",
    })


def delete_product(request, product_id):
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute("SELECT image FROM tsbd_products WHERE id=%s", [product_id])
            row = cursor.fetchone()

        if row and row[0] and str(row[0]).startswith("products/"):
            default_storage.delete(row[0])

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM tsbd_products WHERE id=%s", [product_id])

    return redirect("product-list")
