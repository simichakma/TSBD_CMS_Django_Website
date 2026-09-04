from django.db import connection
from django.shortcuts import render


def _count(sql):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()[0]
    except Exception:
        return 0


def dashboard(request):
    return render(request, "dashboard/dashboard.html", {
        "total_services": _count("SELECT COUNT(*) FROM tsbd_services WHERE status = 1"),
        "total_projects": _count("SELECT COUNT(*) FROM tsbd_projects WHERE status = 1"),
        "total_products": _count("SELECT COUNT(*) FROM tsbd_products WHERE status = 1"),
        "total_blogs": _count("SELECT COUNT(*) FROM tsbd_blog WHERE status = 1"),
        "total_team": _count("SELECT COUNT(*) FROM tsbd_team WHERE status = 1"),
        "total_messages": _count("SELECT COUNT(*) FROM website_contact_message"),
    })


def message_list(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, name, email, phone, subject, message, created_at
                FROM website_contact_message
                ORDER BY id DESC
            """)
            messages = cursor.fetchall()
    except Exception:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, name, email, phone, subject, message
                FROM website_contact_message
                ORDER BY id DESC
            """)
            messages = cursor.fetchall()

    return render(request, "dashboard/messages.html", {"messages": messages})
