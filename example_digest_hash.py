import datetime
import hashlib

class ExampleHash:
    
    def __init__(self):
        self.hashFunction = hashlib.new('sha256')

    def compHash(self, data):
        myBytes = data.encode()
        self.hashFunction.update(myBytes)
        print(self.hashFunction.hexdigest())
    
