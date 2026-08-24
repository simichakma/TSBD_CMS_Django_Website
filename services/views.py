from django.db import connection
from django.shortcuts import redirect, render


def home_view(request):
    services = _get_services()
    context = {
        'services': services,
    }
    return render(request, 'index.html', context) 

def _get_services():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, service_name, service_details, status
            FROM tsbd_services
            ORDER BY id DESC
        """)
        rows = cursor.fetchall()

    return [
        {
            "id": row[0],
            "service_name": row[1],
            "service_details": row[2] or "",
            "status": row[3],
        }
        for row in rows
    ]


def service_list(request):
    return render(request, "services/service_list.html", {
        "services": _get_services(),
    })

def service_save(request):
    if request.method == "POST":
        service_id = request.POST.get("service_id", "").strip()
        service_name = request.POST.get("service_name", "").strip()
        service_details = request.POST.get("service_details", "").strip()
        status = 1 if request.POST.get("status") == "1" else 0

        if service_id:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE tsbd_services
                    SET service_name = %s,
                        service_details = %s,
                        status = %s
                    WHERE id = %s
                """, [service_name, service_details, status, service_id])
        else:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO tsbd_services
                    (service_name, service_details, status)
                    VALUES (%s, %s, %s)
                """, [service_name, service_details, status])

    return redirect("service_list")


def service_delete(request, service_id):
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM tsbd_services WHERE id = %s", [service_id])
    return redirect("service_list")
