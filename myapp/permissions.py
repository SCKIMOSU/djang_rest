from rest_framework.permissions import IsAuthenticated

from myapp.models import Post


class AuthorCheckPermission(IsAuthenticated):
    # API 호출 권한
    def has_permission(self, request, view):
        # List/Retrieve 작업에 대해서는 항상 허용
        if request.method == "GET":
            return True
        # 이외의 기능은 IsAuthenticated를 통과해야 함
        else:
            return super().has_permission(request, view)

    # 특정 Object를 대상으로 하는 API에 대한 호출 권한
    # ex1. 로그인하지 않은 사용자의 경우
    # /api/students/ (O)
    # /api/students/1/ (X)
    # ex2. 로그인 한 사용자이지만, Post의 작성자가 아닌 경우
    # /api/students/ (O)
    # /api/students/1/ (X)
    # ex3. 로그인 한 사용자이며, Post의 작성자인 경우
    # /api/students/ (O)
    # /api/students/1/ (O)
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        else:
            if isinstance(obj, Post):
                return obj.author == request.user
            else:
                return True
