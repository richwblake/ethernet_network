from nic import NIC

class Node():
    def __init__(self, name: str):
        self.name = name
        self.nic = NIC()

    def get_name(self):
        return self.name

    def get_mac_address(self):
        return self.nic.mac_address

    def to_str(self):
        print(f"name: {self.get_name()}\nMAC address: {self.get_mac_address()}")
