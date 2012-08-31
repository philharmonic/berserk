class Structure(object):
    data = "abcd"
    def __init__(self, l):
        self.reserved = l*self.data

def memory():
    s = Structure(10000)
def cpu():
    a = 0.8*2.3

if __name__ == "__main__":
    while True:
        memory()
        cpu()
    
