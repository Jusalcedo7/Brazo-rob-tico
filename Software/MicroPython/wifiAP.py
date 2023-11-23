def apConfig(ssid, pwd):
    import network
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True)
    ap_if.config(essid=ssid, password=pwd)
    while not ap_if.active():
        pass
    print('network config:', ap_if.ifconfig())

