// Copyright (c) 2016 Ultimaker B.V.
// Cura is released under the terms of the AGPLv3 or higher.

import QtQuick 2.2
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1
import QtQuick.Window 2.1

import UM 1.2 as UM
import Cura 1.0 as Cura


Cura.MachineAction
{
    anchors.fill: parent;
    Item
    {
        id: filanmentMachineAction
        anchors.fill: parent;

        UM.I18nCatalog { id: catalog; name: "cura"; }

        Label
        {
            id: filanmentText
            width: parent.width
            wrapMode: Text.WordWrap
            text: catalog.i18nc("@label", "Load new filanment, or unload old one")
        }

        Row
        {
            id: filanmentWrapper
            anchors.top: filanmentText.bottom
            anchors.topMargin: UM.Theme.getSize("default_margin").height
            anchors.horizontalCenter: parent.horizontalCenter
            width: childrenRect.width
            spacing: UM.Theme.getSize("default_margin").width

            Button
            {
                id: loadFilanmentButton
                text: catalog.i18nc("@action:button","Load filanment")
                onClicked:
                {
                    manager.loadFilanment();
                }
            }

            Button
            {
                id: extrudeButton
                text: catalog.i18nc("@action:button","Extrude more")
                onClicked:
                {
                    manager.extrudeFilanment();
                }
            }

            Button
            {
                id: unloadFilanmentButton
                text: catalog.i18nc("@action:button","Unload filanment")
                onClicked:
                {
                    manager.unloadFilanment();
                }
            }
        }

        Label
        {
            id: moveText
            anchors.top: filanmentWrapper.bottom
            anchors.topMargin: UM.Theme.getSize("default_margin").height
            width: parent.width
            wrapMode: Text.WordWrap
            text: catalog.i18nc("@label", "Move paltform and printhead")
        }

        Row
        {
            id: moveWrapper
            anchors.top: moveText.bottom
            anchors.topMargin: UM.Theme.getSize("default_margin").height
            anchors.horizontalCenter: parent.horizontalCenter
            width: childrenRect.width
            spacing: UM.Theme.getSize("default_margin").width

            Button
            {
                id: homeXYButton
                text: catalog.i18nc("@action:button","Move to home position")
                onClicked:
                {
                    manager.moveHome();
                }
            }

            Button
            {
                id: autolevelButton
                text: catalog.i18nc("@action:button","Bed autoleveling")
                onClicked:
                {
                    manager.autoLevel();
                }
            }

            Button
            {
                id: moveUpButton
                text: catalog.i18nc("@action:button","Lift up printhead")
                onClicked:
                {
                    manager.moveUp();
                }
            }
        }

        Label
        {
            id: zOffsetText
            anchors.top: moveWrapper.bottom
            anchors.topMargin: UM.Theme.getSize("default_margin").height
            width: parent.width
            wrapMode: Text.WordWrap
            text: catalog.i18nc("@label", "Set default Z-offset and move printhead to center at Z=0.0")
        }

        Row
        {
            id: zOffsetWrapper
            anchors.top: zOffsetText.bottom
            anchors.topMargin: UM.Theme.getSize("default_margin").height
            anchors.horizontalCenter: parent.horizontalCenter
            width: childrenRect.width
            spacing: UM.Theme.getSize("default_margin").width

            TextField {
              id: zOffset
              text: manager.zOffset
              placeholderText: catalog.i18nc("@label:textbox", "Z Offset...");
              inputMethodHints: Qt.ImhFormattedNumbersOnly

              onTextChanged:
              {
                  manager.zOffset = text;
              }
            }

            Button
            {
                id: zOffsetButton
                text: catalog.i18nc("@action:button","Set default Z-offset")
                onClicked:
                {
                    manager.setZoffset(zOffset.text);
                }
            }
        }
        Label
        {
            id: statusText
            anchors.top: zOffsetWrapper.bottom
            anchors.topMargin: UM.Theme.getSize("default_margin").height
            width: parent.width
            wrapMode: Text.WordWrap
            text: manager.status
        }
    }
}
