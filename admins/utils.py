from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User


# Validate if the user is allowed to visit the site
def validate_access(request, role, message=""):
    user = User.objects.get(username=request.user)
    if user.staff.role != role:
        raise PermissionDenied(message)
    return user
