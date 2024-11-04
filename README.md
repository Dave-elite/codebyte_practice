# Equivalent Keypresses

This Python script defines a function that checks if two sequences of keypresses are equivalent, taking into account the backspace operation represented by `-B`. The function processes two strings of comma-separated keypresses and returns whether they yield the same final output after applying backspaces.

## Functionality

The function `equivalentKeypresses(strArr)` accepts a list of two strings, where each string contains keypresses separated by commas. The function simulates the effect of a backspace (`-B`), which removes the last character from the current sequence.

### Key Features
- Parses two strings of keypresses.
- Handles backspace operations effectively.
- Compares the resulting sequences after processing all keypresses.
- Returns "true" if both sequences are equivalent, otherwise returns "false".

## Example Usage

```python
print(equivalentKeypresses(["a,b,c,d", "a,b,c,d,-B,d"]))  # Output: "true"
print(equivalentKeypresses(["c,a,r,d", "c,a,-B,r,d"]))    # Output: "false"
