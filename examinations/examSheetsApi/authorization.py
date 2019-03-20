from rest_framework import permissions


class QuestionSheetPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class QuestionPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user




class AnswerFormPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        SAFE_METHODS = ('POST', 'HEAD', 'OPTIONS')
        if request.method in SAFE_METHODS:
            return True
        return obj.exam_sheet_id.owner == request.user or obj.user == request.user

    def has_permission(self, request, view):
        SAFE_METHODS = ('GET', 'POST', 'HEAD', 'OPTIONS')
        if request.method in SAFE_METHODS:
            return True




class AnswerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return obj.form_id.user == request.user or obj.user == request.user
        return False


    def has_permission(self, request, view):
        SAFE_METHODS = ('GET', 'POST', 'HEAD', 'OPTIONS')
        if request.method in SAFE_METHODS:
            return True
