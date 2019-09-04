from django.urls import path

from . import views

urlpatterns = [ 
    path('loading/<int:user_id>/', views.loading, name='loading'),
    path('<int:user_id>/', views.result, name='result'),
]