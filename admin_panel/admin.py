from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from blog_auth.models import CustomUser
from django.contrib import admin


@staff_member_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'admin_panel/user_list.html', {'users': users})

admin.site.register(CustomUser)
