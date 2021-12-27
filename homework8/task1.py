class KeyValueStorage:
    def __init__(self, path):
        with open(path) as file:
            for line in file:
                key, value = line.rstrip().split("=")
                if not key.isidentifier():
                    raise ValueError
                try:
                    value = int(value)
                except ValueError:
                    pass
                setattr(self, key, value)

    def __getitem__(self, key):
        return self.__dict__[key]
