from django.urls import path

from . import views
from .views import BlogListView

urlpatterns=[
    # path('', views.index, name='index'),
    path('', BlogListView.as_view(), name='Blog'),
    path('create_blog', views.create_blog, name='create_blog'),
    path('blog_details/<int:id>', views.blog_details, name='blog_details'),
    path('edit_blog/<int:id>', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:id>', views.delete_blog, name='delete_blog'),
    path('search', views.search, name='search'),
    path('comment/<int:id>', views.comment, name='comment')


]