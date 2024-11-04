# Equivalent Keypresses

This Python script defines a function that checks if two sequences of keypresses are equivalent, taking into account the backspace operation represented by `-B`. The function processes two strings of comma-separated keypresses and returns whether they yield the same final output after applying backspaces.

## Functionality

The function `equivalentKeypresses(strArr)` accepts a list of two strings, where each string contains keypresses separated by commas. The function simulates the effect of a backspace (`-B`), which removes the last character from the current sequence.

### Key Features
- Parses two strings of keypresses.
- Handles backspace operations effectively.
- Compares the resulting sequences after processing all keypresses.
- Returns "true" if both sequences are equivalent, otherwise returns "false".

<!-- ## Example Usage

```python
print(equivalentKeypresses(["a,b,c,d", "a,b,c,d,-B,d"]))
print(equivalentKeypresses(["c,a,r,d", "c,a,-B,r,d"]))     -->

#   Third Greatest Word

This Python script defines a function that retrieves the third largest word from an array of strings, considering their lengths. If multiple words share the same length, the function prioritizes the last occurrence of those words in the original array.

## Functionality

The function `ThirdGreatest(strArr)` accepts a list of strings and sorts them based on their lengths to determine the third largest word.

### Key Features
- Sorts words by length in descending order.
- Handles cases where words have the same length by using their original index.
- Returns the third largest word from the array.

## Example Usage

<!-- ```python
print(ThirdGreatest(["hello", "world", "before", "all"]))  # Output: "world"
print(ThirdGreatest(["hello", "world", "after", "all"]))   # Output: "after" -->
