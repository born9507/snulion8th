from django.urls import path
from feedpage import views
#feeds/ 이후
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/edit', views.edit, name='edit'),
    
    path('<int:id>/comments/', views.create_comment, name='create_comment'),
    path('<int:id>/comments/<int:cid>/', views.delete_comment, name='delete_comment'),

    path('<int:pk>/like/', views.feed_like, name='like'),

    #여기서 id 는 views.py로 보내는 변수, 
    #index.html에서 숫자를 받아온다.
]
