from django.contrib import admin
from django.urls import path,include
from mycompany import views
from django.shortcuts import redirect
urlpatterns = [
    path('',views.index),
    path('blog',views.blog),
    path('home',views.index),
    path('contact',views.contact),
    path('complete_blog',views.completeblog),
    path('details',views.detail),
    path('single_return/<int:Id>',views.single_return),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('single',views.blog_return),
    path('one_blog',views.single_return),
    path('single_return/home_1', views.redirect_view),
    path('single_return/blog_1', views.redirect_blog),
    path('single_return/contact_1',views.redirect_contact),
    path('single_return/complete_blog',views.completeblog),
    path('single_return/details',views.redirect_detail),
]

handler404 = "mycompany.views.page_not_found_view"