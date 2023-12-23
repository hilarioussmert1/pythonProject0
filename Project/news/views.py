from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .filters import NewsFilter
from .forms import NewsForm
from .models import News


class NewsList(ListView):
    model = News
    ordering = 'name'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2

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
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'news_create.html'


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news_create.html'

