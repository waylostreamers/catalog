from django.contrib.auth.views import LoginView, LogoutView


class WayloLoginView(LoginView):
    """The login view
    """


class WayloLogoutView(LogoutView):
    """The logout view
    """

    next_page = "/"
