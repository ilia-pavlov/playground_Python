class Text(str):
    def duplication(self):  # add a new methods to existing "str" base class
        return self + self

    def jumping_around(self):
        return self + " we jump!"


text = Text('Python')
print(text.duplication())
print(text.jumping_around())


class TrackableList(list):
    def append(self, object):
        print("Append called")  # overriding existing class
        super().append(object)


list = TrackableList()
list.append("1")
