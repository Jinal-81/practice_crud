from django.contrib.auth.mixins import UserPassesTestMixin


class CustomPermissionMixin(UserPassesTestMixin):
    """
    This mixin used to check permission for user
    """
    def test_func(self):
        return self.request.user.user_permissions.filter(
            codename=self.permission_required).exists()
