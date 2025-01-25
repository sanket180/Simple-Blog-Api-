from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register("users", views.UserViewSet,basename="users")
router.register("", views.PostViewSet,basename="posts")


urlpatterns = router.urls





# urlpatterns = [
#     path("", views.PostList.as_view(),name="post_list"),
#     path("<int:pk>/", views.PostDetail.as_view(),name="post_detail"),
#     path("users/", views.ListUser.as_view(),name="user_list"),
#     path("users/<int:pk>/", views.DetailUser.as_view(),name="user_detail"),
# ]