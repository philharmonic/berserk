def log(something):
    print(something)


# MEMORY
#---------------------
# import sys

# class Structure(object):
#     data = "abcd"
#     def __init__(self, l):
#         self.reserved = l*self.data

# def memory(size = 1):
#     """
#     @param size: MBs to allocate
#     """
#     # allocate
#     data = range(10000)
#     size = sys.getsizeof(data)
#     log("allocated %d bytes" % (size))
#     # read / write
#---------------------

def cpu():
    a = 0.8*2.3

def run_from_conf(conf):
    #memory(size=conf.size)
    import memory
    memory.run(10**3)

def sample_run():
    while True:
        memory()
        cpu()

if __name__ == "__main__":
    #sample_run()
    import conf
    run_from_conf(conf)
