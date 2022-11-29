from django.contrib import admin 
from django.urls import path, include 
from register import views as v 
from django.contrib.auth import views as auth_views 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User 
from register.forms import MyAuthForm 
 
urlpatterns = [ 
         
         
        path('admin/', admin.site.urls), 
        path('', v.redirect_login,name="login"), 
        path("register/", v.register, name="register"), 
 
        path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset/reset_password.html'),name='reset_password'), 
        path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_sent.html'),name='password_reset_done'), 
        path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_form.html'),name='password_reset_confirm'), 
        path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_complete.html'),name='password_reset_complete'), 
        path('', include("main.urls")), 
        path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=MyAuthForm), name='login'), 
        path('', include("django.contrib.auth.urls")), 
         
    ] 
# handler404 = 'main.views.handler404' 
# handler500 = 'main.views.handler500'