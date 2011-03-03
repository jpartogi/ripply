import riak

class Connection(object):
    def __init__(self):
        self.client = riak.RiakClient()

    def client(self):
        return self.client