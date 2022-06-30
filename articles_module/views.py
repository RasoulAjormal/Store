# Create your views here.
from re import match

from django.db.models import Count
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView

from articles_module.models import ArticleModel, ArticleCategoryModel, ArticleCommentModel
from site_module.models import SiteBanner


class ArticlesView(ListView):
    template_name = 'articles_page.html'
    model = ArticleModel
    paginate_by = 4

    def get_queryset(self):
        queryset = super(ArticlesView, self).get_queryset()
        queryset = queryset.filter(is_active=True, is_delete=False)
        category_id = self.kwargs.get('pk')
        if category_id is not None:
            ArticleCategoryModel.objects.filter()
            queryset = queryset.filter(article_category__id__iexact=category_id)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticlesView, self).get_context_data()
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerPositions.ArticlesPageUrl)
        return context


class ArticlesDetailView(DetailView):
    template_name = 'articles_detail_page.html'
    model = ArticleModel

    def get_context_data(self, **kwargs):
        article_id = self.kwargs.get('pk')
        article: ArticleModel = kwargs.get('object')
        context = super(ArticlesDetailView, self).get_context_data()
        context['article'] = ArticleModel.objects.filter(id=article_id, is_delete=False, is_active=True).first()
        context['comments'] = ArticleCommentModel.objects.prefetch_related('articlecommentmodel_set').filter(
            article=article_id, is_read_admin=True, parent_id=None, is_delete=False)
        context['commentCount'] = ArticleCommentModel.objects.filter(article_id=article.id, is_read_admin=True).count()
        context['categories'] = ArticleCategoryModel.objects.prefetch_related('articlemodel_set').filter(
            is_active=True, parent__isnull=True)
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerPositions.ArticleDetail)
        return context


def article_categories_component(request: HttpRequest):
    article_main_categories = ArticleCategoryModel.objects.annotate(
        article_count=Count('articlemodel')).prefetch_related(
        'articlemodel_set').filter(
        is_active=True,
        parent_id=None)
    return render(request, 'components/article_category_compnation.html', {'main_categories': article_main_categories})


def add_article_comment(request: HttpRequest):
    if request.user.is_authenticated:
        Comment = request.GET.get('comment')
        parent_id = request.GET.get('parent_id')
        articleId = request.GET.get('articleId')
        Full_Name = request.GET.get('full_name')
        Email = request.GET.get('email')
        if Full_Name != '' and Comment != '' and articleId != '' and match(
                r'^[a-zA-Z1-9\.\_]+\@[a-zA-Z1-9]+\.[a-zA-Z]{3}$',
                Email):
            if parent_id != '':
                new_comment = ArticleCommentModel(article_id=articleId, message=Comment, parent_id=parent_id,
                                                  user_id=request.user.id, full_name=Full_Name)
                new_comment.save()
            else:
                new_comment = ArticleCommentModel(article_id=articleId, message=Comment, parent_id=None,
                                                  user_id=request.user.id, full_name=Full_Name)
                new_comment.save()
            context = {
                'comments': ArticleCommentModel.objects.filter(article_id=articleId, is_read_admin=True,
                                                               parent=None, is_delete=False).order_by(
                    '-createdDate').prefetch_related('articlecommentmodel_set'),
                'commentCount': ArticleCommentModel.objects.filter(is_delete=False, is_read_admin=True).count()
            }
            return render(request, 'include/article_comments_partial.html', context)
        else:
            return JsonResponse({'status': 'Invalid'})
    else:
        return JsonResponse({
            'status': 'PageLogin',
            'text': 'برای نظر دادن اول وارد شوید.',
            'icon': 'error',
            'confirmButtonText': 'ورود به سایت',
        })
