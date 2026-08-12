from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Articles
from .forms import ArticlesForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
class NewsDetails(DetailView):
    model = Articles
    template_name = 'news/Details.html'
    context_object_name = 'article'

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

@login_required
def NewsUpdateDetails(request, post_id):
    post = get_object_or_404(Articles, id=post_id)
    if post.author != request.user:
        return render(request, '403.html', status=403) 

    if request.method == 'POST':
        form = ArticlesForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('news_details', pk=post.id)
    else:
           form = ArticlesForm(instance=post)

    return render(request, 'news/details_full.html', {'form': form, 'post': post})

class NewsDeleteDetails(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = 'news/delete_news.html'
    success_url = reverse_lazy('news_home')

    def test_func(self):
        post = self.get_object()
        is_author = post.author == self.request.user
        print(f"User: {self.request.user}, Author: {post.author}, Can delete: {is_author}")
        return is_author

    def delete(self, request, *args, **kwargs):
        print("Delete method called")
        return super().delete(request, *args, **kwargs)
    
def create(request): 
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False) 
            article.author = request.user
            article.save()
            return redirect('news_home') 
        else:
            error = 'Неправильно заполнили форму'

    else:
        form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)