from rest_framework import routers
from myapp.views import TodoViewset
router = routers.DefaultRouter()
router.register(r'myapp',TodoViewset)