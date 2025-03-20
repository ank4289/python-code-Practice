class father:
    def myrule(self):
        print("my rule is there for making money save and go")



class mother:
    def mysaving(self):
        print("my rule is to spend and save and enjoy life")


class son(father,mother):
    pass

s=son()
s.myrule()
s.mysaving()