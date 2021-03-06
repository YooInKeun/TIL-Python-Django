from django.urls import path
import blog.views

urlpatterns = [
    path('new/', blog.views.new, name = 'new'),
    path('create/', blog.views.create, name = 'create'),
    path('portfolio/', blog.views.portfolio, name='portfolio'),
    path('blog/<int:blog_id>/', blog.views.detail, name='detail'),
    path('newblog/', blog.views.blogpost, name="newblog"),
]