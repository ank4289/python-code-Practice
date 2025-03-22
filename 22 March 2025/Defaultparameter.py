

class Browser:

    def __init__(self,brow):
        self.brow=brow


    def browser(self, brow="chrome"):
        print("The browser is "+ self.brow)


web=Browser("firefox")
web.browser()