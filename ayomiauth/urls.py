from django.contrib import admin
from django.urls import path, include

from ayomiauth.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.my_account, name='profile'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('admin/', admin.site.urls),
]
