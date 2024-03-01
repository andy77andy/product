from rest_framework import routers

from catalog.views import CategoryViewSet, BrandViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register("products", ProductViewSet)
router.register("brands", BrandViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = router.urls

app_name = "catalog"
