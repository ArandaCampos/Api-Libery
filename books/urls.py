from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from books.api.viewsets import bookViewSets

app_name = "api"

router = DefaultRouter(trailing_slash=False)
router.register(r'books', bookViewSets)

urlpatterns = router.urls