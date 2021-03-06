import base64
from django.conf import settings

from scrapy.exceptions import NotConfigured


class ProxyMiddleware(object):
  def __init__(self):

    proxy_username = getattr(settings, 'PROXY_USERNAME', '')
    proxy_password = getattr(settings, 'PROXY_PASSWORD', '')
    proxy_url = getattr(settings, 'PROXY_URL', '')

    if proxy_username and proxy_password and proxy_url:
      if not proxy_url.startswith('http'):
        raise Exception('Scrapy expects a url for the proxy url. Example: http://proxy.mysite.com')

      self.proxy_auth_header = (
        'Basic ' + base64.encodestring('%s:%s' % (proxy_username, proxy_password)).replace('\n', '')
      )
      self.proxy_url = proxy_url
    else:
      #this will not kill the process, scrapy will just bypass this middleware
      raise NotConfigured

  def process_request(self, request, spider):
    # ignore if proxy is already seted
    if 'proxy' not in request.meta:
      if 'craigslist' in request.url:
        self._set_proxy(request)


  def _set_proxy(self, request):
    request.meta['proxy'] = self.proxy_url
    request.headers['Authorization'] = self.proxy_auth_header
