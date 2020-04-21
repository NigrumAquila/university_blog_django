from django.db import models
import django.utils.timezone

class Faculty(models.Model):
    abbreviation = models.CharField(max_length = 10)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "faculties"

class Group(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

class Mark(models.Model):
    name = models.CharField(max_length = 50)
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length = 50)
    hour = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Lecturer(models.Model):
    surname = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    patronymic = models.CharField(max_length = 50)
    post = models.ForeignKey(on_delete = models.SET_NULL, to = 'Post', null = True)
    faculty = models.ForeignKey(on_delete = models.SET_NULL, to = 'Faculty', null = True)

    def __str__(self):
        return self.surname

class Student(models.Model):
    group = models.ForeignKey(on_delete = models.SET_NULL, to = 'Group', null = True)
    number = models.CharField(max_length = 10)
    surname = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    patronymic = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 40, choices = (('man', 'м'), ('woman', 'ж')), default = 'м')
    birthday = models.DateTimeField(default = django.utils.timezone.now)

    def __str__(self):
        return self.surname

class GroupSubject(models.Model):
    group = models.ForeignKey(on_delete = models.SET_NULL, to = 'Group', null = True)
    subject = models.ForeignKey(on_delete = models.SET_NULL, to = 'Subject', null = True)
    lecturer = models.ForeignKey(on_delete = models.SET_NULL, to = 'Lecturer', null = True)
    exam_test = models.CharField(max_length = 40, choices = (('exam', 'экзамен'), ('offset', 'зачет')), default = 'зачет')

    class Meta:
        db_table = "blog_group_subject"
        verbose_name = "group_subject"
        verbose_name_plural = "group_subjects"

class ExamMark(models.Model):
    group_subject = models.ForeignKey(on_delete = models.SET_NULL, to = 'GroupSubject', null=True)
    student = models.ForeignKey(on_delete = models.SET_NULL, to = 'Student', null = True)
    mark = models.ForeignKey(on_delete = models.SET_NULL, to = 'Mark', null = True)
    date = models.DateTimeField(default = django.utils.timezone.now)

    class Meta:
        db_table = "blog_exam_mark"
        verbose_name = "exam_mark"
        verbose_name_plural = "exam_marks"