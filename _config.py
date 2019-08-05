
class NNConfig:
    def __init__(self):
        self.batch_size = 64
        self.epochs = 500

    def set_param(self, key, new_value):
        if key in self.__dict__:
            self.__dict__[key] = new_value

    def show(self):
        for key in self.__dict__:
            print(str(key), "=", self.__dict__[key])