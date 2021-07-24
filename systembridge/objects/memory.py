"""
Class object for Memory
Documentation: https://system-bridge.timmo.dev
"""
from .base import BridgeBase


class Layout(BridgeBase):
    @property
    def size(self):
        return self.attributes.get("size", None)

    @property
    def bank(self):
        return self.attributes.get("bank", "")

    @property
    def type(self):
        return self.attributes.get("type", "")

    @property
    def ecc(self):
        return self.attributes.get("ecc", False)

    @property
    def clockSpeed(self):
        return self.attributes.get("clockSpeed", None)

    @property
    def formFactor(self):
        return self.attributes.get("formFactor", "")

    @property
    def manufacturer(self):
        return self.attributes.get("manufacturer", "")

    @property
    def partNum(self):
        return self.attributes.get("partNum", "")

    @property
    def serialNum(self):
        return self.attributes.get("serialNum", "")

    @property
    def voltageConfigured(self):
        return self.attributes.get("voltageConfigured", None)

    @property
    def voltageMin(self):
        return self.attributes.get("voltageMin", None)

    @property
    def voltageMax(self):
        return self.attributes.get("voltageMax", None)


class Memory(BridgeBase):
    @property
    def total(self):
        return self.attributes.get("total", None)

    @property
    def free(self):
        return self.attributes.get("free", None)

    @property
    def used(self):
        return self.attributes.get("used", None)

    @property
    def active(self):
        return self.attributes.get("active", None)

    @property
    def available(self):
        return self.attributes.get("available", None)

    @property
    def buffers(self):
        return self.attributes.get("buffers", None)

    @property
    def cached(self):
        return self.attributes.get("cached", None)

    @property
    def slab(self):
        return self.attributes.get("slab", None)

    @property
    def buffcache(self):
        return self.attributes.get("buffcache", None)

    @property
    def swaptotal(self):
        return self.attributes.get("swaptotal", None)

    @property
    def swapused(self):
        return self.attributes.get("swapused", None)

    @property
    def swapfree(self):
        return self.attributes.get("swapfree", None)

    @property
    def layout(self):
        return [Layout(x) for x in self.attributes.get("layout", [])]
