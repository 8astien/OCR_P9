from django.urls import path
from .views import (
    create_or_update_review,
    create_or_update_ticket,
    create_ticket_and_review,
    delete_review,
    delete_ticket,
    respond_to_ticket,
)

app_name = "reviews"

urlpatterns = [
    path("create/", create_ticket_and_review, name="review-ticket-creation"),
    path("tickets/create/", create_or_update_ticket, name="create_ticket"),
    path("tickets/update/<int:ticket_id>/", create_or_update_ticket, name="update_ticket"),
    path("tickets/delete/<int:ticket_id>/", delete_ticket, name="delete_ticket"),
    path("tickets/respond/<int:ticket_id>/", respond_to_ticket, name="respond_to_ticket"),
    path("tickets/update/<int:ticket_id>/<int:review_id>/", create_or_update_review, name="update_review"),
    path("reviews/delete/<int:review_id>/", delete_review, name="delete_review"),
]
