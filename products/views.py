from django.core.files.storage import default_storage
from django.conf import settings
<<<<<<< HEAD
from django.db import connection, transaction
from django.shortcuts import redirect, render

MODULE_COUNT = 5

=======
from django.db import connection
from django.shortcuts import redirect, render

>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de

def _image_url(image):
    if not image:
        return ""
    image = str(image).strip()
<<<<<<< HEAD
=======
    
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de
    if image.startswith(("http://", "https://", "/")):
        return image
    if image.startswith("media/"):
        return "/" + image
<<<<<<< HEAD
    if "products/" in image or image.startswith("products/"):
        return f"{settings.MEDIA_URL}{image}"
    return f"{settings.MEDIA_URL}products/{image}"


def _module_rows(product_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT module_number, title, description
                FROM tsbd_product_modules
                WHERE product_id = %s
                ORDER BY module_number ASC
            """, [product_id])
            return cursor.fetchall()
    except Exception:
        return []


def _product_item(row):
    modules = _module_rows(row[0])
    item = {
        "id": row[0],
        "product_name": row[1] or "",
        "product_details": row[2] or "",
        "image": row[3] or "",
        "image_url": _image_url(row[3]),
        "status": row[4],
        "modules": [],
    }
    for number, title, description in modules:
        item["modules"].append({
            "number": f"{number:02d}",
            "title": title or "",
            "description": description or "",
        })
    return item


=======
        
    if "products/" in image or image.startswith("products/"):
        return f"{settings.MEDIA_URL}{image}"
        
    return f"{settings.MEDIA_URL}products/{image}"


>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de
def product_list(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, product_name, product_details, image, status
            FROM tsbd_products
            ORDER BY id DESC
        """)
<<<<<<< HEAD
        rows = cursor.fetchall()

    return render(request, "products/product_list.html", {
        "products": [_product_item(row) for row in rows]
    })
=======
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
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("product_name", "").strip()
        details = request.POST.get("product_details", "").strip()
        status = 1 if request.POST.get("status") == "1" else 0
        image = request.FILES.get("image")

        if name:
            image_path = default_storage.save("products/" + image.name, image) if image else ""
<<<<<<< HEAD
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO tsbd_products
                            (product_name, product_details, image, status)
                        VALUES (%s, %s, %s, %s)
                    """, [name, details, image_path, status])
                    product_id = cursor.lastrowid
                    _save_modules(request, product_id, cursor)
=======
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO tsbd_products
                        (product_name, product_details, image, status)
                    VALUES (%s, %s, %s, %s)
                """, [name, details, image_path, status])
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de
            return redirect("product-list")

    return render(request, "products/product_form.html")


<<<<<<< HEAD
def _save_modules(request, product_id, cursor):
    for number in range(1, MODULE_COUNT + 1):
        title = request.POST.get(f"point_{number}", "").strip()
        description = request.POST.get(f"point_{number}_description", "").strip()
        cursor.execute("""
            INSERT INTO tsbd_product_modules
                (product_id, module_number, title, description)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                title = VALUES(title),
                description = VALUES(description)
        """, [product_id, number, title, description])


=======
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de
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

<<<<<<< HEAD
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE tsbd_products
                    SET product_name=%s, product_details=%s, image=%s, status=%s
                    WHERE id=%s
                """, [name, details, image_path, status, product_id])
                _save_modules(request, product_id, cursor)
=======
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE tsbd_products
                SET product_name=%s, product_details=%s, image=%s, status=%s
                WHERE id=%s
            """, [name, details, image_path, status, product_id])
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de

        return redirect("product-list")

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, product_name, product_details, image, status
            FROM tsbd_products WHERE id=%s
        """, [product_id])
        product = cursor.fetchone()

<<<<<<< HEAD
    modules = _module_rows(product_id) if product else []
    module_map = {m[0]: {"title": m[1] or "", "description": m[2] or ""} for m in modules}
    context = {
        "product": product,
        "product_image_url": _image_url(product[3]) if product else "",
    }
    for number in range(1, MODULE_COUNT + 1):
        context[f"module_{number}_title"] = module_map.get(number, {}).get("title", "")
        context[f"module_{number}_description"] = module_map.get(number, {}).get("description", "")
    return render(request, "products/product_form.html", context)
=======
    return render(request, "products/product_form.html", {
        "product": product,
        "product_image_url": _image_url(product[3]) if product else "",
    })
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de


def delete_product(request, product_id):
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute("SELECT image FROM tsbd_products WHERE id=%s", [product_id])
            row = cursor.fetchone()

        if row and row[0] and str(row[0]).startswith("products/"):
            default_storage.delete(row[0])

<<<<<<< HEAD
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM tsbd_product_modules WHERE product_id=%s", [product_id])
                cursor.execute("DELETE FROM tsbd_products WHERE id=%s", [product_id])
=======
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM tsbd_products WHERE id=%s", [product_id])
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de

    return redirect("product-list")
