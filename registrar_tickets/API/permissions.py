from rest_framework.permissions import BasePermission, SAFE_METHODS


class PermissionEspecial(BasePermission):
    message = 'Debes cumplir con este tipo de permiso'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return request.user.username.startwith('f')

# Tipo de permiso especial que si se agrega a los permisos solo se podria agregar ticket a los
# usuarios administradores y que su nombre comience con la letra 'f'
