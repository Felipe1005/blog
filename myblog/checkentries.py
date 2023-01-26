from puput import models
from django.http import HttpResponse, response
import requests
# from django.core.cache import cache
# from django.views.decorators.cache import never_cache
# from wagtailcache.cache import nocache_page
from django.core.cache import caches

def checkallentries(request):
    base_site = 'https://felipesalas.cl'
    # base_site = 'http://localhost:8000'
    cache = caches['custom']
    entries_url = cache.get('entries_url')
    blog_page = cache.get('blog_page')
    if (entries_url == None) or (blog_page == None):
        entries = models.EntryPage.objects.get_queryset()
        blog_page = entries[0].blog_page
        entries_url = [x.relative_url(blog_page, request=request) for x in entries]
        cache.set('blog_page', blog_page)
        cache.set('entries_url', entries_url)
    cache.close()
    url_404 = '/64hdhjd'
    # entries_url.append(url_404)
    entries_url.append('/')
    
    # response = str()
    for entrie_url in entries_url:
        r = requests.get(base_site + entrie_url)
        # response = response + '----' + str(r.status_code)
        del(r)
    return HttpResponse(status=204)