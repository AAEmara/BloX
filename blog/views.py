from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from comments.forms import CommentForm
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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(parent__isnull=True).order_by('-created_at')
    form = CommentForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={request.path}")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=pk)
    return render(request,'blog/post_detail.html',{
        'post':post,
        'comments':comments,
        'comment_form':form
    })