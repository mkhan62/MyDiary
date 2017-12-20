from django.conf.urls import url
from diary import views



urlpatterns = [
    url(r'^$', views.ChapterListView.as_view(), name='chapter_list'),
    url(r'^summary/$', views.SummaryView.as_view(), name='summary'),
    url(r'^chapter/(?P<pk>\d+)/$', views.ChapterDetailView.as_view(), name='chapter_detail'),
    url(r'^chapter/new/$', views.CreateChapterView.as_view(), name='chapter_new'),
    url(r'^chapter/(?P<pk>\d+)/update/$', views.ChapterUpdateView.as_view(), name='chapter_update'),
    url(r'chapter/(?P<pk>\d+)/delete/$', views.ChapterDeleteView.as_view(), name='chapter_delete'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='chapter_draft_list'),
    url(r'^chapter/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^chapter/(?P<pk>\d+)/publish/$', views.chapter_publish, name='chapter_publish'),
]
