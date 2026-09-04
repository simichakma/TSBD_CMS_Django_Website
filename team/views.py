from pathlib import Path

from django.conf import settings
from django.core.files.storage import default_storage
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify


def _image_url(image):
    if not image:
        return ""
    image = str(image).strip()
    if image.startswith(("http://", "https://", "/")):
        return image
    if image.startswith("media/"):
        return "/" + image
    return f"{settings.MEDIA_URL}{image if image.startswith('team/') else 'team/' + image}"


<<<<<<< HEAD
def _public_url(request, member_id):
    return request.build_absolute_uri(reverse("team-detail", kwargs={"member_id": member_id}))
=======
def _public_url(request, slug):
    return request.build_absolute_uri(reverse("team-detail", kwargs={"member_slug": slug}))
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de


def _unique_slug(name, team_id=None):
    base = slugify(name) or "team-member"
    reserved = {"admin", "dashboard", "about", "services", "projects", "products", "blog", "team", "contact", "api", "media", "static"}
    if base in reserved:
        base = f"{base}-member"
    candidate, suffix = base, 2
    with connection.cursor() as cursor:
        while True:
            sql, params = "SELECT id FROM tsbd_team WHERE slug=%s", [candidate]
            if team_id is not None:
                sql += " AND id<>%s"
                params.append(team_id)
            cursor.execute(sql, params)
            if cursor.fetchone() is None:
                return candidate
            candidate, suffix = f"{base}-{suffix}", suffix + 1


def _row_to_member(row, request=None):
    member = {
        "id": row[0], "name": row[1] or "", "designation": row[2] or "",
        "linkedin": row[3] or "", "bio": row[4] or "", "email": row[5] or "",
        "phone": row[6] or "", "image": row[7] or "", "image_url": _image_url(row[7]),
        "status": bool(row[8]), "slug": row[9] or "",
    }
<<<<<<< HEAD
    if request and member["id"]:
        member["public_url"] = _public_url(request, member["id"])
=======
    if request and member["slug"]:
        member["public_url"] = _public_url(request, member["slug"])
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de
    return member


TEAM_SELECT = """
    SELECT id, name, designation, linkedin, bio, email, phone, image, status, slug
    FROM tsbd_team
"""


def team_list(request):
    with connection.cursor() as cursor:
        cursor.execute(TEAM_SELECT + " ORDER BY id DESC")
        members = [_row_to_member(row, request) for row in cursor.fetchall()]
    return render(request, "team/team_list.html", {"team_members": members})


def team_data(request):
    if request.method != "GET":
        return JsonResponse({"success": False, "message": "Only GET request is allowed."}, status=405)
    with connection.cursor() as cursor:
        cursor.execute(TEAM_SELECT + " ORDER BY id DESC")
        members = [_row_to_member(row, request) for row in cursor.fetchall()]
    return JsonResponse({"success": True, "members": members})


def add_team(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Only POST request is allowed."}, status=405)
    name = request.POST.get("name", "").strip()
    if not name:
        return JsonResponse({"success": False, "message": "Name is required."}, status=400)
    image = request.FILES.get("image")
    image_path = default_storage.save(f"team/{Path(image.name).name}", image) if image else ""
    slug = _unique_slug(name)
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO tsbd_team
                    (name, designation, email, phone, bio, linkedin, image, status, slug)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, [
                name, request.POST.get("designation", "").strip(), request.POST.get("email", "").strip(),
                request.POST.get("phone", "").strip(), request.POST.get("bio", "").strip(),
                request.POST.get("linkedin", "").strip(), image_path,
                1 if request.POST.get("status") == "1" else 0, slug,
            ])
<<<<<<< HEAD
            team_id = cursor.lastrowid
=======
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de
    except Exception:
        if image_path:
            default_storage.delete(image_path)
        raise
<<<<<<< HEAD
    return JsonResponse({"success": True, "message": "Team member saved successfully.", "slug": slug, "public_url": _public_url(request, team_id)})
=======
    return JsonResponse({"success": True, "message": "Team member saved successfully.", "slug": slug, "public_url": _public_url(request, slug)})
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de


def get_team(request, team_id):
    if request.method != "GET":
        return JsonResponse({"success": False, "message": "Only GET request is allowed."}, status=405)
    with connection.cursor() as cursor:
        cursor.execute(TEAM_SELECT + " WHERE id=%s", [team_id])
        row = cursor.fetchone()
    if not row:
        return JsonResponse({"success": False, "message": "Team member not found."}, status=404)
    return JsonResponse({"success": True, "team": _row_to_member(row, request)})


def edit_team(request, team_id):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Only POST request is allowed."}, status=405)
    with connection.cursor() as cursor:
        cursor.execute("SELECT image, slug FROM tsbd_team WHERE id=%s", [team_id])
        old = cursor.fetchone()
    if not old:
        return JsonResponse({"success": False, "message": "Team member not found."}, status=404)
    name = request.POST.get("name", "").strip()
    if not name:
        return JsonResponse({"success": False, "message": "Name is required."}, status=400)
    old_image, old_slug = old[0] or "", old[1] or ""
    slug = old_slug or _unique_slug(name, team_id)
    image = request.FILES.get("image")
    image_path = default_storage.save(f"team/{Path(image.name).name}", image) if image else old_image
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE tsbd_team SET name=%s, designation=%s, email=%s, phone=%s,
                bio=%s, linkedin=%s, image=%s, status=%s, slug=%s WHERE id=%s
        """, [
            name, request.POST.get("designation", "").strip(), request.POST.get("email", "").strip(),
            request.POST.get("phone", "").strip(), request.POST.get("bio", "").strip(),
            request.POST.get("linkedin", "").strip(), image_path,
            1 if request.POST.get("status") == "1" else 0, slug, team_id,
        ])
    if image and old_image and old_image != image_path and str(old_image).startswith("team/"):
        default_storage.delete(old_image)
<<<<<<< HEAD
    return JsonResponse({"success": True, "message": "Team member updated successfully.", "slug": slug, "public_url": _public_url(request, team_id)})
=======
    return JsonResponse({"success": True, "message": "Team member updated successfully.", "slug": slug, "public_url": _public_url(request, slug)})
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de


def delete_team(request, team_id):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Only POST request is allowed."}, status=405)
    with connection.cursor() as cursor:
        cursor.execute("SELECT image FROM tsbd_team WHERE id=%s", [team_id])
        row = cursor.fetchone()
        if not row:
            return JsonResponse({"success": False, "message": "Team member not found."}, status=404)
        cursor.execute("DELETE FROM tsbd_team WHERE id=%s", [team_id])
    if row[0] and str(row[0]).startswith("team/"):
        default_storage.delete(row[0])
    return JsonResponse({"success": True, "message": "Team member deleted successfully."})
