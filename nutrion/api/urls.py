from rest_framework import routers
from .views import PatientCreateView
from .views import PatientStatsView
from .views import PatientListStatsView

router = routers.SimpleRouter()
router.register(r'patients', PatientCreateView, basename='patients')
router.register(r'add-stats', PatientStatsView, basename='patients-stats'),
router.register(r'list-stats', PatientListStatsView, basename='patientstats-list')


urlpatterns = router.urls
