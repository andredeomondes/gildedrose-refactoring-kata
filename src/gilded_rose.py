from src.item import Item
from typing import List

class GildedRose:
    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self):
        for i in range(len(self.items)):
            if self.items[i].name != "Aged Brie" and self.items[i].name != "Backstage passes to a TAFKAL80ETC concert":
                if self.items[i].quality > 0:
                    if self.items[i].name != "Sulfuras, Hand of Ragnaros":
                        self.items[i].quality -= 1
            else:
                if self.items[i].quality < 50:
                    self.items[i].quality += 1
                    if self.items[i].name == "Backstage passes to a TAFKAL80ETC concert":
                        if self.items[i].sell_in < 11:
                            if self.items[i].quality < 50:
                                self.items[i].quality += 1
                        if self.items[i].sell_in < 6:
                            if self.items[i].quality < 50:
                                self.items[i].quality += 1
            if self.items[i].name != "Sulfuras, Hand of Ragnaros":
                self.items[i].sell_in -= 1
            if self.items[i].sell_in < 0:
                if self.items[i].name != "Aged Brie":
                    if self.items[i].name != "Backstage passes to a TAFKAL80ETC concert":
                        if self.items[i].quality > 0:
                            if self.items[i].name != "Sulfuras, Hand of Ragnaros":
                                self.items[i].quality -= 1
                    else:
                        self.items[i].quality = 0
                else:
                    if self.items[i].quality < 50:
                        self.items[i].quality += 1
