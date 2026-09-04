from django.db import connection, transaction
from django.shortcuts import redirect, render

MODULE_COUNT = 5


def _module_rows(service_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT module_number, title, description
            FROM tsbd_service_modules
            WHERE service_id = %s
            ORDER BY module_number ASC
        """, [service_id])
        rows = cursor.fetchall()
    return rows


def _get_services():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, service_name, service_details, status
            FROM tsbd_services
            ORDER BY id DESC
        """)
        rows = cursor.fetchall()

    services = []
    for row in rows:
        modules = _module_rows(row[0])
        item = {
            "id": row[0],
            "service_name": row[1] or "",
            "service_details": row[2] or "",
            "status": row[3],
        }
        for number in range(1, MODULE_COUNT + 1):
            found = next((m for m in modules if m[0] == number), None)
            item[f"point_{number}"] = found[1] if found else ""
            item[f"point_{number}_description"] = found[2] if found else ""
        services.append(item)
    return services


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

        with transaction.atomic():
            with connection.cursor() as cursor:
                if service_id:
                    cursor.execute("""
                        UPDATE tsbd_services
                        SET service_name = %s,
                            service_details = %s,
                            status = %s
                        WHERE id = %s
                    """, [service_name, service_details, status, service_id])
                    current_id = int(service_id)
                else:
                    cursor.execute("""
                        INSERT INTO tsbd_services
                        (service_name, service_details, status)
                        VALUES (%s, %s, %s)
                    """, [service_name, service_details, status])
                    current_id = cursor.lastrowid

                for number in range(1, MODULE_COUNT + 1):
                    title = request.POST.get(f"point_{number}", "").strip()
                    description = request.POST.get(f"point_{number}_description", "").strip()
                    cursor.execute("""
                        INSERT INTO tsbd_service_modules
                            (service_id, module_number, title, description)
                        VALUES (%s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                            title = VALUES(title),
                            description = VALUES(description)
                    """, [current_id, number, title, description])

    return redirect("service_list")


def service_delete(request, service_id):
    if request.method == "POST":
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM tsbd_service_modules WHERE service_id = %s", [service_id])
                cursor.execute("DELETE FROM tsbd_services WHERE id = %s", [service_id])
    return redirect("service_list")
