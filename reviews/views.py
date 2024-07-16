from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, TicketForm
from .models import Review, Ticket


@login_required
def create_ticket_and_review(request):
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if ticket_form.is_valid() and review_form.is_valid():
            new_ticket = ticket_form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()

            new_review = review_form.save(commit=False)
            new_review.ticket = new_ticket
            new_review.user = request.user
            new_review.save()

            return redirect("feed:user_posts")
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    return render(
        request, "reviews/review-ticket-creation.html", {"ticket_form": ticket_form, "review_form": review_form}
    )


@login_required
def create_or_update_ticket(request, ticket_id=None):
    ticket = None
    if ticket_id:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        if ticket.user != request.user:
            return redirect("feed:home")
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()
            return redirect("feed:user_posts")
    else:
        form = TicketForm(instance=ticket)
    return render(request, "reviews/ticket-creation.html", {"form": form, "ticket": ticket})


@login_required
def create_or_update_review(request, ticket_id, review_id=None):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    review = None
    if review_id:
        review = get_object_or_404(Review, pk=review_id)
        if review.user != request.user:
            return redirect("feed:home")
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.ticket = ticket
            new_review.save()
            return redirect("feed:user_posts")
    else:
        form = ReviewForm(instance=review)
    return render(request, "reviews/review-response.html", {"form": form, "ticket": ticket, "review": review})


@login_required
def respond_to_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.ticket = ticket
            new_review.user = request.user
            new_review.save()
            return redirect("feed:user_posts")
    else:
        form = ReviewForm()
    return render(request, "reviews/review-response.html", {"ticket": ticket, "form": form})


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id, user=request.user)
    ticket.delete()
    return redirect("feed:user_posts")


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect("feed:user_posts")
