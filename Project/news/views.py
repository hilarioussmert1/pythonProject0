from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, UpdateView, DeleteView)
from django.views.generic.edit import CreateView
from .filters import NewsFilter
from .forms import NewsForm
from .models import News
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class NewsList(ListView):
    model = News
    ordering = 'name'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs


class NewDetail(DetailView):
    model = News
    template_name = 'new.html'
    context_object_name = 'new'


class NewsSearch(ListView):
    model = News
    ordering = 'name'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_news',)
    form_class = NewsForm
    model = News
    template_name = 'news_create.html'

    def form_valid(self, form):
        new = form.save(commit=False)
        if self.request.path == '/news/articles/create/':
            new.article_news = 'AR'
        new.save()
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, LoginRequiredMixin,  UpdateView):
    permission_required = ('news.change_news',)
    form_class = NewsForm
    model = News
    template_name = 'news_create.html'


class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class ProtectedView(LoginRequiredMixin, TemplateView):
    model = News
    template_name = 'news_create.html'
    form_class = NewsForm
    login_url = 'news'

