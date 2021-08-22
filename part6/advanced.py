from __future__ import print_function    # 2.X compatibility

# Rozszerzanie typów za pomocą osadzania

# Ten przykład rozszerza klasę wbudowanej listy

class Set:
   def __init__(self, value = []):    # Constructor
       self.data = []                 # Manages a list
       self.concat(value)

   def intersect(self, other):        # other is any sequence
       res = []                       # self is the subject
       for x in self.data:
           if x in other:             # Pick common items
               res.append(x)
       return Set(res)                # Return a new Set

   def union(self, other):            # other is any sequence
       res = self.data[:]             # Copy of my list
       for x in other:                # Add items in other
           if not x in res:
               res.append(x)
       return Set(res)

   def concat(self, value):           # value: list, Set...
       for x in value:                # Removes duplicates
          if not x in self.data:
               self.data.append(x)

   def __len__(self):          return len(self.data)            # len(self), if self
   def __getitem__(self, key): return self.data[key]            # self[i], self[i:j]
   def __and__(self, other):   return self.intersect(other)     # self & other
   def __or__(self, other):    return self.union(other)         # self | other
   def __repr__(self):         return 'Set:' + repr(self.data)  # print(self),...
   def __iter__(self):         return iter(self.data)           # for x in self,...ta)

x = Set([1, 3, 5, 7])
print(x.union(Set([1, 4, 7])))
print(x | Set([1, 4, 6]))

# Rozszerzanie typów za pomocą klas podrzędnych
# Można wbdowane typy rozszerzać również przez dziedziczenie

class Set(list):
    def __init__(self, value = []):      # Constructor
        list.__init__([])                # Customizes list
        self.concat(value)               # Copies mutable defaults

    def intersect(self, other):          # other is any sequence
        res = []                         # self is the subject
        for x in self:
            if x in other:               # Pick common items
                res.append(x)
        return Set(res)                  # Return a new Set

    def union(self, other):              # other is any sequence
        res = Set(self)                  # Copy me and my list
        res.concat(other)
        return res

    def concat(self, value):             # value: list, Set, etc.
        for x in value:                  # Removes duplicates
            if not x in self:
                self.append(x)

    def __and__(self, other): return self.intersect(other)
    def __or__(self, other):  return self.union(other)
    def __repr__(self):       return 'Set:' + list.__repr__(self)

if __name__ == '__main__':
    x = Set([1,3,5,7])
    y = Set([2,1,4,5,6])
    print(x, y, len(x))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    x.reverse(); print(x)

# Klasy w nowym stylu

# 1011