class Pets:
    def __init__(self, pets):
        self.pets = pets

    def get_pets_by_count(self):
        count = {}
        for _, name in self.pets:
            if name in count:
                count[name] += 1
            else:
                count[name] = 1
        return count
