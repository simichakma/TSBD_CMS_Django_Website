from django.db import migrations
<<<<<<< HEAD


class Migration(migrations.Migration):
    """Compatibility no-op: the supplied SQL dump already defines tsbd_team.

    The current Team app uses only columns present in that schema:
    id, name, designation, bio, image, email, linkedin, status, sort_order.
    """

    dependencies = []
    operations = []
=======
from django.utils.text import slugify


def add_team_fields(apps, schema_editor):
    with schema_editor.connection.cursor() as cursor:
        columns = {column.name for column in schema_editor.connection.introspection.get_table_description(cursor, "tsbd_team")}
        if "phone" not in columns:
            cursor.execute("ALTER TABLE tsbd_team ADD COLUMN phone VARCHAR(50) NULL DEFAULT ''")
        if "slug" not in columns:
            cursor.execute("ALTER TABLE tsbd_team ADD COLUMN slug VARCHAR(180) NULL")
        cursor.execute("SELECT id, name, slug FROM tsbd_team ORDER BY id")
        rows = cursor.fetchall()
        used = {row[2] for row in rows if row[2]}
        reserved = {"admin", "dashboard", "about", "services", "projects", "products", "blog", "team", "contact", "api", "media", "static"}
        for member_id, name, current_slug in rows:
            if current_slug:
                continue
            base = slugify(name or "") or "team-member"
            if base in reserved:
                base += "-member"
            slug, suffix = base, 2
            while slug in used:
                slug, suffix = f"{base}-{suffix}", suffix + 1
            cursor.execute("UPDATE tsbd_team SET slug=%s WHERE id=%s", [slug, member_id])
            used.add(slug)
        try:
            cursor.execute("CREATE UNIQUE INDEX tsbd_team_slug_unique ON tsbd_team (slug)")
        except Exception:
            pass


class Migration(migrations.Migration):
    dependencies = []
    operations = [migrations.RunPython(add_team_fields, migrations.RunPython.noop)]
>>>>>>> 5501b4d12a9573602d1e327d5599a5f07fcdc2de
