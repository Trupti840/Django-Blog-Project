#blog/urls.py

from django.urls import path
# from . import views
from .views import HomeView, CategoriesView, BlogDeatilView, CreateBlogView, CreateCommentView, CreateCategoryView, UpdateBlogView, DeleteCategoryView, DeleteBlogView

urlpatterns = [
    # path('', views.home, name='home'),
    # Add other URL patterns as needed
    path('', HomeView.as_view(), name='home'),
    # below is the expale for show page (showing post for perticular id which is primary key(pk))
    path('blog/<int:pk>', BlogDeatilView.as_view(), name='blog_detail'),
    path('addblog', CreateBlogView.as_view() , name="add_blog"),
    path('post/<int:post_id>/comment/', CreateCommentView.as_view(), name='create_comment'),
    path('update_blog/<int:pk>', UpdateBlogView.as_view(), name='update_blog'),
    path('blog/<int:pk>/delete', DeleteBlogView.as_view(), name='delete_blog'),
    path('addcategory', CreateCategoryView.as_view() , name="add_category"),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('category/<int:pk>/delete', DeleteCategoryView.as_view(), name='delete_category'),

]
