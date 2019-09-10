from django.urls import path

from . import views

urlpatterns = [ 
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/<int:from_user_id>/', views.signup_from, name='signup_from'),
    path('login/<int:from_user_id>/', views.login_from, name='login_from'),
    #path('update/<int:user_id>/', views.update, name='update'),
    #path('changed/<int:user_id>/', views.changed, name='changed'),
]