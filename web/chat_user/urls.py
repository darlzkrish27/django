from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^login/$',views.Login, name='login'),
    url(r'^logout/$',views.Logout,name='logut'),
    url(r'^home/$',views.Home,name='home')

    url(r'^post/$',views.Post,name='post')
    url(r'^messages/$',views.Messages,name='messages')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
