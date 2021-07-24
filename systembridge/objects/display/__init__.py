"""
Class object for Filesystem
Documentation: https://system-bridge.timmo.dev
"""
from typing import List, Union
from ..base import BridgeBase


class DisplaysBounds(BridgeBase):
    @property
    def x(self):
        return self.attributes.get("x", None)

    @property
    def y(self):
        return self.attributes.get("y", None)

    @property
    def width(self):
        return self.attributes.get("width", None)

    @property
    def height(self):
        return self.attributes.get("height", None)


class DisplaysWorkarea(BridgeBase):
    @property
    def x(self):
        return self.attributes.get("x", None)

    @property
    def y(self):
        return self.attributes.get("y", None)

    @property
    def width(self):
        return self.attributes.get("width", None)

    @property
    def height(self):
        return self.attributes.get("height", None)


class DisplaysSize(BridgeBase):
    @property
    def width(self):
        return self.attributes.get("width", None)

    @property
    def height(self):
        return self.attributes.get("height", None)


class DisplaysWorkareasize(BridgeBase):
    @property
    def width(self):
        return self.attributes.get("width", None)

    @property
    def height(self):
        return self.attributes.get("height", None)


class DisplayInfo(BridgeBase):
    @property
    def id(self):
        return self.attributes.get("id", None)

    @property
    def bounds(self):
        return DisplaysBounds(self.attributes.get("bounds", {}))

    @property
    def workArea(self):
        return DisplaysWorkarea(self.attributes.get("workArea", {}))

    @property
    def accelerometerSupport(self):
        return self.attributes.get("accelerometerSupport", "")

    @property
    def monochrome(self):
        return self.attributes.get("monochrome", False)

    @property
    def colorDepth(self):
        return self.attributes.get("colorDepth", None)

    @property
    def colorSpace(self):
        return self.attributes.get("colorSpace", "")

    @property
    def depthPerComponent(self):
        return self.attributes.get("depthPerComponent", None)

    @property
    def size(self):
        return DisplaysSize(self.attributes.get("size", {}))

    @property
    def displayFrequency(self):
        return self.attributes.get("displayFrequency", None)

    @property
    def workAreaSize(self):
        return DisplaysWorkareasize(self.attributes.get("workAreaSize", {}))

    @property
    def scaleFactor(self):
        return self.attributes.get("scaleFactor", None)

    @property
    def rotation(self):
        return self.attributes.get("rotation", None)

    @property
    def internal(self):
        return self.attributes.get("internal", False)

    @property
    def touchSupport(self):
        return self.attributes.get("touchSupport", "")


class Display(BridgeBase):
    @property
    def brightness(self) -> int:
        return self.attributes.get("brightness", -1)

    @property
    def displays(self) -> Union[List[DisplayInfo], list]:
        return [DisplayInfo(x) for x in self.attributes.get("displays", [])]
