"""
Class object for Graphics
Documentation: https://system-bridge.timmo.dev
"""
from .base import BridgeBase


class Controllers(BridgeBase):
    @property
    def vendor(self):
        return self.attributes.get("vendor", "")

    @property
    def model(self):
        return self.attributes.get("model", "")

    @property
    def bus(self):
        return self.attributes.get("bus", "")

    @property
    def vram(self):
        return self.attributes.get("vram", None)

    @property
    def vramDynamic(self):
        return self.attributes.get("vramDynamic", False)

    @property
    def subDeviceId(self):
        return self.attributes.get("subDeviceId", "")

    @property
    def driverVersion(self):
        return self.attributes.get("driverVersion", "")

    @property
    def name(self):
        return self.attributes.get("name", "")

    @property
    def pciBus(self):
        return self.attributes.get("pciBus", "")

    @property
    def memoryTotal(self):
        return self.attributes.get("memoryTotal", None)

    @property
    def memoryUsed(self):
        return self.attributes.get("memoryUsed", None)

    @property
    def memoryFree(self):
        return self.attributes.get("memoryFree", None)

    @property
    def utilizationGpu(self):
        return self.attributes.get("utilizationGpu", None)

    @property
    def utilizationMemory(self):
        return self.attributes.get("utilizationMemory", None)

    @property
    def temperatureGpu(self):
        return self.attributes.get("temperatureGpu", None)

    @property
    def powerDraw(self):
        return self.attributes.get("powerDraw", None)

    @property
    def powerLimit(self):
        return self.attributes.get("powerLimit", None)

    @property
    def clockCore(self):
        return self.attributes.get("clockCore", None)

    @property
    def clockMemory(self):
        return self.attributes.get("clockMemory", None)


class Displays(BridgeBase):
    @property
    def vendor(self):
        return self.attributes.get("vendor", "")

    @property
    def model(self):
        return self.attributes.get("model", "")

    @property
    def deviceName(self):
        return self.attributes.get("deviceName", "")

    @property
    def main(self):
        return self.attributes.get("main", True)

    @property
    def builtin(self):
        return self.attributes.get("builtin", False)

    @property
    def connection(self):
        return self.attributes.get("connection", "")

    @property
    def resolutionX(self):
        return self.attributes.get("resolutionX", None)

    @property
    def resolutionY(self):
        return self.attributes.get("resolutionY", None)

    @property
    def sizeX(self):
        return self.attributes.get("sizeX", None)

    @property
    def sizeY(self):
        return self.attributes.get("sizeY", None)

    @property
    def pixelDepth(self):
        return self.attributes.get("pixelDepth", "")

    @property
    def currentResX(self):
        return self.attributes.get("currentResX", None)

    @property
    def currentResY(self):
        return self.attributes.get("currentResY", None)

    @property
    def positionX(self):
        return self.attributes.get("positionX", None)

    @property
    def positionY(self):
        return self.attributes.get("positionY", None)


class Graphics(BridgeBase):
    @property
    def controllers(self):
        return [Controllers(x) for x in self.attributes.get("controllers", [])]

    @property
    def displays(self):
        return [Displays(x) for x in self.attributes.get("displays", [])]
