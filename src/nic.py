from random import randint

class NIC():
    def __init__(self):
        self.mac_address = NIC.gen_48bit_mac_address()

    @classmethod
    def gen_8bit_hex_str(cls):
        rand_hex = randint(0, 255)
        if int(rand_hex) < 16:
            rand_hex = "0" + str(hex(rand_hex))[2:]
        else:
            rand_hex = str(hex(rand_hex))[2:]

        return rand_hex

    @classmethod
    def gen_48bit_mac_address(cls):
        mac = ""
        for i in range(0, 6):
            mac += ":" + NIC.gen_8bit_hex_str()

        return mac[1:]
