from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView
from rest_framework.exceptions import PermissionDenied
from .models import BaseRegisterForm
from ..news.models import News, Category
from ..news.views import NewsList


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_user(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')

class CategoryListView(NewsList):
    model = News
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'

    def det_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
