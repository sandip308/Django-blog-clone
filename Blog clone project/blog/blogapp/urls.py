
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Postlistview.as_view(),name='post_list'),
    path('about/',views.Aboutview.as_view(),name='about'),
    path('post/<int:pk>',views.Postdetailview.as_view(),name='post_detail'),
    path('post/newpost',views.Createpostview.as_view(),name='new_post'),
    path('post/<int:pk>/updatepost',views.Postupdateview.as_view(),name='update_post'),
    path('postdelete/<int:pk>',views.Postdeleteview.as_view(),name='delete_post'),
    path('drafts/',views.Postdraftview.as_view(),name='draft_post'),
    path('addcomment/<int:pk>',views.add_comment,name='add_comment'),
    path('commentapproved/<int:pk>',views.comment_approve,name='comment_approve'),
    path('removecomment/<int:pk>',views.comment_remove,name='comment_remove'),
    path('postpublish/<int:pk>',views.post_publish,name='post_publish'),
]