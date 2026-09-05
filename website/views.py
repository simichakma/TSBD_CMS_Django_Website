from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import connection
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render


def _public_services():
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, service_name, service_details, status
                FROM tsbd_services
                WHERE status = 1
                ORDER BY id ASC
            """)
            rows = cursor.fetchall()
    except Exception as e:
        print("SERVICE LOAD ERROR:", e)
        return []

    services = []
    for index, row in enumerate(rows, start=1):
        modules = []
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT module_number, title, description
                    FROM tsbd_service_modules
                    WHERE service_id = %s
                    ORDER BY module_number ASC
                """, [row[0]])
                module_rows = cursor.fetchall()
            modules = [
                {"number": f"{m[0]:02d}", "title": m[1] or "", "description": m[2] or ""}
                for m in module_rows
            ]
        except Exception as e:
            print("SERVICE MODULE LOAD ERROR:", e)

        services.append({
            "id": row[0],
            "title": row[1] or "",
            "service_name": row[1] or "",
            "description": row[2] or "",
            "short_description": row[2] or "",
            "text": row[2] or "",
            "number": f"{index:02d}",
            "modules": modules,
        })
    return services


def _image_url(image):
    if not image:
        return ""
    image = str(image)
    if image.startswith(("http://", "https://", "/")):
        return image
    if image.startswith(("projects/", "products/", "blog/", "team/")):
        return f"/media/{image}"
    return f"/static/images/{image}"


def _public_team():
    select_columns = [
        "id", "name", "designation", "linkedin", "bio", "email",
        "image", "status",
    ]
    try:
        with connection.cursor() as cursor:
            # The supplied database dump does not include the optional phone
            # and slug columns. Detect them so the public team page works
            # with both the original dump and an upgraded database.
            cursor.execute("SHOW COLUMNS FROM tsbd_team")
            available_columns = {row[0] for row in cursor.fetchall()}
            if "phone" in available_columns:
                select_columns.insert(6, "phone")
            if "slug" in available_columns:
                select_columns.append("slug")
            cursor.execute("""
                SELECT {columns}
                FROM tsbd_team
                WHERE status = 1
                ORDER BY id ASC
            """.format(columns=", ".join(select_columns)))

            rows = cursor.fetchall()

    except Exception as e:
        print("TEAM LOAD ERROR:", e)
        rows = []

    members = []
    for row in rows:
        member = dict(zip(select_columns, row))
        members.append({
            "id": member["id"],
            "name": member["name"] or "",
            "designation": member["designation"] or "",
            "linkedin": member["linkedin"] or "",
            "bio": member["bio"] or "",
            "email": member["email"] or "",
            "phone": member.get("phone") or "",
            "image": member["image"] or "",
            "status": member["status"],
            "slug": member.get("slug") or "",
            "image_url": _image_url(member["image"]),
        })
    return members


def _public_projects():
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT p.id, p.project_name, p.project_details,
                       p.service_id, s.service_name, p.damo_link, p.status, p.image
                FROM tsbd_projects p
                LEFT JOIN tsbd_services s ON p.service_id = s.id
                WHERE p.status = 1
                ORDER BY p.id DESC
            """)
            rows = cursor.fetchall()

            print("PROJECT ROWS:", rows)

    except Exception as e:
        print("PROJECT ERROR:", e)
        rows = []

    return [
        {
            "id": r[0],
            "title": r[1],
            "text": r[2] or "",
            "service_id": r[3],
            "service_name": r[4] or "",
            "demo_link": r[5] or "",
            "status": r[6],
            "image": r[7] or "",
            "image_url": _image_url(r[7]),
        }
        for r in rows
    ]

def _public_products():
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, product_name, product_details, image, status
                FROM tsbd_products
                WHERE status = 1
                ORDER BY id DESC
            """)
            rows = cursor.fetchall()
    except Exception as e:
        print("PRODUCT LOAD ERROR:", e)
        rows = []

    products = []
    for r in rows:
        modules = []
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT module_number, title, description
                    FROM tsbd_product_modules
                    WHERE product_id = %s
                    ORDER BY module_number ASC
                """, [r[0]])
                module_rows = cursor.fetchall()
            modules = [
                {
                    "number": f"{m[0]:02d}",
                    "title": m[1] or "",
                    "description": m[2] or "",
                }
                for m in module_rows
            ]
        except Exception as e:
            print("PRODUCT MODULE LOAD ERROR:", e)

        products.append({
            "id": r[0],
            "product_name": r[1] or "",
            "product_details": r[2] or "",
            "image": r[3] or "",
            "image_url": _image_url(r[3]),
            "status": r[4],
            "modules": modules,
        })
    return products


def _public_blogs():
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    id,
                    title,
                    short_description,
                    content,
                    author,
                    status
                FROM tsbd_blog
                WHERE status = 1
                ORDER BY id DESC
            """)

            rows = cursor.fetchall()

    except Exception as e:
        print("BLOG LOAD ERROR:", e)
        return []

    return [
        {
            "id": r[0],
            "title": r[1] or "",
            "short_description": r[2] or "",
            "content": r[3] or "",
            "author": r[4] or "",
            "status": r[5],
            "image_url": "",
        }
    for r in rows
]



def home(request):
    return render(request, "index.html", {
        "services": _public_services(),
        "projects": _public_projects(),
        "products": _public_products(),
        "blogs": _public_blogs()[:3],
        "team": _public_team(),
    })


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html", {"services": _public_services()})


def service_detail(request, service_id):
    services = _public_services()
    service = next((item for item in services if item["id"] == service_id), None)
    if service is None:
        raise Http404("Service not found.")
    return render(request, "public/service_detail.html", {"service": service})


def projects(request):
    return render(request, "projects.html", {"projects": _public_projects()})


def product_list(request):
    return render(request, "public/products.html", {"products": _public_products()})


def product_detail(request, product_id):
    products = _public_products()
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        from django.http import Http404
        raise Http404("Product not found.")
    return render(request, "public/product_detail.html", {"product": product})


def blog_list(request):
    return render(request, "public/blog.html", {"blogs": _public_blogs()})


def blog_detail(request, blog_id):
    blogs = _public_blogs()
    blog = next((b for b in blogs if b["id"] == blog_id), None)
    if blog is None:
        from django.http import Http404
        raise Http404("Blog post not found.")
    return render(request, "public/blog_detail.html", {"blog": blog})

def team(request):
    return render(request,"public/team.html",{"members": _public_team()})


def team_detail(request, member_id):
    if not any(member["id"] == member_id for member in _public_team()):
        raise Http404("Team member not found.")
    return render(request, "public/team_detail.html", {"member_id": member_id})


def team_member_api(request, member_id):
    member = next((item for item in _public_team() if item["id"] == member_id), None)
    if member is None:
        return JsonResponse({"success": False, "message": "Team member not found."}, status=404)
    return JsonResponse({"success": True, "member": member})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not message:
            messages.error(request, "Name, email and message are required.")
            return render(request, "contact.html")

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Please enter a valid email address.")
            return render(request, "contact.html")

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO website_contact_message
                    (name, email, phone, subject, message)
                VALUES (%s, %s, %s, %s, %s)
            """, [name, email, phone, subject, message])

        messages.success(request, "Thank you! Your message has been submitted successfully.")
        return redirect("contact")

    return render(request, "contact.html")



# from django.contrib import messages
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
# from django.db import connection
# from django.http import Http404
# from django.shortcuts import get_object_or_404, redirect, render


# def _public_services():
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 SELECT id, service_name, service_details, status
#                 FROM tsbd_services
#                 WHERE status = 1
#                 ORDER BY id ASC
#             """)
#             rows = cursor.fetchall()
#     except Exception:
#         rows = []

#     return [
#         {
#             "id": row[0],
#             "title": row[1],
#             "description": row[2] or "",
#             "text": row[2] or "",
#             "number": f"{index:02d}",
#         }
#         for index, row in enumerate(rows, start=1)
#     ]


# def _image_url(image):
#     if not image:
#         return ""
#     image = str(image)
#     if image.startswith(("http://", "https://", "/")):
#         return image
#     if image.startswith(("projects/", "products/", "blog/")):
#         return f"/media/{image}"
#     return f"/static/images/{image}"


# def _public_projects():
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 SELECT p.id, p.project_name, p.project_details,
#                        p.service_id, s.service_name, p.status, p.image
#                 FROM tsbd_projects p
#                 LEFT JOIN tsbd_services s ON p.service_id = s.id
#                 WHERE p.status = 1
#                 ORDER BY p.id DESC
#             """)
#             rows = cursor.fetchall()
#     except Exception:
#         rows = []

#     return [
#         {
#             "id": r[0],
#             "title": r[1],
#             "text": r[2] or "",
#             "service_id": r[3],
#             "service_name": r[4] or "",
#             "status": r[5],
#             "image": r[6] or "",
#             "image_url": _image_url(r[6]),
#         }
#         for r in rows
#     ]


# def _public_products():
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 SELECT id, product_name, product_details, damo_link, image, status
#                 FROM tsbd_products
#                 WHERE status = 1 AND id IS NOT NULL
#                 ORDER BY id DESC
#             """)
#             rows = cursor.fetchall()
#     except Exception:
#         rows = []

#     return [
#         {
#             "id": r[0],
#             "product_name": r[1],
#             "product_details": r[2] or "",
#             "demo_link": r[3] or "",
#             "image": r[4] or "",
#             "image_url": _image_url(r[4]),
#             "status": r[5],
#         }
#         for r in rows if r[0]
#     ]


# def _public_blogs():
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 SELECT id, title, slug, short_description, content,
#                        author, status, created_at
#                 FROM tsbd_blog
#                 WHERE status = 1
#                 ORDER BY id DESC
#             """)
#             rows = cursor.fetchall()
#     except Exception:
#         rows = []

#     return [
#         {
#             "id": r[0],
#             "title": r[1],
#             "slug": r[2],
#             "short_description": r[3] or "",
#             "content": r[4] or "",
#             "author": r[5] or "",
#             "status": r[6],
#             "created_at": r[7],
#             "image_url": "",
#             "text": r[3] or r[4] or "",
#         }
#         for r in rows
#     ]


# def home(request):
#     return render(request, "index.html", {
#         "services": _public_services()[:3],
#         "projects": _public_projects()[:3],
#         "products": _public_products()[:3],
#         "blogs": _public_blogs()[:3],
#     })


# def about(request):
#     return render(request, "about.html")


# def services(request):
#     return render(request, "services.html", {"services": _public_services()})


# def projects(request):
#     return render(request, "projects.html", {"projects": _public_projects()})


# def product_list(request):
#     return render(request, "public/products.html", {"products": _public_products()})


# def product_detail(request, product_id):
#     products = _public_products()
#     product = next((p for p in products if p["id"] == product_id), None)
#     if product is None:
#         raise Http404("Product not found.")
#     return render(request, "public/product_detail.html", {"product": product})


# def blog_list(request):
#     return render(request, "public/blog.html", {"blogs": _public_blogs()})


# def blog_detail(request, blog_id):
#     blogs = _public_blogs()
#     blog = next((b for b in blogs if b["id"] == blog_id), None)
#     if blog is None:
#         raise Http404("Blog post not found.")
#     return render(request, "public/blog_detail.html", {"blog": blog})


# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get("name", "").strip()
#         email = request.POST.get("email", "").strip()
#         phone = request.POST.get("phone", "").strip()
#         subject = request.POST.get("subject", "").strip()
#         message = request.POST.get("message", "").strip()

#         if not name or not email or not message:
#             messages.error(request, "Name, email and message are required.")
#             return render(request, "contact.html")

#         try:
#             validate_email(email)
#         except ValidationError:
#             messages.error(request, "Please enter a valid email address.")
#             return render(request, "contact.html")

#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 INSERT INTO website_contact_message
#                     (name, email, phone, subject, message)
#                 VALUES (%s, %s, %s, %s, %s)
#             """, [name, email, phone, subject, message])

#         messages.success(request, "Thank you! Your message has been submitted successfully.")
#         return redirect("contact")

#     return render(request, "contact.html")
