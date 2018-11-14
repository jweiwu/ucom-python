class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


rect1 = Rectangle(3, 5)
print "area for rect1=%d" % rect1.calculate_area()

rect2 = Rectangle(4, 6)
print "area for rect2=%d" % rect2.calculate_area()
