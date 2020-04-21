from django.db.models import Count, Min, Max, Sum, When, Case, F, IntegerField, CharField, Q
from django.shortcuts import render
from django.views import generic
from .models import *


def index(request):
    return render(request, 'blog/index.html')

class SubjectListView(generic.ListView):
    model = Subject
    paginate_by = 10

class FacultyListView(generic.ListView):
    model = Faculty
    paginate_by = 10

class FacultyDetailView(generic.DetailView):
    model = Faculty

    def get_context_data(self, **kwargs):
        context = super(FacultyDetailView, self).get_context_data(**kwargs)
        context['lecturer_list'] = Lecturer.objects.filter(faculty = self.get_object()).values('surname', 'name', 'patronymic', 'post__name')
        return context

class GroupListView(generic.ListView):
    model = Group
    paginate_by = 10

class GroupDetailView(generic.DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        context['student_list'] = Student.objects.filter(group = self.get_object()).values('number', 'surname', 'name', 'patronymic', 'gender', 'birthday')
        return context

class LecturerListView(generic.ListView):
    queryset = Lecturer.objects.all().values('surname', 'name', 'patronymic', 'post__name', 'faculty__abbreviation')
    
    def get_context_data(self, **kwargs):
        context = super(LecturerListView, self).get_context_data(**kwargs)

        p_surname = self.request.GET.get('surname')
        p_name = self.request.GET.get('name')
        p_patronymic = self.request.GET.get('patronymic')
        p_post =self.request.GET.get('post')
        p_faculty = self.request.GET.get('faculty')
        
        surname = Q(surname=p_surname) if (p_surname != '' and p_surname != None) else Q()
        name = Q(name=p_name) if (p_name != '' and p_name != None) else Q() 
        patronymic = Q(patronymic=p_patronymic) if (p_patronymic != '' and p_patronymic != None) else Q()
        post = Q(post__name=p_post) if (p_post != '' and p_post != None) else Q()
        faculty = Q(faculty__abbreviation=p_faculty) if (p_faculty != '' and p_faculty != None) else Q()

        context['lecturer_list'] = Lecturer.objects.all().values('surname', 'name', 'patronymic', 'post__name', 'faculty__abbreviation').filter(surname, name, patronymic, post, faculty)
        return context

class StudentListView(generic.ListView):
    queryset = Student.objects.all().values('group__name', 'number', 'surname', 'name', 'patronymic', 'gender', 'birthday')
    
    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)

        p_group = self.request.GET.get('group')
        p_number = self.request.GET.get('number')
        p_surname = self.request.GET.get('surname')
        p_name = self.request.GET.get('name')
        p_patronymic = self.request.GET.get('patronymic')
        p_gender =self.request.GET.get('gender')
        p_birthday = self.request.GET.get('birthday')
        
        group = Q(group__name=p_group) if (p_group != '' and p_group != None) else Q()
        number = Q(number=p_number) if (p_number != '' and p_number != None) else Q()
        surname = Q(surname=p_surname) if (p_surname != '' and p_surname != None) else Q() 
        name = Q(name=p_name) if (p_name != '' and p_name != None) else Q() 
        patronymic = Q(patronymic=p_patronymic) if (p_patronymic != '' and p_patronymic != None) else Q()
        gender = Q(gender=p_gender) if (p_gender != '' and p_gender != None) else Q()
        birthday = Q(birthday=p_birthday) if (p_birthday != '' and p_birthday != None) else Q()

        context['student_list'] = Student.objects.all().values('group__name', 'number', 'surname', 'name', 'patronymic', 'gender', 'birthday').filter(group, number, surname, name, patronymic, gender, birthday)
        return context

class GroupSubjectListView(generic.ListView):
    queryset = GroupSubject.objects.all().values('id', 'group__name', 'subject__name', 'lecturer__surname', 'lecturer__name', 'lecturer__patronymic', 'exam_test')
    
    def get_context_data(self, **kwargs):
        context = super(GroupSubjectListView, self).get_context_data(**kwargs)

        p_group = self.request.GET.get('group')
        p_subject = self.request.GET.get('subject')
        p_surname = self.request.GET.get('surname')
        p_name = self.request.GET.get('name')
        p_patronymic = self.request.GET.get('patronymic')
        p_exam_test =self.request.GET.get('exam_test')
        
        group = Q(group__name=p_group) if (p_group != '' and p_group != None) else Q()
        subject = Q(subject__name=p_subject) if (p_subject != '' and p_subject != None) else Q()
        surname = Q(lecturer__surname=p_surname) if (p_surname != '' and p_surname != None) else Q() 
        name = Q(lecturer__name=p_name) if (p_name != '' and p_name != None) else Q() 
        patronymic = Q(lecturer__patronymic=p_patronymic) if (p_patronymic != '' and p_patronymic != None) else Q()
        exam_test = Q(exam_test=p_exam_test) if (p_exam_test != '' and p_exam_test != None) else Q()

        context['groupsubject_list'] = GroupSubject.objects.all().values('id', 'group__name', 'subject__name', 'lecturer__surname', 'lecturer__name', 'lecturer__patronymic', 'exam_test').filter(group, subject, surname, name, patronymic, exam_test)
        return context

class GroupSubjectDetailView(generic.DetailView):
    model = GroupSubject

    def get_context_data(self, **kwargs):
        context = super(GroupSubjectDetailView, self).get_context_data(**kwargs)
        context['groupsubject'] = GroupSubject.objects.filter(id=self.get_object().id).values('group__name', 'subject__name', 'lecturer__surname', 'lecturer__name', 'lecturer__patronymic', 'exam_test').first()
        context['exammark_list'] = ExamMark.objects.all().filter(group_subject = self.get_object()).values('student__number', 'student__surname', 'student__name', 'student__patronymic', 'mark__name', 'date')
        return context

def results(request):
    plan = GroupSubject.objects.all().values('group__name', 'exam_test').annotate(count_subject = Count('id'), max_ball = Case(When(exam_test = "экзамен", then = 5*Count('id')), When(exam_test = 'зачет', then = (1*Count('id'))), output_field = IntegerField())).order_by('group', 'exam_test')
    
    fact = ExamMark.objects.all().values('student__number', 'student__name', 'student__surname', 'student__patronymic', 'group_subject__exam_test', 'student__group__name').annotate(count_marks = Count('id'), min_mark = Min('mark__value'), sum_mark = Sum('mark__value')).order_by('student__group__name', 'student__number', 'group_subject__exam_test')
    
    for data in fact:
        data['student'] = data.get('student__surname') + ' ' + data.get('student__name')[0] + '.' + data.get('student__patronymic')[0] + '.'
        exam_test = data.get('group_subject__exam_test')
        min_mark = data.get('min_mark')
        data['total'] = 'да' if ((exam_test == 'экзамен' and min_mark > 2) or (exam_test == 'зачет' and min_mark > 0)) else 'нет'

    enumeration = enumerate(fact)
    for idx, data in enumeration:
        try:
            if fact[idx+1]['student'] == data['student']:
                if (fact[idx+1]['total'] == 'да' and data['total'] == 'да'):
                    max_ball_left = plan.filter(group__name = data['student__group__name'], exam_test = data['group_subject__exam_test'])[0]['max_ball']
                    max_ball_right = plan.filter(group__name = fact[idx+1]['student__group__name'], exam_test = fact[idx+1]['group_subject__exam_test'])[0]['max_ball']
                    if (fact[idx+1]['sum_mark'] + data['sum_mark'] == max_ball_left + max_ball_right):
                        fact[idx+1]['grant'] = '200'
                        data['grant'] = '200'
                    elif (fact[idx+1]['sum_mark'] + data['sum_mark'] == max_ball_left + max_ball_right - 1):
                        fact[idx+1]['grant'] = '150'
                        data['grant'] = '150'
                    elif (fact[idx+1]['min_mark'] > 3):
                        fact[idx+1]['grant'] = '100'
                        data['grant'] = '100'
                else:
                    fact[idx+1]['grant'] = '0'
                    data['grant'] = '0'
            
                next(enumeration)
            elif ((data['min_mark'] > 3 and data['group_subject__exam_test'] == 'экзамен') or (data['min_mark'] > 0 and data['group_subject__exam_test'] == 'зачет')):
                data['grant'] = '100'
            else:
                data['grant'] = '0'
        except IndexError:
            pass
            if ((data['min_mark'] > 3 and data['group_subject__exam_test'] == 'экзамен') or (data['min_mark'] > 0 and data['group_subject__exam_test'] == 'зачет')):
                data['grant'] = '100'
            else:
                data['grant'] = '0'
    
    uniq_students = list({v['student__number']:v for v in fact}.values())

    return render(request, 'blog/results.html', {'plan': plan, 'fact': fact, 'uniq_students': uniq_students})