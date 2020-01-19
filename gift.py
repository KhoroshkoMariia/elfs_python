class Gift:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
    def __str__(self):
        return self.name + ";" + str(self.difficulty)