from django.urls import path
from . import views


urlpatterns = [
    path('navbar', views.Navbar.as_view(template_name = "navbar.html"), name='navbar'),
    path('article_list', views.ArticleListView.as_view(), name='articlelist'),
    path('<int:id>', views.ArticleDetailView.as_view(), name='articledetail'),
    path('article_create', views.ArticleCreateView.as_view(), name='articlecreate'),  
    path('article_update/<int:id>', views.ArticleUpdateView.as_view(), name='articleupdate'),
    path('article_delete/<int:id>', views.ArticleDeleteView.as_view(), name="articledelete"),
]
