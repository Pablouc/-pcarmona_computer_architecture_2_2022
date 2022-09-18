from sre_parse import State


class Block:

    state="I"
    dir=bin(0)

    def __init__(self,block) -> None:
        self.block=block