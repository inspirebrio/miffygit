from rest_framework.pagination import LimitOffsetPagination

class ResultsSetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 50000