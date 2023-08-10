from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class UserIsAuthenticatedMixin(LoginRequiredMixin):
    pass


class UserIsCreatorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user == self.get_object().creator
