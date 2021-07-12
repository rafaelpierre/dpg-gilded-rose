from enum import Enum

from gilded_rose.gilded_rose import (
    AgedBrie,
    BackstagePass,
    Conjured,
    StandardItem,
    Sulfuras,
)

from loguru import logger


class ItemType(str, Enum):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    CONJURED = "Conjured Mana Cake"
    SULFURAS = "Sulfuras, Hand of Ragnaros"


class ItemFactory:
    @staticmethod
    def create_item(name: str, sell_in: int, quality: int):
        """Factory method which returns an object instance,
        depending on the item name.

        Args:
            name: Item name.
            sell_in: Days remaining until expiration date.
            quality: Indicates product quality.

        Returns:
            An object of class AgedBrie, BackstagePass, Conjured,
            StandardItem, or Sulfuras.
        """

        logger.debug(f"Creating item: {name}")

        if name == ItemType.AGED_BRIE:
            return AgedBrie(name, sell_in, quality)
        if name == ItemType.BACKSTAGE_PASS:
            return BackstagePass(name, sell_in, quality)
        if name == ItemType.CONJURED:
            return Conjured(name, sell_in, quality)
        if name == ItemType.SULFURAS:
            return Sulfuras(name, sell_in, quality)
        else:
            return StandardItem(name, sell_in, quality)
