from django.urls import path

from . import views, class_view


urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name= "logout"),
    path('search/', class_view.SearchResultsView.as_view(), name='search-results'),
    path('product/<int:pk>/', class_view.ProductDetailsView.as_view(), name='product-detail'),
    path('product/create/', class_view.CreatePostView.as_view(), name='create-product'),
    path('product/update/<int:pk>/', class_view.UpdateProductView.as_view(), name='update-product'),
    path('product/delete/<int:pk>/', class_view.DeleteProductView.as_view(), name='delete-product'),
]
