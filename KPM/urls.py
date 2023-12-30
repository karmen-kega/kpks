"""
URL configuration for KPM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user import views
from user.views import LoginView, RapportCreateView, UserListAPIView, RapportListView, UserListAllAPIView, PositionCreateView, RegisterView, missionListView, MissionPointListView, messageListView, UserImageView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.connection_page, name='connection'),
    path('inscription', views.inscription_page, name='inscription'),
    path('map', views.map, name='map'),
    path('gestion', views.gestion, name='gestion'),
    path('all_info',views.info_all_user, name= 'all_info'),
    path('delete_user/<int:my_id>', views.delete_user,name='delete_user'),
    path('update_user/<int:my_id>', views.update_user,name='update_user'),
    path('update_user_password/<int:my_id>', views.update_user_password,name='update_user_password'),
    path('upload_photo/<int:my_id>', views.upload_photo,name='upload_photo'),
    path('rapport', views.rapport_views,name='rapport'),
    path('delete_rapport', views.supprimer_rapport,name='delete_rapport'),
    path('mission', views.create_mission,name='mission'),
    path('message', views.create_message,name='message'),
    path('voir_message', views.voir_message,name='voir_message'),
    path('update_mission/<int:my_id>', views.update_mission,name='update_mission'),
    path('delete_mission/<int:my_id>', views.delete_mission,name='delete_mission'),
    path('voir_mission', views.voir_mission,name='voir_mission'),
    path('download_rapport', views.download_rapport,name='download_rapport'),
    path('time_connection', views.time_connection,name='time_connection'),
    path('download_connection', views.download_excel_connection,name='download_connection'),
    path('delete_connection', views.supprimer_historique_connexion,name='delete_connection'),
    path('download_traject', views.download_traject,name='download_traject'),
    path('supprimer_traject', views.supprimer_traject,name='supprimer_traject'),
    path('traject', views.time_traject,name='traject'),
    path('logout', views.logout_user,name='logout'),

    #url des api
    path('api/register', RegisterView.as_view(), name='register'),
    path('api/login', LoginView.as_view(), name='login-api'),
    path('api/rapport', RapportCreateView.as_view(), name='rapport-api'),
    path('api/mission/<int:receveur_id>', missionListView.as_view(), name='mision-api'),
    path('api/position', PositionCreateView.as_view(), name='position-api'),
    path('api/register', RegisterView.as_view(), name='register'),
    path('api/user-receveur', UserListAPIView.as_view(), name='user-list'),
    path('api/all_user', UserListAllAPIView.as_view(), name='user-list-all'),
    path('api/list_rapport/<int:envoyeur_id>', RapportListView.as_view(), name='list_rapport'),
    path('api/list_message/<int:receveur_id>', messageListView.as_view(), name='list_message'),
    path('api/sum_point/<int:receveur_id>', MissionPointListView.as_view(), name='sum_point'),
    path('api/image/<int:id>', UserImageView.as_view(), name='user-image-api')
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)