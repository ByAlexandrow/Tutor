from django.shortcuts import render

from blog.models import Post


def index(request):
    """Showing of all chapters with their topics."""
    try:
        last_post = Post.objects.filter(
            is_published=True
        ).order_by('-date').first()
    except Exception:
        last_post = None
    
    context = {
        'last_post': last_post,
    }
    
    return render(request, 'homepage/index.html', context)
