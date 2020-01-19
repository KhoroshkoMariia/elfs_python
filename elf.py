class Elf:
    def __init__(self, id, name, level):
        self.id = id
        self.name = name
        self.level = level
    def __str__(self):
        return self.id + ";" + self.name + ";" + str(self.level)