class point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def slope(self,x,y):
        m = (y - self.y) / (x - self.x)
        return m