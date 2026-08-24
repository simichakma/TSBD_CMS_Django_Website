from django.core.files.storage import default_storage
from django.db import connection
from django.shortcuts import redirect, render


def _get_services():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, service_name
            FROM tsbd_services
            WHERE status = 1
            ORDER BY service_name ASC
        """)
        return cursor.fetchall()


def _project_image_url(image):
    if not image:
        return ""
    image = str(image)
    if image.startswith(("http://", "https://", "/")):
        return image
    if image.startswith("projects/"):
        return "/media/" + image
    return "/static/images/" + image


def _get_projects():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.id, p.project_name, p.project_details, p.service_id, service_name, p.status, p.image, p.damo_link
            FROM tsbd_projects p
            LEFT JOIN tsbd_services s ON p.service_id = s.id
            ORDER BY p.id DESC
        """)
        rows = cursor.fetchall()

    return [{
        "id": r[0],
        "project_name": r[1],
        "project_details": r[2] or "",
        "service_id": r[3],
        "service_name": r[4] or "",
        "status": r[5],
        "image": r[6] or "",
        "image_url": _project_image_url(r[6]),
        "damo_link": r[7] or "",
    } for r in rows]


def project_list(request):
    return render(request, "projects/project_list.html", {
        "projects": _get_projects(),
        "services": _get_services(),
    })


def project_save(request):
    if request.method != "POST":
        return redirect("project_list")

    project_id = request.POST.get("project_id", "").strip()
    project_name = request.POST.get("project_name", "").strip()
    project_details = request.POST.get("project_details", "").strip()
    service_id = request.POST.get("service_id", "").strip()
    damo_link = request.POST.get("damo_link", "").strip()
    status = 1 if request.POST.get("status") == "1" else 0
    uploaded_image = request.FILES.get("image")

    if not project_name:
        return redirect("project_list")

    service_value = service_id or None

    if project_id:
        with connection.cursor() as cursor:
            cursor.execute("SELECT image FROM tsbd_projects WHERE id = %s", [project_id])
            old = cursor.fetchone()

        image_path = old[0] if old else ""
        if uploaded_image:
            if image_path and str(image_path).startswith("projects/"):
                default_storage.delete(image_path)
            image_path = default_storage.save(
                "projects/" + uploaded_image.name,
                uploaded_image,
            )

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE tsbd_projects
                SET project_name=%s, project_details=%s, service_id=%s,
                    status=%s, image=%s, damo_link=%s
                WHERE id=%s
            """, [project_name, project_details, service_value, status, image_path, damo_link, project_id])
    else:
        image_path = ""
        if uploaded_image:
            image_path = default_storage.save(
                "projects/" + uploaded_image.name,
                uploaded_image,
            )

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO tsbd_projects
                    (project_name, project_details, service_id, status, image, damo_link)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, [project_name, project_details, service_value, status, image_path, damo_link])

    return redirect("project_list")


def project_delete(request, project_id):
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute("SELECT image FROM tsbd_projects WHERE id=%s", [project_id])
            row = cursor.fetchone()

        if row and row[0] and str(row[0]).startswith("projects/"):
            default_storage.delete(row[0])

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM tsbd_projects WHERE id=%s", [project_id])

    return redirect("project_list")
