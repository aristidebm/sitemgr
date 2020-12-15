class TakenTagError(Exception):
    def __init__(self, msg="This tag is already taken. Please choose another."):
        self.message = msg

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class TagNotFoundError(Exception):
    def __init__(self, msg="Can't find the specified tag"):
        self.message = msg

    def __repr__(self):
        return f"{self.__class__.__name__}()"
