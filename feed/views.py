from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from itertools import chain
from reviews.models import Ticket, Review


@login_required
def user_posts(request):
    user = request.user
    user_tickets = Ticket.objects.filter(user=user).annotate(content_type=Value("TICKET", CharField()))
    user_reviews = Review.objects.filter(user=user).annotate(content_type=Value("REVIEW", CharField()))
    responses_to_user_tickets = (
        Review.objects.filter(ticket__user=user)
        .exclude(user=user)
        .annotate(content_type=Value("RESPONSE", CharField()))
    )

    all_posts = sorted(
        chain(user_tickets, user_reviews, responses_to_user_tickets), key=lambda post: post.time_created, reverse=True
    )

    return render(
        request,
        "feed/user_posts.html",
        {"all_posts": all_posts, "show_navigation_buttons": False, "allow_edit": True, "allow_review": False},
    )


@login_required
def feed_view(request):

    following_users = list(request.user.following.all().values_list("followed_user_id", flat=True))
    following_users.append(request.user.id)

    user_tickets = Ticket.objects.filter(user__id__in=following_users).annotate(
        content_type=Value("TICKET", CharField())
    )
    user_reviews = Review.objects.filter(user__id__in=following_users).annotate(
        content_type=Value("REVIEW", CharField())
    )

    all_posts = sorted(chain(user_tickets, user_reviews), key=lambda post: post.time_created, reverse=True)

    return render(
        request,
        "feed/user_posts.html",
        {"all_posts": all_posts, "show_navigation_buttons": True, "allow_edit": False, "allow_review": True},
    )
