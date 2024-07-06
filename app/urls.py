from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from app.views import home,About,service,project,contact,blog,team
from django.contrib.auth import views as auth_view
# from .forms import MyPasswordChangeForm, MySetPasswordForm,MyPasswordResetForm
urlpatterns = [

    path('', home, name='home'),
    path('home/', home, name='home'),
    path('About/', About, name='About'),
    path('service/', service, name='service'),
    path('project/', project, name='project'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('team/', team, name='team'),
    path('testimonial/', team, name='testimonial'),

]