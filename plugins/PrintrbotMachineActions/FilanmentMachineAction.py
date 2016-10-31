from cura.MachineAction import MachineAction
from cura.PrinterOutputDevice import PrinterOutputDevice

from PyQt5.QtCore import pyqtSlot

from UM.Application import Application
from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")


class FilanmentMachineAction(MachineAction):
    def __init__(self):
        super().__init__("Filanment", catalog.i18nc("@action", "Level build plate"))
        self._qml_url = "FilanmentMachineAction.qml"
        self.zOffset = ""
        self._zOffset = 0

    def _execute(self):
        pass

    def _reset(self):
        self.zOffset = ""
        self._zOffset = 0
        pass

    @pyqtSlot()
    def loadFilanment(self):
        output_device = self._getOutputDevice()
        if output_device:
            printer_output_devices[0].homeBed()

    @pyqtSlot()
    def extrudeFilanment(self):
        output_device = self._getOutputDevice()
        if output_device:
            printer_output_devices[0].homeBed()

    @pyqtSlot()
    def loadFilanment(self):
        output_device = self._getOutputDevice()
        if output_device:
            printer_output_devices[0].homeBed()

    @pyqtSlot()
    def moveHome(self):
        output_device = self._getOutputDevice()
        if output_device:
            printer_output_devices[0].homeBed()

    @pyqtSlot()
    def autoLevel(self):
        output_device = self._getOutputDevice()
        if output_device:
            printer_output_devices[0].homeBed()

    @pyqtSlot()
    def moveUp(self):
        output_device = self._getOutputDevice()
        if output_device:
            printer_output_devices[0].homeBed()

    @pyqtSlot()
    def setZoffset(self,offset):
        output_device = self._getOutputDevice()
        if output_device:
            printer_output_devices[0].homeBed()

    def _getOutputDevice(self):
        output_devices = self._getPrinterOutputDevices()
        if output_devices:  # We found at least one output device
            return output_devices[0]
        else:
            return false

    def _getPrinterOutputDevices(self):
        return [printer_output_device for printer_output_device in Application.getInstance().getOutputDeviceManager().getOutputDevices() if isinstance(printer_output_device, PrinterOutputDevice)]

