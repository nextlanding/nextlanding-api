import json
from celery.task import task
from django.conf import settings
from django.db import transaction
from django.forms import model_to_dict
from scrapy_test.aggregates.search.models import Search
from scrapy_test.aggregates.search.services import search_service
from scrapy_test.apps.domain.search.models import PotentialSearch
from scrapy_test.apps.domain.search.services import potential_search_service
from scrapy_test.apps.domain.search.signals import potential_search_completed
from scrapy_test.libs.payment_utils.services import payment_service


@task
def associate_search_task(search_id, potential_search_id):
  search = search_service.get_search(search_id)
  potential_search = potential_search_service.get_potential_search(potential_search_id)

  return potential_search_service.associate_search(search, potential_search).id
