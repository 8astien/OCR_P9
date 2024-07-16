from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.user.is_authenticated:

            # Liste des chemins publics (sans auth)
            public_paths = [reverse("authentication:login"), reverse("authentication:signin")]

            if request.path not in public_paths:
                return redirect(reverse("authentication:login"))
        return None
