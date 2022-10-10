from rest_framework.throttling import SimpleRateThrottle


class DetailViewThrottle(SimpleRateThrottle):
    scope = 'detailviewthrottle'
    cache_format = 'throttle_%(scope)s_%(ident)s_%(detail)s'

    def get_cache_key(self, request, view):
        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request),
            'detail': view.kwargs.get('pk')
        }