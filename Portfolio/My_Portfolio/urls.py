from django.urls import path
from My_Portfolio import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('update/<int:id>', views.Profile, name = "update"),
    path('img/<int:id>', views.Project, name = "img"),
    path('deleteEducation/<int:id>', views.deleteEducation, name = "delete-education"),
    path('deleteLanguage/<int:id>', views.deleteLanguage, name = "delete-language"),
    path('deleteExperience/<int:id>', views.deleteExperience, name = "delete-experience"),
    path('deleteSkill/<int:id>', views.deleteSkill, name = "delete-skill"),
    path('deleteProject/<int:id>', views.deleteProject, name = "delete-project"),
    path('deleteMessage/<int:id>', views.deleteMessage, name = "delete-message"),
    path('UpdateEducation/<int:id>', views.UpdateEducation, name = "update-education"),
    path('UpdateExperience/<int:id>', views.UpdateExperience, name = "update-experience"),
    path('UpdateLanguage/<int:id>', views.UpdateLanguage, name = "update-language"),
]