from celery.task import task
from scrapy_test.aggregates.apartment.services import apartment_service
from scrapy_test.aggregates.search.services import search_service
from scrapy_test.apps.domain.apartment.services import add_apartment_to_search_service
from scrapy_test.apps.domain.search.services import potential_search_service, emailer_sender_service


@task
def create_apartment_task(apartment_id):
  apartment = apartment_service.get_apartment(apartment_id)

  return add_apartment_to_search_service.create_apartment(apartment).id