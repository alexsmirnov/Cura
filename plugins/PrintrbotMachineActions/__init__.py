# Copyright (c) 2016 Ultimaker B.V.
# Cura is released under the terms of the AGPLv3 or higher.

from . import FilanmentMachineAction

from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")

def getMetaData():
    return {
        "plugin": {
            "name": catalog.i18nc("@label", "Printrbot machine actions"),
            "author": "alexsmirnov",
            "version": "1.0",
            "description": catalog.i18nc("@info:whatsthis", "Provides machine actions for Printrbot machines (such as filanment change, movements, etc)"),
            "api": 3
        }
    }

def register(app):
    return { "machine_action": [FilanmentMachineAction.FilanmentMachineAction()]}
