from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('viewjobs', views.viewjobs, name='viewjobs'),
    path('job_details_list', views.job_details_list, name='job_details_list'),
    path('submit_form/',views.submit_form, name='submit_form'),
    path('addjobseekerprofile/', views.addjobseekerprofile, name='addjobseekerprofile'),
    path('applytojob/',views.apply_to_job, name='apply_to_job'),

]