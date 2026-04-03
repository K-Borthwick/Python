import basics.hello_world as hw

def test_hello_world_msg():
    MESSAGE = hw.hello_world('Kyle')
    assert MESSAGE == 'Hello World! Your name is Kyle'
    