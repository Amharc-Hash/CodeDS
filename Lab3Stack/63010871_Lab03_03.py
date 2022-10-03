class Stack:
    def __init__(self, list=None):
        self.string = ''
        if list == None: self.items = []
        else: self.items = list

    def push(self, i): return self.items.append(i)

    def isEmpty(self): return self.items == []

    def pop(self):
        if not self.isEmpty(): return self.items.pop()

    def size(self): return len(self.items)

    def peek(self): 
        if not self.isEmpty(): return self.items[-1]
    
    def empty(self): return self.items.clear()

    def __str__(self):
        return self.string.join(self.items)

    def copy(self, other):
        self.items = other.items.copy()
        self.items.reverse()



inp = input('Enter Input : ').split()
sk_inp = Stack(inp)
st_cal = Stack()
st_score = Stack()
combo = 0
ready = False

while True:
    firstSize = sk_inp.size()
    for i in range(sk_inp.size()):
        if i == 0:  # FIRST PUSH
            st_cal.push(sk_inp.pop())
        else:
            if not st_cal.isEmpty() and not sk_inp.isEmpty():  # CHECK IF NOT EMPTY
                if st_cal.peek() != sk_inp.peek():    # CHECK IF SAME OR NOT
                    if not ready: st_cal.push(sk_inp.pop())     # FIRST ONE INTO CAL
                    else:
                        st_cal.push(st_score.pop())   # PUSH SCORE "BACK" TO CAL
                        st_cal.push(sk_inp.pop())     # PUSH INP TO CAL
                        ready = False                 # SET READY = FALSE
                else:
                    if not ready:                     # SECOND ONE
                        st_score.push(sk_inp.pop())   # PUSH INP TO SCORE
                        ready = True
                    else:
                        st_cal.pop()                  # SCORE 3 STRIKE
                        sk_inp.pop()
                        st_score.pop()
                        combo += 1
                        ready = False
    else:
        if firstSize == st_cal.size():                # LAST
            print(st_cal.size())
            if st_cal.isEmpty():
                print('Empty')
            else:
                print(st_cal)
            if combo > 1:
                print('Combo :', combo, '! ! !')
            break

        sk_inp.copy(st_cal)                          # EVERY LOOP HAS TO DO
        st_cal.empty()                               # EMPTY CAL