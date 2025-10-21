class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.current_step = 0
        self.webpages = [homepage]

        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.webpages = self.webpages[:self.current_step+1]
        self.current_step += 1
        self.webpages.append(url)

        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if steps > self.current_step:
            self.current_step = 0
            return self.webpages[self.current_step]
        else:
            self.current_step -= steps
            return self.webpages[self.current_step]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if (len(self.webpages) - 1 - self.current_step < steps):
                self.current_step = len(self.webpages) - 1 
                return self.webpages[self.current_step]
        else:
                self.current_step += steps
                return self.webpages[self.current_step]


        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)