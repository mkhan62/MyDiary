from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from diary.models import Chapter, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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


#############################

@login_required
def chapter_publish(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    chapter.publish()
    return redirect('chapter_detail', pk=pk)




@login_required
def add_comment_to_post(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.chapter = chapter
            comment.save()
            return redirect('chapter_detail', pk=chapter.pk)

    else:
        form = CommentForm()
    return render(request, 'chapter/comment_form.html', {'form': form} )


@login_required
def commeent_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('chapter_detail', pk=comment.chapter.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    chapter_pk = comment.chapter.pk
    comment.delete()
    return redirect('chapter_detail', pk=post_pk)
