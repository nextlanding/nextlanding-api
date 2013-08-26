from scrapy_test.aggregates.listing.domain.listing_builder import ListingBuilder
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.libs.datetime_utils.parsers import datetime_parser


def get_listing(pk):
  return Listing.objects.get(pk=pk)


def get_listing_by_url(url):
  return Listing.objects.get(url=url)


def create_listing(**listing_attrs):
  builder = ListingBuilder(**listing_attrs)
  listing = builder.build_listing()
  save_or_update(listing)
  return listing


def update_listing(**listing_attrs):
  url = listing_attrs['url']
  listing = get_listing_by_url(url)
  listing.update_last_updated_date(datetime_parser.get_datetime(listing_attrs['last_updated_date'][0]))
  save_or_update(listing)
  return listing


def save_or_update(listing):
  listing.save(internal=True)
