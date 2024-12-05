# app.py
# This is a test commit
def add(a, b):
    print("add func")
    return a + b

def test_add():
    print("test add func: case 1")
    assert add(1, 2) == 3
    print("test add func: case 2")
    assert add(1, -1) == 0

if __name__ == "__main__":
    test_add()
