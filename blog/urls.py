from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^post/', views.post_list, name='post_list'),
    url(r'^yuedu/', views.yuedu, name='yuedu'),
    url(r'^xiangxi/',views.home1,name="home1"),
    url(r'^xiangxi/(?P<my_args>\d+)/$',views.detail,name="detail"),
    url(r'^my_view/', views.my_view, name='my_view'),
    url(r'^home/', views.biaodan, name='home'),
    url(r'^biaodan/', views.biaodan, name='biaodan'),
    url(r'^add/', views.add, name='add'),
    url(r'^$',views.index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]