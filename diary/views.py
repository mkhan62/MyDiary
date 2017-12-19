from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from diary.models import Chapter, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from diary.forms import ChapterForm, CommentForm
from django.urls import reverse_lazy
# Create your views here.

class SummaryView(TemplateView):
    template_name = summary.html


class ChapterListView(ListView):
    model = Chapter

    def get_queryset(self):
        return Chapter.objects.filter(published_date__lte=timezone.now()).order_by('-published_date'))


class ChapterDetailView(DetailView):
    model = Chapter


class CreateChapterView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'diary/chapter_detail.html'

    form_class = ChapterForm
    model = Chapter

class ChapterUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'diary/chapter_detail.html'

    form_class = ChapterForm
    model = Chapter

class ChapterDeleteView(LoginRequiredMixin, DeleteView):
    model = Chapter
    success_url = reverse_lazy('chapter_list')

    # not anyone can access creating a chapter
class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'diary/chapter_list.html'
    model = Chapter

    def get_queryset(self):
        return Chapter.objects.filter(published_date__isnull=True).order_by('create_date')
