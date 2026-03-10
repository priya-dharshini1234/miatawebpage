# myapp/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
     path('logout/', views.logout_view, name='logout'),

    # Main study pages
    
    path('study/', views.study, name='study'),

    # Student services and other pages
    path('student-services/', views.student_services, name='student_services'),
    path('research/', views.research, name='research'),
    path('faculties/', views.faculties, name='faculties'),
    path('about/', views.about, name='about'),

    # Additional links from sub-nav and mobile menu
    path('subjects/', views.subjects, name='subjects'),
    path('courses/', views.courses, name='courses'),
    path('apply/', views.apply, name='apply'),
    path('fees/', views.fees, name='fees'),
    path('international/', views.international, name='international'),
    path('experience/', views.experience, name='experience'),
    path('events/', views.events, name='events'),
    path('offer-holders/', views.offer_holders, name='offer_holders'),
    path('contact/', views.contact, name='contact'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('chap1', views.chap1, name='chap1'),
    path('ass1', views.ass1, name='ass1'),
    path('result', views.result, name='result'),
    
]
