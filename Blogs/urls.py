from django.urls import path
from Blogs import views

urlpatterns= [
    path('addBlogCategory/',views.add_blog_category,name='add_blog_category'),
    path('addBlog/',views.add_blog,name='add_blog'),
    path('addEvent/',views.add_event,name='add_event'),
    path('updateBlog/<int:pk>/updateBlog',views.BlogUpdateView.as_view(),name='update_blog'),
    path('deleteBlog/<int:pk>/deleteBlog',views.BlogDeleteView.as_view(),name='delete_blog'),
    path('updateBlogCategory/<int:pk>/updateBlogCategory',views.BlogCategoryUpdateView.as_view(),name='update_blogCategory'),
    path('deleteBlogCategory/<int:pk>/deleteBlogCategory',views.BlogCategoryDeleteView.as_view(),name='delete_blogCategory'),
    path('updateEvent/<int:pk>/updateEvent',views.EventsUpdateView.as_view(),name='update_event'),
    path('deleteEvent/<int:pk>/deleteEvent',views.EventsDeleteView.as_view(),name='delete_event'),
    path('viewBlogs/',views.view_blogs,name='view_blogs'),
    path('viewEvents/',views.view_events,name='view_events'),
    path('homePage/',views.homepage,name='view_homepage'),
    path('category/<int:pk>/chosenCategory',views.category_page,name='category_page'),
    path('blogItem/<int:pk>/particularblog/',views.blog_item,name='blog_item'),
]