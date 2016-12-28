# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class ExampleItem(Item):
        description = Field()
        link = Field()
        crawled = Field()
        spider = Field()
        url = Field()
	joburl = Field()
	jobname = Field()
	companyaddr = Field()
	companyaddrurl = Field()
	salary = Field()
	jobdate = Field()
	exp = Field()
	education = Field()


class ExampleLoader(ItemLoader):
        default_item_class = ExampleItem
        default_input_processor = MapCompose(lambda s: s.strip())
        default_output_processor = TakeFirst()
        description_out = Join()
