from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render, redirect


@login_required(login_url="/register/")
def profile_view(request):
    user = request.user
    return render(request, "accounts/profile.html", {"user": user})


@login_required(login_url="/register/")
def update_info_view(request):
    user = request.user
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        user.username = username
        user.email = email
        user.save()
        return redirect("accounts_profile_view")
    return render(request, "accounts/update_info.html", {"user": user})


@login_required(login_url="/register/")
def change_password_view(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('accounts_profile_view')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
