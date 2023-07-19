from django.contrib.auth.mixins import UserPassesTestMixin

class UserIsCreatorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user == self.get_object().creator
