from cura.MachineAction import MachineAction
from cura.PrinterOutputDevice import PrinterOutputDevice

from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot

from UM.Application import Application
from UM.Logger import Logger
from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")


class FilanmentMachineAction(MachineAction):
    def __init__(self):
        super().__init__("Filanment", catalog.i18nc("@action", "Printrbot operations"))
        self._qml_url = "FilanmentMachineAction.qml"
        self._zOffset = "0.0"
        self.statusText = ""

    def _execute(self):
        pass

    def _reset(self):
        self._zOffset = "0.0"
        pass

    @pyqtProperty(str)
    def zOffset(self):
        return self._zOffset

    @zOffset.setter
    def zOffsetChanged(self,newOffset):
        self._zOffset = newOffset

    statusChanged = pyqtSignal()

    @pyqtProperty(str, notify = statusChanged)
    def status(self):
        return self.statusText

    def setStatus(self,statusText):
        self.statusText = statusText
        self.statusChanged.emit()

    def send(self,device,command,st = None):
        if(st):
            self.setStatus(st)
        else:
            self.setStatus("Send command: "+command)
        device.sendCommand(command)

    @pyqtSlot()
    def loadFilanment(self):
        output_device = self._getOutputDevice()
        if output_device:
            self.send(output_device,"M83")
            self.send(output_device,"M109 S200")
            self.send(output_device,"G1 E20 F500")
            self.send(output_device,"G1 E20 F500")
            self.send(output_device,"M104 S0")
            self.send(output_device,"M84","Filanment loaded")

    @pyqtSlot()
    def extrudeFilanment(self):
        output_device = self._getOutputDevice()
        if output_device:
            self.send(output_device,"M83")
            self.send(output_device,"M109 S200")
            self.send(output_device,"G1 E20 F500")
            self.send(output_device,"M104 S0")
            self.send(output_device,"M84","Filanment extruded")

    @pyqtSlot()
    def unloadFilanment(self):
        output_device = self._getOutputDevice()
        if output_device:
            self.send(output_device,"M83")
            self.send(output_device,"M109 S200")
            self.send(output_device,"G1 E-20 F500")
            self.send(output_device,"G1 E-20 F500")
            self.send(output_device,"M104 S0")
            self.send(output_device,"M84","Filanment unloaded")

    @pyqtSlot()
    def moveHome(self):
        output_device = self._getOutputDevice()
        if output_device:
            output_device.homeHead()

    @pyqtSlot()
    def autoLevel(self):
        output_device = self._getOutputDevice()
        if output_device:
            self.send(output_device,"G28 X0 Y0")
            self.send(output_device,"G28 Z0")
            self.send(output_device,"G29")
            self.send(output_device,"M84","Bed leveled")

    @pyqtSlot()
    def moveUp(self):
        output_device = self._getOutputDevice()
        if output_device:
            self.send(output_device,"G91")
            self.send(output_device,"G1 Z+25")
            self.send(output_device,"M84","Lifted")

    @pyqtSlot(str)
    def setZoffset(self,offset):
        output_device = self._getOutputDevice()
        if output_device:
            self.send(output_device,"M212 Z%s" % (offset) )
            self.send(output_device,"M500")
            self.autoLevel()
            self.send(output_device,"G90")
            self.send(output_device,"G1 X50 Y100 Z0 F","Printhead at Z0, check height")

    def _getOutputDevice(self):
        output_devices = self._getPrinterOutputDevices()
        if output_devices:  # We found at least one output device
            Logger.log("d","Found output devices: %s",str(output_devices))
            return output_devices[0]
        else:
            Logger.log("d","No output device found: %s",str(output_devices))
            self.setStatus("Not connected")
            return []

    def _getPrinterOutputDevices(self):
        return [printer_output_device for printer_output_device in Application.getInstance().getOutputDeviceManager().getOutputDevices() if isinstance(printer_output_device, PrinterOutputDevice)]

