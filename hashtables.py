class HashtTable:

    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0 
        for i in key:
            h += ord(i)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)

        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
    
    def display(self):
        for kv in list(enumerate(self.arr)):
            if kv[1] is not None:
                print(f"{kv[0]} : {kv[1]}")
            





t = HashtTable()


t['Bernard'] = 179
t['Elian'] = 195
t['Jetnor'] = 167
t['Fredi'] = 178
t['Enri'] = 182

print('hashtable after adding my friends height')
t.display()

del t['Elian']

print("hashtable after removing one")
t.display()

