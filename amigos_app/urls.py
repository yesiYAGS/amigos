from django.urls import path
from amigos_app import views

urlpatterns = [
		path('main', views.index),
        path('reg_validate', views.reg_validate),
		path('login_validate', views.login_validate),
		path('logout', views.logout),
		path('friends', views.friends),
        path('user/add/<int:id>', views.add),
        path('user/<int:id>', views.user),
        path('user/remove/<int:id>', views.remove),
        path('home', views.home)
		
]