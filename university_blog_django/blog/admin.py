from django.contrib import admin
from .models import Faculty, Group, Mark, Post, Subject, Lecturer, Student, GroupSubject, ExamMark

admin.site.register(Faculty)
admin.site.register(Group)
admin.site.register(Mark)
admin.site.register(Post)
admin.site.register(Subject)
admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(GroupSubject)
admin.site.register(ExamMark)