from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_product/', views.post_product, name="post_product"),
    path('update_product/<str:pk>', views.update_product, name="update_product"),
    path('delete_product/<str:pk>', views.delete_product, name="delete_product")
]