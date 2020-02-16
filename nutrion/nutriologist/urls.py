from django.urls import path
from rest_framework import routers

from nutriologist import views
#router = routers.DefaultRouter()
#router.register('hello', views.HelloView.as_view(), "hello")

urlpatterns =[
    path('login/', views.LoginAdminView.as_view(), name="login_view"),
    path('logout/', views.logout_view, name='logut_view'),
    path('home/', views.HomeAdminView.as_view(), name='home_admin_view'),
    path('clients/', views.ClientsAdminView.as_view(), name='clients_admin_view'),
    path('appointments/', views.CalendarAdminView.as_view(), name='citas_admin_view'),
    path('clients/search/<str:query>/', views.ClientsAdminQueryView.as_view(), name='clients_search_view' ),
    path('home/add-client/', views.AddClientAdminView.as_view(), name='add_client_view'),
    path('clients/<int:pk>/', views.SingleClientView.as_view(), name='single_client_view'),

]
