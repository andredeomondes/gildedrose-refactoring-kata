from src.item import Item
from src.gilded_rose import GildedRose


class TestGildedRose:
    def test_normal_item_before_sell_date(self):
        item = Item("Elixir of the Mongoose", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.sell_in == 4
        assert item.quality == 9

    def test_normal_item_after_sell_date(self):
        item = Item("Elixir of the Mongoose", 0, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.sell_in == -1
        assert item.quality == 8

    def test_normal_item_quality_never_negative(self):
        item = Item("Elixir of the Mongoose", 5, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 0

    def test_aged_brie_increases_quality(self):
        item = Item("Aged Brie", 2, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 1
        assert item.sell_in == 1

    def test_aged_brie_quality_max_50(self):
        item = Item("Aged Brie", 2, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 50

    def test_aged_brie_increases_double_after_sell_date(self):
        item = Item("Aged Brie", 0, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 2

    def test_sulfuras_never_changes(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.sell_in == 0
        assert item.quality == 80

    def test_sulfuras_negative_sell_in(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.sell_in == -1
        assert item.quality == 80

    def test_backstage_pass_increases_quality(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 21

    def test_backstage_pass_quality_zero_after_sell_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 0

    def test_backstage_pass_double_quality_when_10_days(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 22

    def test_backstage_pass_triple_quality_when_5_days(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 23

    def test_backstage_pass_quality_max_50(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 50

    def test_conjured_item_degrades_twice_as_fast_before_sell(self):
        item = Item("Conjured Mana Cake", 3, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 8

    def test_conjured_item_degrades_twice_as_fast_after_sell(self):
        item = Item("Conjured Mana Cake", 0, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 6

    def test_conjured_item_quality_never_negative_before_sell(self):
        item = Item("Conjured Mana Cake", 5, 1)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 0

    def test_conjured_item_quality_never_negative_after_sell(self):
        item = Item("Conjured Mana Cake", 0, 3)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 0

    def test_conjured_item_quality_zero_stays_zero(self):
        item = Item("Conjured Mana Cake", 5, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 0

    def test_conjured_item_sell_in_decreases(self):
        item = Item("Conjured Mana Cake", 3, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.sell_in == 2

    def test_conjured_item_quality_max_50(self):
        item = Item("Conjured Mana Cake", 5, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 48
        assert item.quality <= 50

