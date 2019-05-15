from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads') # registrando nuestros end points

urlpatterns = router.urls # Nos da los urls que creamos como end points