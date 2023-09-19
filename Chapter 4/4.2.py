class NewInt(int):
    def repeat(self, k=2):
        return int(str(self)*k)

    def to_bin(self):
        return int("{0:#b}".format(self)[2:])


