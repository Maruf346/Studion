from rest_framework.permissions import BasePermission, SAFE_METHODS # type: ignore

class IsAdminOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        # Allow read-only methods for all users
        if request.method in SAFE_METHODS:
            return True
        # Write permissions only for admin users
        return request.user and request.user.is_staff
