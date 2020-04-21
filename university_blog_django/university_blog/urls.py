from django.contrib import admin
from django.urls import path
from blog import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', LoginView.as_view(template_name = 'auth/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'auth/logout.html'), name = 'logout'),

    path('', views.index, name = 'index'),
    path('results/', views.results, name = 'results'),
    path('subjects/', views.SubjectListView.as_view(), name = 'subject_list'),    
    path('faculties/', views.FacultyListView.as_view(), name = 'faculty_list'),
    path('faculties/<int:pk>/', views.FacultyDetailView.as_view(), name = 'faculty_detail'),
    path('groups/', views.GroupListView.as_view(), name = 'group_list'),
    path('groups/<int:pk>/', views.GroupDetailView.as_view(), name = 'group_detail'),
    path('lecturers/', views.LecturerListView.as_view(), name = 'lecturer_list'),
    path('students/', views.StudentListView.as_view(), name = 'student_list'),
    path('group_subjects/', views.GroupSubjectListView.as_view(), name = 'group_subject_list'),
    path('group_subjects/<int:pk>/', views.GroupSubjectDetailView.as_view(), name = 'group_subject_detail'),
]