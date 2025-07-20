from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from comments.forms import CommentForm
from comments.models import Comment
from .models import Post, PostReaction
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.order_by('-likes', '-publish_date')
    paginator = Paginator(posts, 5)  # 5 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, "blog/base_blog.html", context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(parent__isnull=True).order_by('-created_at')
    form = CommentForm()
    # Fetching user reaction
    user_reaction = None
    if request.user.is_authenticated:
        user_reaction = post.reactions.filter(user=request.user).first()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={request.path}")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            parent_id = request.POST.get('parent_id')
            if parent_id:
                try:
                    parent_comment = Comment.objects.get(id=parent_id, post=post)
                    # only allow replies to top-level comments
                    if not parent_comment.parent:
                        comment.parent = parent_comment
                except Comment.DoesNotExist:
                    pass  # Ignore bad parent_id silently
            comment.save()
            return redirect('blog:post_detail',pk=pk)
    return render(request,'blog/post_detail.html',{
        'post':post,
        'comments':comments,
        'form':form,
        'user_reaction': user_reaction,
    })

@login_required
def react_to_post(request, pk, reaction_type):
    post = get_object_or_404(Post, pk=pk)
    is_like = reaction_type == 'like'

    reaction, created = PostReaction.objects.get_or_create(
        user=request.user,
        post=post,
        defaults={'is_like': is_like}
    )

    if not created:
        if reaction.is_like == is_like:
            reaction.delete()
        else:
            reaction.is_like = is_like
            reaction.save()
    post.likes = post.reactions.filter(is_like=True).count()
    post.save()
    # Auto-delete post if it gets 10+ dislikes
    if post.reactions.filter(is_like=False).count() >= 10:
        post.delete()
        return redirect('home')

    return redirect('blog:post_detail', pk=pk)