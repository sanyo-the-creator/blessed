from . import views
from django.urls import path
from django.conf import settings #add this
from django.conf.urls.static import static
urlpatterns = [
    path("home/", views.home, name="home"),
    path("myproducts/", views.userproducts, name="myproducts"),
    path("add/", views.addProducts, name="add"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)