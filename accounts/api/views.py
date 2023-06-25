from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.models import Account, AccountStatus
from accounts.api.serializers import AccountSerializer, AccountStatusSerializer, AccountPhotoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from accounts.api.permissions import OwnAccountOrReadOnly, StatusOwnerOrReadOnly
from rest_framework.filters import SearchFilter

class AccountViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, OwnAccountOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['country']

class AccountStatusViewSet(ModelViewSet):
    serializer_class = AccountStatusSerializer
    permission_classes = [IsAuthenticated, StatusOwnerOrReadOnly]

    def get_queryset(self):
        queryset = AccountStatus.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user_account__user__username=username)
        return queryset


    def perform_create(self, serializer):
        user_account = self.request.user.account
        serializer.save(user_account=user_account)

class AccountPhotoView(generics.UpdateAPIView):
    serializer_class = AccountPhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        account_object = self.request.user.account
        return account_object
