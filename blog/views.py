# blog/views.py
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required # Import for subscription views
from comments.forms import CommentForm
from comments.models import Comment
from .models import Post, Category # Ensure Category is imported
from django.http import JsonResponse # Keep if you use it elsewhere

def home(request):
    """
    Renders the home page with paginated posts and all categories for the sidebar.
    """
    posts = Post.objects.order_by('-likes', '-publish_date')
    paginator = Paginator(posts, 5)  # 5 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    all_categories = Category.objects.all() # Fetch all categories for the sidebar

    context = {
        'page_obj': page_obj,
        'categories': all_categories, # Add categories to the context
    }

    return render(request, "blog/base_blog.html", context)

def post_detail(request, pk):
    """
    Renders the detail page for a single post, including comments and a comment form.
    Handles comment submission.
    """
    post = get_object_or_404(Post, pk=pk)
    # Filter for top-level comments (parent__isnull=True)
    comments = post.comments.filter(parent__isnull=True).order_by('-created_at')
    form = CommentForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            # Redirect to login page with 'next' parameter to return after login
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
                    # Only allow replies to top-level comments
                    if not parent_comment.parent:
                        comment.parent = parent_comment
                except Comment.DoesNotExist:
                    pass  # Ignore bad parent_id silently
            comment.save()
            return redirect('blog:post_detail', pk=pk) # Redirect to the same post detail page

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

@login_required
def subscribe_category(request, category_id):
    """
    Allows a logged-in user to subscribe to a specific category.
    """
    category = get_object_or_404(Category, id=category_id)

    # Check if the user is already subscribed to prevent duplicates
    if category not in request.user.subscribed_categories.all():
        request.user.subscribed_categories.add(category)
        # TODO: Implement bonus: Send confirmation email here
        # send_subscription_confirmation_email(request.user, category)
        print(f"User {request.user.username} subscribed to {category.name}") # For debugging
    return redirect(request.META.get('HTTP_REFERER', reverse('home')))


@login_required
def unsubscribe_category(request, category_id):
    """
    Allows a logged-in user to unsubscribe from a specific category.
    """
    category = get_object_or_404(Category, id=category_id)

    # Check if the user is subscribed before attempting to remove
    if category in request.user.subscribed_categories.all():
        request.user.subscribed_categories.remove(category)
        print(f"User {request.user.username} unsubscribed from {category.name}") # For debugging

    return redirect(request.META.get('HTTP_REFERER', reverse('home')))

