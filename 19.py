from custom_exception import FakeError

def raise_fake_error():
    """ Wondering how errors happen? Usually from code like line 6 below! """
    """ You can see how to build a customized error in the custom_exception.py file """
    raise FakeError()


raise_fake_error()