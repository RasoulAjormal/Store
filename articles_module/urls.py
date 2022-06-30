from django.urls import path

from articles_module import views

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='ArticlesPageUrl'),
    path('cat/<pk>/', views.ArticlesView.as_view(), name='ArticleByCategory'),
    path('<pk>/', views.ArticlesDetailView.as_view(), name='ArticleDetail'),
    path('add-article-comment', views.add_article_comment, name='AddArticleComment'),

]
