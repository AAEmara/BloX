from django.shortcuts import render
from .models import Post
from django.http import JsonResponse

def home(request):
    top_posts = Post.objects.order_by('-likes', '-publish_date')[:5]
    context = {'top_posts': top_posts}
    
    #Uncomment the following line to render a template when adding the frontend and comment the JsonResponse
    # return render(request, 'home.html', {'top_posts': top_posts})

    #for testing as there's no frontend yet (you have to remove it or comment it when you add the frontend)
    # data = [{"title": post.title, "likes": post.likes, "date": post.publish_date} for post in top_posts]
    # return JsonResponse(data, safe=False)
    return render(request, "blog/base_blog.html", context)
