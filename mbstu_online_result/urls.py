
from django.contrib import admin
from django.urls import include,path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

   # path('login', views.user_login, name='login'),

    #path('logout/', views.user_logout, name='logout'),

    #path('signup/', views.user_signup, name='signup'),

    #path('', views.home, name="home"),


    path('student/', include('student.urls')),

    path('teacher/', include('teacher.urls')),



    path('api/', include('api.urls')),

    path('', include('Authenticate.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)