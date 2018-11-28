from django.urls import path

from . import views


app_name = 'volmap'
urlpatterns = [
    path('', views.index, name='index'),
    path('me/', views.me, name='me'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('<int:activity_id>/signup/', views.signup, name='signup'),
    path('route/<str:destination>', views.route, name='route'),
]
