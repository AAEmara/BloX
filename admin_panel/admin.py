from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render
from blog_auth.models import CustomUser


@staff_member_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'admin_panel/user_list.html', {'users': users})

@staff_member_required
def block_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if not user.is_superuser:
        user.is_active = False
        user.save()
    return redirect('admin_panel:user_list')

@staff_member_required
def unblock_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if not user.is_superuser:
        user.is_active = True
        user.save()
    return redirect('admin_panel:user_list')