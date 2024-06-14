class HashtTable:

    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0 
        for i in key:
            h += ord(i)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx , el in enumerate(self.arr[h]):
            if len(el) == 2 and el[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self, key):
        h = self.get_hash(key)

        for el in self.arr[h]:
            if el[0] == key:
                return el[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, el in enumerate(self.arr[h]):
            if el[0] == key:
                del self.arr[h][index]
    




t = HashtTable()


t['Bernard'] = 179
t['Elian'] = 195
t['Jetnor'] = 167
t['Fredi'] = 178
t['Enri'] = 182
t['March 6'] = 10
t['March 17'] = 30


print('hashtable after adding my friends height')
print(t.arr)
del t['March 17']

print("hashtable after removing one")
print(t.arr)

print('value at march 6: ',t['March 6'])

