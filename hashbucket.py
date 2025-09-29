class HashBucket:
    def __init__(self, M, B):
        self.M = M # table size 
        self.T = [None] * M # init table
        self.B = B # bucket amount
        self.B_S = M // B # bucket size 
        self.OF = [] # overflow list

    def hash(self, data):
        sum = 0
        N = len(data)
        for i in range(N):
            sum += ord(data[i])
        return sum % self.M

    def insert(self, data):
        i = self.hash(data)
        bucket = i % self.B # get the position in bucket that we first try to fill 
        start = bucket * self.B_S # get starting index of bucket 
        end = start + self.B_S # get end index of bucket 
        for j in range(start, end): # loop from start to end in bucket
            if self.T[j] == data: 
                return
        for j in range(start, end):
            if self.T[j] is None or self.T[j] == "T": # if empty or T then insert 
                self.T[j] = data
                return
        if data in self.OF: # if data already in overflow, dont append 
            return
        else:
            self.OF.append(data)

    def delete(self, data):
        i = self.hash(data)
        bucket = i % self.B # get the position in bucket that we first try to fill 
        start = bucket * self.B_S  # same logic as in inserting
        end = start + self.B_S
        for j in range(start, end):
            if self.T[j] == data:
                self.T[j] = "T" # change to tombstone if element gound
                return
            if self.T[j] is None: # if index is none then go to next 
                continue
            for i in self.OF: # loop through self OF if data found from there remove it 
                if i == data:
                    self.OF.remove(data)


    def print(self):
        for x in self.T:
            if x is None:
                print("F ", end="")
            else:
                print(x, end=" ")
        for x in self.OF:
            print(x, end=" ")
        print("\n")



if __name__ == "__main__":
    table = HashBucket(8, 4)
    table.print()
    table.insert("apple")
    table.insert("orange")
    table.insert("banana")
    table.insert("grapes")
    table.insert("mango")
    table.insert("peach")
    table.insert("apple")
    table.print()

    table.delete("banana")
    table.delete("kiwi")
    table.delete("peach")
    table.print()