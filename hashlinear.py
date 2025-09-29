class HashLinear:
    def __init__(self, M):
        self.M = M              # table size
        self.T = [None] * M     # init table

    def hash(self, data):
        sum = 0  # hashing function from instructions
        N = len(data) 
        for i in range(N):
            sum += ord(data[i])
        return sum % self.M

    def insert(self, data):  
        i = self.hash(data) # find correct index
        start = i # save start for checking when whole lists has been looped through in probing
        if self.T[i] == None or self.T[i] == "T": # we can insert if slot is empty or there is tombstone
            self.T[i] = data
        elif self.T[i] == data:
            return
        else: 
            while True:
                i += 1
                if i == self.M:
                    i = 0
                if self.T[i] == None or self.T[i] == "T": # we can insert if slot is empty or there is tombstone
                    self.T[i] = data
                    return
                if i == start:
                    return


    def delete(self, data):
        i = self.hash(data)
        start = i 
        if self.T[i] == data:
            self.T[i] = "T" #tombstone
        else: 
            while True:
                i += 1
                if i == self.M:
                    i = 0
                if self.T[i] == data: # we can insert if slot is empty or there is tombstone
                    self.T[i] = "T"
                    return
                if i == start:
                    return
    

    def print(self): # basic for loop to print everything
        for x in self.T:
            if x == None:
                print("F ", end="")
            else:
                print(x, end=" ")
        print("\n")

if __name__ == "__main__":
    table = HashLinear(8)
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
