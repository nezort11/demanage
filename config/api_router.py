from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from demanage.boards.views import BoardViewSet
from demanage.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("boards", BoardViewSet)


# api:{basename}-[detail/list]
# /api/{prefix}/{lookup}/
urlpatterns = router.urls
