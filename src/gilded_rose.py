class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for i in range(len(self.items)):
            if self.items[i].name.startswith("Conjured"):
                # Conjured items degrade twice as fast as normal items
                degradation = 2
                if self.items[i].sell_in <= 0:
                    degradation = 4
                self.items[i].quality = max(0, self.items[i].quality - degradation)
                self.items[i].sell_in -= 1
            elif self.items[i].name != "Aged Brie" and self.items[i].name != "Backstage passes to a TAFKAL80ETC concert":
                if self.items[i].quality > 0:
                    if self.items[i].name != "Sulfuras, Hand of Ragnaros":
                        self.items[i].quality -= 1
                if self.items[i].name != "Sulfuras, Hand of Ragnaros":
                    self.items[i].sell_in -= 1
                if self.items[i].sell_in < 0:
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
