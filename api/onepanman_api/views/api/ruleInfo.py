from rest_framework import viewsets

from onepanman_api.models import RuleInfo
from onepanman_api.serializers.ruleInfo import RuleInfoSerializer


class RuleInfoViewSet(viewsets.ModelViewSet):
    queryset = RuleInfo
    serializer_class = RuleInfoSerializer