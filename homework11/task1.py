class SimplifiedEnum(type):
    def __new__(mcs, cls, bases, classdict):
        simple_enum_cls = super().__new__(mcs, cls, bases, classdict)
        for key in classdict.keys():
            if cls + "__keys" in key:
                for item in classdict[key]:
                    setattr(simple_enum_cls, item, item)
        return simple_enum_cls


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
