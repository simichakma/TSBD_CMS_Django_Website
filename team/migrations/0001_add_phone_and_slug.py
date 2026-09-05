from django.db import migrations


class Migration(migrations.Migration):
    """Compatibility no-op: the supplied SQL dump already defines tsbd_team.

    The current Team app uses only columns present in that schema:
    id, name, designation, bio, image, email, linkedin, status, sort_order.
    """

    dependencies = []
    operations = []
