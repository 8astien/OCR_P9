from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authentication.models import CustomUser
from user_management.models import UserFollows
from .forms import FollowForm


@login_required
def manage_follows(request):
    user = request.user
    following_users = [follow.followed_user for follow in user.following.all()]
    followers_users = [follow.user for follow in user.followed_by.all()]

    if request.method == "POST":
        form = FollowForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            if username == user.username:
                messages.error(request, "Vous ne pouvez pas vous suivre vous-même.")
            else:
                try:
                    user_to_follow = CustomUser.objects.get(username=username)
                    _, created = UserFollows.objects.get_or_create(user=user, followed_user=user_to_follow)
                    if created:
                        messages.success(request, f"Vous suivez maintenant {username}.")
                    else:
                        messages.info(request, "Vous suivez déjà cet utilisateur.")
                except CustomUser.DoesNotExist:
                    messages.error(request, "Utilisateur non trouvé.")
        return redirect("user_management:manage_follows")
    else:
        form = FollowForm()

    return render(
        request,
        "user_management/manage_follows.html",
        {"form": form, "follows": following_users, "followers": followers_users},
    )


@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(CustomUser, username=username)
    UserFollows.objects.filter(user=request.user, followed_user=user_to_unfollow).delete()
    messages.success(request, f"Vous avez arrêté de suivre {username}.")
    return redirect("user_management:manage_follows")
