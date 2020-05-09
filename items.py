from config import *

class Item:
    def __init__(self, iid):
        self.id = iid
        self.dropped = False

class BackPack:
    def __init__(self, row):
        self.row = row
        self.items = [[None, None, None, None, None] for _ in range(row)]



