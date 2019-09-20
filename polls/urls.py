from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('login',views.login_page),
    path('register',views.register_page),
    path('',views.chat_page),
    path('edit',views.edit_page),
    path('dashboard',views.dashboard_page),
    path('create_post',views.create_post),
    path('post/<int:id>/delete',views.delete_post),
    path('post_comment',views.post_comment),
    path('logout',views.log_out)
]
