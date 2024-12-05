def add(a, b):
    print("add func")  # This print will be hidden by pytest
    return a + b

def test_add(capsys):  # Add capsys fixture to capture output
    print("test add func: case 1")
    assert add(1, 2) == 3
    print("test add func: case 2")
    assert add(1, -1) == 1
    
    # Capture and check the output if you need to verify the prints
    captured = capsys.readouterr()
    assert "test add func: case 1" in captured.out
    assert "test add func: case 2" in captured.out
