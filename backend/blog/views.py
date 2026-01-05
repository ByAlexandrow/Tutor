# from django.views.generic import ListView, DetailView
# from django.shortcuts import render
# from django.core.paginator import Paginator
# from .models import Post, Tag

# class PostsListView(ListView):
#     model = Post
#     template_name = 'blog/posts.html'
#     context_object_name = 'posts'
#     paginate_by = 6
#     ordering = ['-date']
    
#     def get_queryset(self):
#         # Получаем только опубликованные посты
#         return Post.objects.filter(is_published=True)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Добавляем теги в контекст
#         context['tags'] = Tag.objects.filter(is_published=True)
#         return context

# blog/views.py
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Post, Tag

class PostsListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True).order_by('-date')
        
        # Фильтрация по тегу (важно: проверяем параметр 'tag')
        tag_filter = self.request.GET.get('tag')
        print(f"DEBUG: Tag filter value: {tag_filter}")  # Для отладки
        
        if tag_filter:
            queryset = queryset.filter(tag__title=tag_filter)
            print(f"DEBUG: Filtered queryset count: {queryset.count()}")  # Для отладки
        
        # Поиск по тексту
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.filter(is_published=True)
        context['current_tag'] = self.request.GET.get('tag', '')
        context['search_query'] = self.request.GET.get('q', '')
        print(f"DEBUG: Current tag in context: {context['current_tag']}")  # Для отладки
        return context

# class BlogDetailView(DetailView):
#     model = Post
#     template_name = 'blog/blog_detail.html'
#     context_object_name = 'post'
    
#     def get_queryset(self):
#         # Получаем только опубликованные посты
#         return Post.objects.filter(is_published=True)


# Для главной страницы (если нужно)
# from django.views.generic import TemplateView

# class HomePageView(TemplateView):
#     template_name = 'index.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Добавляем последние 3 статьи в контекст главной страницы
#         context['latest_posts'] = Post.objects.filter(is_published=True).order_by('-date')[:3]
#         return context