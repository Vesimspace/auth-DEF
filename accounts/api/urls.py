from django.urls import path, include
from accounts.api.views import AccountViewSet, AccountStatusViewSet, AccountPhotoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user-accounts', AccountViewSet)
router.register(r'status', AccountStatusViewSet, basename='status')


urlpatterns = [
    path('', include(router.urls)),
    path('account_photo/', AccountPhotoView.as_view(), name='account-photo')
]