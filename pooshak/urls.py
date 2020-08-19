from django.urls import path

from pooshak import views

app_name = 'pooshak'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('product/details/<int:product_id>/', views.product_details, name="product_details"),
]
