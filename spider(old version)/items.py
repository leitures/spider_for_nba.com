from scrapy.item import Item, Field

class FirstscrapyItem(Item):
    title = Field(serializer=str)
    link = Field(serializer=str)