from django.urls import path

from . import views

urlpatterns = [ 
    path('question_set_1/<int:user_id>/', views.question_set_1, name='question_set_1'),
    path('question_set_2/<int:user_id>/', views.question_set_2, name='question_set_2'),
    path('question_set_3/<int:user_id>/', views.question_set_3, name='question_set_3'),
    path('question_set_4/<int:user_id>/', views.question_set_4, name='question_set_4'),
    path('question_set_5/<int:user_id>/', views.question_set_5, name='question_set_5'),
]