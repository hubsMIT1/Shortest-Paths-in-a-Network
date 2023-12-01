class Edge:
    def __init__(self, tail, head, transmit_time):
        self.tail = tail
        self.head = head
        self.transmit_time = transmit_time
        self.is_up = True