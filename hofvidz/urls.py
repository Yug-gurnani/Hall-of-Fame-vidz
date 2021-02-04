from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from halls import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
	#Home
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    #AUTH
    path('signup',views.SignUp.as_view(),name = 'signup'),
    path('login',auth_views.LoginView.as_view(),name= 'login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    #Halls
    path('halloffame/create_hall',views.Create_hall.as_view(),name='create_hall'),
    path('halloffame/<int:pk>',views.Detail_hall.as_view(),name='detail_hall'),
    path('halloffame/<int:pk>/update',views.Update_hall.as_view(),name='update_hall'),
    path('halloffame/<int:pk>/delete',views.Delete_hall.as_view(),name='delete_hall'),
    # Video
    path('halloffame/<int:pk>/addvideo',views.add_video,name='addvideo'),
    path('video/search',views.video_search,name='video_search'),
    path('video/<int:pk>/delete',views.Delete_video.as_view(),name='delete_video'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
