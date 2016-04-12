class Josh:
    def __init__(self):
        print("in constructor")
        self.a = 5

    def inc(self):
        self.a += 1

    def get_class(self, j):
        print str(j.a);


josh = Josh()
alon = josh

josh.inc()

print (josh.a)
print (alon.a)
josh.inc()
josh(alon)