from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'), # :8000/bookmark
    path('add/', BookmarkCreateView.as_view(), name='add'), # :8000/bookmark/add
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]