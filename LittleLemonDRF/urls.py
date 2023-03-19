from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
    path('categories/', views.CategoriesView.as_view()),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.single_item_view),
    path('groups/manager/users', views.managers),
    path('groups/delivery-crew/users', views.delivery_crew),
    path('cart/menu-items', views.cart_items),
    path('orders', views.orders_items),
    path('orders/<int:pk>', views.delivery_order),
]

router = routers.SimpleRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'menu-items', views.MenuItemViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'order', views.OrderItemViewSet)

urlpatterns += router.urls