from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("todo_app.urls")),
    url(r'^api-auth/', include('rest_framework.urls'))
]
