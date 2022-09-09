from rest_framework.throttling import SimpleRateThrottle


class DetailViewThrottle(SimpleRateThrottle):
    scope = 'detailviewthrottle'

    def get_cache_key(self, request, view):
        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request)
        }