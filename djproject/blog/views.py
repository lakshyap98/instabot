from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    View
)
from .models import Article
from .forms import ArticleModelForm
from django.urls import reverse

class Navbar(View):
    template_name = "navbar.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class ArticleUpdateView(UpdateView):
    form_class = ArticleModelForm
    template_name = "article/article_create.html"
    # queryset = Article.objects.all()

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleCreateView(CreateView):
    # queryset = Article.objects.all()
    form_class = ArticleModelForm
    template_name = "article/article_create.html"
    # success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    # def success_url(self):
        # return "\"

class ArticleListView(ListView):
    # return <modelname>_<viewname> (article_list.html)
    # return object_list (deafult)
    queryset = Article.objects.all()
    template_name = "article/article_list.html"

class ArticleDetailView(DetailView):
    # return <modelname>_<viewname> (article_list.html)
    # return object (default)
    # queryset = Article.objects.all()
    template_name = "article/article_detail.html"

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)

class ArticleDeleteView(DeleteView):
    template_name = "article/article_delete.html"
    # success_url = reverse('articlelist')

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)
    
    def get_success_url(self):
        import pdb; pdb.set_trace()
        return reverse('articlelist')