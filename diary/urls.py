from django.conf.urls import url
from diary import views



urlpatterns = [
    url(r'^$', views.ChapterListView.as_view(), name='chapter_list'),
    url(r'^summary/$', viwes.SummaryView.as_view(), name='summary'),
    url(r'^chapter/(?P<pk>\d+)$', views.ChapterDetailView.as_view(), name='chapter_detail'),
    url(r'^chapter/new/$', views.CreateChapterView.as_view(), name='chapter_new'),
    url(r'^chapter/(?P<pk>\d+)/update/$', views.ChapterUpdateView.as_view(), name='chapter_update'),
    url(r'chapter/(?P<pk>\d+)/delete/$', views.ChapterDeleteView.as_view(), name='chapter_delete'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='chapter_draft_list'),
]
