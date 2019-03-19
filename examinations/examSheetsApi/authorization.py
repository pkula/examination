from rest_framework import permissions


class QuestionSheetPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

    def has_permission(self, request, view):
        SAFE_METHODS = ('GET', 'POST', 'HEAD', 'OPTIONS')
        if request.method in SAFE_METHODS:
            return True


class QuestionPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


    def has_permission(self, request, view):
        SAFE_METHODS = ('GET', 'POST', 'DELETE', 'HEAD', 'OPTIONS')
        if request.method in SAFE_METHODS:
            return True


