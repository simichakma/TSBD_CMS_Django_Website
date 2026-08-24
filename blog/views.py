from django.db import connection
from django.shortcuts import redirect, render


def blog_list(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, title, short_description, content,author, status
            FROM tsbd_blog
            ORDER BY id DESC
        """)
        blogs = cursor.fetchall()
    return render(request, "blog/blog_list.html", {"blogs": blogs})


def add_blog(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        short_description = request.POST.get("short_description", "").strip()
        content = request.POST.get("content", "").strip()
        author = request.POST.get("author", "").strip()
        status = 1 if request.POST.get("status") == "1" else 0

        if title and short_description:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO tsbd_blog
                        (title, short_description, content, author, status)
                    VALUES (%s, %s, %s, %s, %s)
                """, [title, short_description, content, author, status])
            return redirect("blog-list")

    return render(request, "blog/blog_form.html")


def edit_blog(request, blog_id):
    if request.method == "POST":
        values = [
            request.POST.get("title", "").strip(),
            request.POST.get("short_description", "").strip(),
            request.POST.get("content", "").strip(),
            request.POST.get("author", "").strip(),
            1 if request.POST.get("status") == "1" else 0,
            blog_id,
        ]
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE tsbd_blog
                SET title=%s, short_description=%s, content=%s,
                    author=%s, status=%s
                WHERE id=%s
            """, values)
        return redirect("blog-list")

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, title, short_description, content, author, status
            FROM tsbd_blog WHERE id=%s
        """, [blog_id])
        blog = cursor.fetchone()

    return render(request, "blog/blog_form.html", {"blog": blog})


def delete_blog(request, blog_id):
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM tsbd_blog WHERE id=%s", [blog_id])
    return redirect("blog-list")
