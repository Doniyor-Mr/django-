from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView, CreateView

from django.urls import reverse_lazy

from .models import News, Category

from  .forms import NewsForm



class HomeNews(ListView):
    model =  News
    template_name = "news/home_news_list.html"
    context_object_name = "news"
    # extra_context = {'title': 'Eng boshi'}

    def get_context_data(self, *, object_list=None, **kwargs):
        contact = super().get_context_data(**kwargs)
        contact['title']='Glavnaya stranitsiya'
        return contact

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = "news/home_news_list.html"
    context_object_name = "news"
    allow_empty = False


    def get_context_data(self, *, object_list=None, **kwargs):
        contact = super().get_context_data(**kwargs)
        contact['title']=Category.objects.get(pk=self.kwargs['category_id'])
        return contact

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

class ViewNews(DetailView):
    model = News
    # template_name = "news/news2_detail.html" yana qoshsa boladi
    context_object_name = "news_item"


class CreateNews(CreateView):
   form_class = NewsForm
   template_name = 'news/add_news.html'
   # success_url = reverse_lazy('home',)





#
# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'YANGILIKLAR',
#     }
#     return render(request, template_name='news/index.html', context=context)

#
# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news,  'category': category})

#
# def view_news(request,news_id):
#     # news_item =News.objects.get(pk=news_id)
#     news_item =get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {"news_item":news_item})

#
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news= News.objects.create(**form.cleaned_data )
#             news = form.save()
#             redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form':form})
#
