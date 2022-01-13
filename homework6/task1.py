def instances_counter(cls):
    class Wrapper:
        counter = 0

        def __init__(self, *args, **kwargs):
            cls.__init__(self, *args, **kwargs)
            Wrapper.counter += 1

        @staticmethod
        def get_created_instances():
            return Wrapper.counter

        def reset_instances_counter(self):
            num_of_instances = self.get_created_instances()
            Wrapper.counter = 0
            return num_of_instances

    return Wrapper


@instances_counter
class User:
    pass
