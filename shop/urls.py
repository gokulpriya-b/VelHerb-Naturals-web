from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("products/<slug:slug>/", views.product_detail, name="product_detail"),
    path("custom-order/", views.custom_order, name="custom_order"),
    path("checkout/", views.checkout, name="checkout"),
    path("order-success/<int:order_id>/", views.order_success, name="order_success"),
    path("staff/orders/", views.staff_orders, name="staff_orders"),
    path("staff/order-feed/", views.order_feed, name="order_feed"),
]
