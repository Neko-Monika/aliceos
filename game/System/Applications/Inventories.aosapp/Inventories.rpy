# 
# Inventories.rpy
# AliceOS
# 
# Created by Marquis Kurt on 9/13/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

init 10 python:

    class ASInventories(ASAppRepresentative):
        bundleName = "Инвентарь"
        bundleId = "app.aliceos.inventories"
        bundleDir = AS_DEFAULT_APP_DIR + "Inventories.aosapp/"
        bundleAuthor = "Project Alice"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Просмотр, использование и управление предметами, добавленными во внутриигровой инвентарь; Инвентарь – это простое приложение, созданное для упрощения систем инвентарей.
        """

        requires = { AS_REQUIRES_NOTIFICATIONKIT }

        inventory = []

        def applicationWillLaunch(self):
            renpy.show_screen("ASInventoryManagerView")
            return

        def callRecentItems(self):
            renpy.show_screen("ASInventorySubView")
            return

        def isEmpty(self):
            return len(self.inventory) == 0

        def retrieve(self):
            print "WARN: ASInventories.retrieve is deprecated. Please use ASInventories.export instead."
            return self.export()

        def export(self, filter=None):
            new_inventory = self.inventory.copy()
            if callable(filter):
                new_inventory = map(filter, new_inventory)
            return new_inventory

        def containsItem(self, item):
            return item in self.inventory

        def getItemById(self, itemId):
            for item in self.inventory:
                if item.itemId == itemId:
                    return item
            return None

        def getItemByName(self, name):
            for item in self.inventory:
                if item.name == name:
                    return item
            return None

        def addItem(self, item, silent=False):
            if isinstance(item, ASInventoryItem):
                self.inventory.append(item)
                if not silent:
                    shouldDisplayItem = self.applicationWillRequestNotification("Получен предмет: %s!" % (item.name), "Откройте Инвентарь, чтобы узнать больше.")

                    if shouldDisplayItem == "didClickRespond":
                        renpy.show_screen("ASInventoryManagerView", currentItem=item)
            else:
                raise TypeError("Expected item to be ASInventoryItem, but received %s" % (type(item)))

        def useItem(self, item):
            if item in self.inventory:
                shouldDispose = item.useItem()

                if shouldDispose:
                    self.inventory.remove(item)
            else:
                raise KeyError("Item not found in the inventory: %s" % (item,) )

        def removeItem(self, item):
            if item in self.inventory:
                self.inventory.remove(item)
            else:
                raise KeyError("Item not found in the inventory: %s" % (item,) )

        def importFromList(self, list):

            listAsInventoryChecks = map(lambda x: isinstance(x, ASInventoryItem), list)
            isInventoryReal = reduce(lambda x, y: x and y, listAsInventoryChecks)

            if isInventoryReal:
                for item in list:
                    self.inventory.append(item)
            else:
                raise TypeError("List contains non-ASInventoryItem items.")


        def __init__(self):
            ASAppRepresentative.__init__(self, AS_DEFAULT_APP_DIR + "Inventories.aosapp/")

    inventory = ASInventories()