from django.db import migrations

MODULES = {
    "Inventory Management System": [
        ("Product & Stock Management", "Maintain products, categories, units and stock information in one organized system."),
        ("Purchase & Supplier Management", "Track suppliers, purchase records and incoming stock to keep procurement organized."),
        ("Sales & Stock Transactions", "Manage sales transactions and automatically maintain accurate stock movement records."),
        ("Reporting & Analytics", "Generate useful reports for stock position, sales activity, purchases and business performance."),
        ("User Access & System Control", "Support role-based access, operational control and reliable management of day-to-day inventory activities."),
    ],
    "Prescription Management System": [
        ("Patient Prescription Records", "Organize prescription information and maintain accessible records for efficient clinical and pharmacy workflows."),
        ("Prescription Entry & Processing", "Record and process prescription details in a structured format to reduce manual errors and improve workflow efficiency."),
        ("Medicine & Dosage Information", "Manage medicine names, dosage instructions and related prescription information in a clear and consistent format."),
        ("Prescription History & Tracking", "Keep historical prescription records available for review, monitoring and operational reference."),
        ("Reports & Management Insights", "Provide structured reports and summaries to support better administrative visibility and decision-making."),
    ],
    "Pharmacy Management System": [
        ("Medicine & Inventory Management", "Manage medicine catalogs, stock levels, expiry information and inventory movement from a centralized system."),
        ("Sales & Billing", "Handle pharmacy sales and billing workflows with organized transaction records for day-to-day operations."),
        ("Purchase & Supplier Management", "Track medicine purchases, suppliers and receiving activities to maintain a reliable supply workflow."),
        ("Expiry & Stock Monitoring", "Monitor expiry dates and stock conditions to support timely action and reduce inventory-related risks."),
        ("Reports & Business Analytics", "Generate operational reports covering sales, purchases, inventory and other key pharmacy activities."),
    ],
    "Diagnosis Management System": [
        ("Patient Information Management", "Maintain structured patient information to support efficient diagnosis and service workflows."),
        ("Diagnosis Record Management", "Record diagnosis information in an organized format for easy access, review and operational continuity."),
        ("Test & Result Tracking", "Manage diagnostic test information and results with clear records for better information handling."),
        ("History & Reporting", "Keep diagnosis history and generate structured reports to support monitoring and administrative review."),
        ("Secure Workflow Management", "Provide controlled access and organized workflows to help maintain reliable and responsible information management."),
    ],
}


def seed_product_modules(apps, schema_editor):
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tsbd_product_modules (
                id INT NOT NULL AUTO_INCREMENT,
                product_id INT NOT NULL,
                module_number INT NOT NULL,
                title VARCHAR(255) NOT NULL DEFAULT '',
                description TEXT NULL,
                PRIMARY KEY (id),
                UNIQUE KEY uq_tsbd_product_module (product_id, module_number),
                KEY idx_tsbd_product_modules_product (product_id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """)

        for product_name, modules in MODULES.items():
            cursor.execute("SELECT id FROM tsbd_products WHERE product_name = %s ORDER BY id ASC", [product_name])
            product_rows = cursor.fetchall()
            for (product_id,) in product_rows:
                for number, (title, description) in enumerate(modules, start=1):
                    cursor.execute("""
                        INSERT INTO tsbd_product_modules (product_id, module_number, title, description)
                        VALUES (%s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE title=VALUES(title), description=VALUES(description)
                    """, [product_id, number, title, description])


def reverse_product_modules(apps, schema_editor):
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS tsbd_product_modules")


class Migration(migrations.Migration):
    dependencies = [("products", "0002_delete_product")]
    operations = [migrations.RunPython(seed_product_modules, reverse_product_modules)]
