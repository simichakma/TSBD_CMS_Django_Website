from django.db import migrations

MODULES = {
    "Software Solution": [
        ("Requirement Analysis", "We analyze your business requirements, workflow, challenges and goals to identify the right software solution."),
        ("Solution Planning", "We plan the system architecture, features, database structure and technologies required for the project."),
        ("Development & Integration", "We develop customized software and integrate databases, APIs and other required services."),
        ("Testing & Deployment", "We thoroughly test the system, resolve issues and deploy the completed solution."),
        ("Support & Maintenance", "We provide ongoing technical support, maintenance and future improvements."),
    ],
    "Web Development": [
        ("Requirement & Research", "We understand your business goals, target audience and website requirements."),
        ("UI/UX Design", "We create a clean, responsive and user-friendly interface designed around your users."),
        ("Frontend & Backend Development", "We develop the complete website with modern frontend and reliable backend technologies."),
        ("Testing & Optimization", "We test functionality, responsiveness, performance and compatibility across devices."),
        ("Deployment & Maintenance", "We deploy your website and provide ongoing updates, maintenance and technical support."),
    ],
    "Software Development": [
        ("Business Analysis", "We analyze your business processes and identify the software requirements."),
        ("Architecture & Planning", "We design a scalable architecture, database structure and technical roadmap."),
        ("Custom Development", "We build customized software according to your specific business requirements."),
        ("QA & Security Testing", "We test the software thoroughly to ensure reliability, usability, performance and security."),
        ("Deployment & Support", "We deploy the software and provide continuous technical support and improvements."),
    ],
    "Training & Internship": [
        ("Program Orientation", "Participants are introduced to the program, learning objectives, tools and professional expectations."),
        ("Learning & Fundamentals", "Participants learn core concepts and practical technologies through structured training."),
        ("Practical Projects", "Participants work on hands-on projects to apply their technical knowledge in practical situations."),
        ("Industry-Based Practice", "Participants gain practical experience through real-world tasks and professional workflows."),
        ("Evaluation & Certification", "Performance is evaluated and successful participants receive appropriate completion recognition."),
    ],
    "Affiliate Marketing": [
        ("Market & Audience Research", "We research target audiences, market trends and relevant product opportunities."),
        ("Offer & Product Selection", "We identify suitable products and offers that align with the target audience."),
        ("Content & Campaign Planning", "We develop content and promotional strategies designed to reach potential customers."),
        ("Promotion & Conversion", "We promote selected offers through suitable digital channels and optimize conversion opportunities."),
        ("Performance Tracking & Optimization", "We monitor campaign performance and improve strategies based on measurable results."),
    ],
}


def seed_modules(apps, schema_editor):
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tsbd_service_modules (
                id INT NOT NULL AUTO_INCREMENT,
                service_id INT NOT NULL,
                module_number INT NOT NULL,
                title VARCHAR(255) NOT NULL DEFAULT '',
                description TEXT NULL,
                PRIMARY KEY (id),
                UNIQUE KEY uq_tsbd_service_module (service_id, module_number),
                KEY idx_tsbd_service_modules_service (service_id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """)

        for service_name, modules in MODULES.items():
            cursor.execute("SELECT id FROM tsbd_services WHERE service_name = %s ORDER BY id ASC LIMIT 1", [service_name])
            row = cursor.fetchone()
            if not row:
                short = {
                    "Software Solution": "Customized software solutions that help businesses automate processes and improve efficiency.",
                    "Web Development": "Modern, responsive and user-focused websites and web applications.",
                    "Software Development": "Custom software engineered around your business requirements.",
                    "Training & Internship": "Practical technology training and internship opportunities with project-based learning.",
                    "Affiliate Marketing": "Structured digital promotion strategies focused on relevant offers and measurable performance.",
                }[service_name]
                cursor.execute("INSERT INTO tsbd_services (service_name, service_details, status) VALUES (%s, %s, 1)", [service_name, short])
                service_id = cursor.lastrowid
            else:
                service_id = row[0]

            for number, (title, description) in enumerate(modules, start=1):
                cursor.execute("""
                    INSERT INTO tsbd_service_modules (service_id, module_number, title, description)
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE title=VALUES(title), description=VALUES(description)
                """, [service_id, number, title, description])


def reverse_modules(apps, schema_editor):
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS tsbd_service_modules")


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.RunPython(seed_modules, reverse_modules)]
