# -*- coding: utf-8 -*-
"""Class containing test cases for GildedRose requirements
described in README.md."""

import pytest


from gilded_rose.gilded_rose import GildedRose, StandardItem, AgedBrie
from gilded_rose.item_factory import ItemFactory, ItemType


def test_lower_quality_daily(caplog):
    """'At the end of each day our system lowers both
    values for every item.'"""

    # Act
    item = ItemFactory.create_item(name="foo", sell_in=10, quality=10)
    items = [item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    # Assert
    assert isinstance(items[0], StandardItem)
    assert item.quality == 9 and item.sell_in == 9


def test_sellin_passed_quality_degrades_twice_fast(caplog):
    """'Once the sell by date has passed, Quality degrades twice as fast.'"""

    # Act
    item = ItemFactory.create_item(name="foo", sell_in=-1, quality=10)
    items = [item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    # Assert
    assert item.quality == 8 and item.sell_in == -2


def test_aged_brie_increase_quality_sellin_passed(caplog):
    """'Aged Brie actually increases in Quality the older it gets.'"""

    # Act
    item = ItemFactory.create_item(name=ItemType.AGED_BRIE, sell_in=10, quality=10)
    items = [item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    # Assert
    assert isinstance(items[0], AgedBrie)
    assert item.quality == 11 and item.sell_in == 9


def test_quality_never_greater_fifty(caplog):
    """The Quality of an item is never more than 50."""

    # Act
    aged_brie_item = ItemFactory.create_item(
        name=ItemType.AGED_BRIE, sell_in=10, quality=50
    )
    backstage_pass_item = ItemFactory.create_item(
        name=ItemType.BACKSTAGE_PASS, sell_in=10, quality=50
    )

    items = [aged_brie_item, backstage_pass_item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 50 and items[0].sell_in == 9
    assert items[1].quality == 50 and items[1].sell_in == 9


def test_sulfuras_never_sold_decreases_quality(caplog):
    """'Sulfuras', being a legendary item, never has
    to be sold or decreases in Quality."""

    # Act
    item = ItemFactory.create_item(
        name=ItemType.SULFURAS,
        sell_in=10,
        quality=50
    )

    items = [item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 80 and items[0].sell_in == 10


def test_backstage_increase_quality_sellin_more_than_10(caplog):
    """'Backstage passes', like aged brie, increases in Quality
    as it’s SellIn value approaches; (...)"""

    # Act
    item = ItemFactory.create_item(name=ItemType.BACKSTAGE_PASS, sell_in=11, quality=30)

    items = [item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 31 and items[0].sell_in == 10


def test_backstage_increase_quality_sellin_between_5_and_10(caplog):
    """'Backstage passes', like aged brie, increases in Quality
    as it’s SellIn value approaches; (...)"""

    # Act
    item = ItemFactory.create_item(name=ItemType.BACKSTAGE_PASS, sell_in=6, quality=30)

    items = [item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 32 and items[0].sell_in == 5


def test_backstage_increase_quality_sellin_between_0_and_5(caplog):
    """Quality drops (...)by 3 when there are 5 days or less"""

    # Act
    item = ItemFactory.create_item(name=ItemType.BACKSTAGE_PASS, sell_in=4, quality=30)

    items = [item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 33 and items[0].sell_in == 3


def test_backstage_increase_quality_sellin_zero_or_less(caplog):
    """(...)Quality drops to 0 after the concert."""

    # Act
    item = ItemFactory.create_item(name=ItemType.BACKSTAGE_PASS, sell_in=0, quality=30)

    items = [item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 0 and items[0].sell_in == -1


def test_conjured(caplog):
    """'Conjured' items degrade in Quality twice as fast as normal items."""

    # Act
    item = ItemFactory.create_item(name=ItemType.CONJURED, sell_in=10, quality=10)

    items = [item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 8 and items[0].sell_in == 9


def test_item_repr(caplog):

    # Act
    item = ItemFactory.create_item(name=ItemType.CONJURED, sell_in=10, quality=10)

    assert repr(item) == "ItemType.CONJURED, 10, 10"
