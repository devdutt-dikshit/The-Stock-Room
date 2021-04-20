
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name="shopHome"),
    path('register/', views.register,name="register"),
    path('thnku/', views.a,name="thnku"),
    path('login/', views.login,name="login"),
    path('tracker/', views.search,name="track"),
    path('logout/', views.logout,name="logout"),
    path('pdp/<int:pk>', views.productview,name="productview"),
    path('checkout/', views.checkout,name="checkout"),
    path('additem/', views.additem,name="additem"),
    path('edit/<int:id>',views.additem),
    path('delete/<int:id>/',views.delete_view),
    path('products/<str:cat>',views.filterprods),
    path('addtcart/<int:uid>/<int:pid>',views.add_to_cart),
    path('allcategory/',views.category),
    path('cart/<int:id>',views.show_cart),
    path('itemdelete/<int:id>',views.delete_cart_item),
    path('updatecart/<int:id>/<str:q>',views.update_cart),

    path('about/', views.about),




]


