from bluepy.btle import Scanner, DefaultDelegate


# noinspection PyPep8Naming
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    @staticmethod
    def handleDiscovery(device, isNewDev, isNewData, **kwargs):
        if isNewDev:
            print("Discovered device", device.addr)
        elif isNewData:
            print("Received new data from", device.addr)


scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)

for dev in devices:
    print()
    var = "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
    for (adtype, desc, value) in dev.getScanData():
        print("  %s = %s" % (desc, value))
