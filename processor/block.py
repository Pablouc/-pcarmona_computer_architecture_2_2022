from sre_parse import State


class Block:

    state="I"
    dir=bin(0)
    data=hex(0)

    def __init__(self, id) :
        self.id=id