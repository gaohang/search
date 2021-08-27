from utils import ESTwins
from config import hosts, auth

class SearchTwins(ESTwins):
    def __init__(self, index_pre, hosts=hosts, auth=auth):
        ESTwins.__init__(self, index_pre, hosts, auth)

if __name__ == "__main__":
    pass