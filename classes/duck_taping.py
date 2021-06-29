class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDown List")


def draw(controls):
    for control in controls:  # python check igf it iterable
        control.draw()  # python check if object have a draw() method
        #  to get polymorphs without abstract method


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])
