from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet, get_new_token,
                    register)

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='User')
router.register('categories', CategoryViewSet, basename='Categories')
router.register('genres', GenreViewSet, basename='Genres')
router.register('titles', TitleViewSet, basename='Titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', register, name='signup'),
    path('v1/auth/token/', get_new_token, name='token')
]
