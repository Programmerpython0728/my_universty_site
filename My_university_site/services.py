from django.db import connection
from contextlib import closing

def dictfetchall(cursor):
    columns=[col[0] for col in cursor.description]
    return [
        dict(zip(columns,row)) for row in cursor.fetchall()
    ]
def dictfetchone(cursor):
    columns=[col[0] for col in cursor.description]
    return [
        dict(zip(columns,row)) for row in cursor.fetchone()
    ]

def get_faculty():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from My_university_site_faculty""")
        faculties=dictfetchall(cursor)
        return faculties

def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from My_university_site_kafedra""")
        kafedra=dictfetchall(cursor)
        return kafedra

def get_subject():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" select * from My_university_site_subject""")
        subjects=dictfetchall(cursor)
        return subjects

def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" select * from My_university_site_teacher""")
        teachers=dictfetchall(cursor)
        return teachers

def get_group():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from My_university_site_group""")
        groups=dictfetchall(cursor)
        return groups

def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from My_university_site_student""")
        students= dictfetchall(cursor)
        return students

