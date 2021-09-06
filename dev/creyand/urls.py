from django.conf.urls import include,url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

# app_name = 'creyand'
#
# router = routers.DefaultRouter()
# router.register(r'creyand',views.ADMIN_REQ)
# urlpatterns = [
#     url(r'',include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
