from django.db import connection


def services_menu(request):
    """Provide active services to the public navigation without breaking startup."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, service_name
                FROM tsbd_services
                WHERE status = 1
                ORDER BY id ASC
            """)
            services = cursor.fetchall()
    except Exception:
        # During first setup/migrations the legacy table may not exist yet.
        services = []

    return {"menu_services": services}
