#pulling in other models so django/south picks them up as mentioned here:
#http://stackoverflow.com/a/6338719/173957
from scrapy_test.apps.domain.search.admin import *
from scrapy_test.apps.domain.apartment.admin import *
from scrapy_test.apps.domain.result.admin import *