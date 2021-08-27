from utils import ESIndex
from config import hosts, auth

class SearchIndex(ESIndex):
    def __init__(self, index: str, hosts=hosts, auth=auth):
        ESIndex.__init__(self, index, hosts, auth)

if __name__ == "__main__":
    pass