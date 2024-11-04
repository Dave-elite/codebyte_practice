# test_equivalent_keypresses.py

from equivalentkeypress import equivalentKeypresses  # Update this import based on your actual module name

def test_equivalent_keypresses():
    # Provided test cases
    assert equivalentKeypresses(["a,b,c,d", "a,b,c,d,-B,d"]) == "true"  # Final result should be the same
    assert equivalentKeypresses(["c,a,r,d", "c,a,-B,r,d"]) == "false"  # Different final result

    # # Additional test cases
    # assert equivalentKeypresses(["a,b,c", "a,b,c"]) == "true"  # No backspaces, same input
    # assert equivalentKeypresses(["a,b,c,-B", "a,b"]) == "true"  # One backspace removes 'c'
    # assert equivalentKeypresses(["a,b,-B,c", "a,c"]) == "true"  # Backspace removes 'b'
    # assert equivalentKeypresses(["x,y,z,-B", "x,y,-B,z"]) == "false"  # Different order with backspaces
    # assert equivalentKeypresses(["a,-B", ""]) == "true"  # Single backspace resulting in empty
    # assert equivalentKeypresses(["a,-B,b", "b"]) == "true"  # Backspace removes 'a', leaving 'b'
    # assert equivalentKeypresses(["-B", ""]) == "true"  # Both are empty after backspace
    # assert equivalentKeypresses(["a,b,c,-B,-B", "a,b"]) == "true"  # Multiple backspaces
    # assert equivalentKeypresses(["a,-B,b,c", "b,c"]) == "true"  # Backspace removes 'a'
    # assert equivalentKeypresses(["a,b,c", "a,b,c,-B,-B,-B"]) == "false"  # More backspaces than keys

    print("All test cases passed!")

if __name__ == "__main__":
    test_equivalent_keypresses()
