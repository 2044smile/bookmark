from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark # models.py 파일에 Bookmark 를 가져와

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url'] # site_name과 url 을 출력한다.
    success_url = reverse_lazy('list') # 성공 시 bookmark_list.html 을 출력한다.
    template_name_suffix = '_create' # templates name은 bookmark_create.html

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')