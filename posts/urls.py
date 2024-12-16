from . import views
from django.urls import path
from django.conf.urls import handler404
from django.conf.urls import handler500

urlpatterns = [
    path('',views.PostList.as_view(),name = 'home'),
    path('create-post/', views.create_post, name='create_post'),
    path('<slug:slug>/edit_post/<int:post_id>',
    views.post_edit, name='edit_post'),
    path('<slug:slug>/delete_post/<int:post_id>',
    views.post_delete, name='post_delete'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
    views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
    views.comment_delete, name='comment_delete'),    
]


handler404 = custom_handler404
handler500 = custom_handler500