from django.urls import path
from . import views
# from .views import PasswordResetView

urlpatterns=[
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    # path('password_reset/', PasswordResetView.as_veiw(), name= "password_reset")

    


]