class iter_list:

    def __init__(self,lst) -> None:
        self.lst = [object for item in lst for object in item]


    def __iter__(self):
        self.count = -1
        return self


    def __next__(self):
        self.count+=1
        self.cur  = len(self.lst)
        if self.cur is self.count:
            raise StopIteration
        else:
            return self.lst[self.count]