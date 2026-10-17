# Caesar Cipher — Day 8

Work in progress from my **100 Days of Code: The Complete Python Pro Bootcamp** course. I have reached Caesar Cipher 2 and am still working on it.

Run the current program with Python 3:

```sh
python main.py
```

Enter `encode` or `decode`, a message containing lowercase letters, and an integer shift. The current loop asks for the direction again, then keeps reusing the same message and shift. Use Ctrl+C to stop it.

## Progress so far

- `exercises/functions_with_inputs.py`: a greeting function with three print statements; the function is not called yet.
- `exercises/positional_vs_keyword_arguments.py`: a name parameter and a positional function call. The multiple-input and keyword-argument exercises are still to do.
- `steps/01_encrypt.py`: my first encryption attempt, before alphabet wrapping.
- `main.py`: encryption with modulo wrapping, a backward-shifting decrypt function, an unfinished caesar wrapper, and a repeated direction prompt.

## Still working on

- Connect the program to `caesar()` and use its arguments instead of global variables.
- Wrap backward shifts too; large decode shifts can currently raise IndexError.
- Handle spaces, numbers, and symbols; they currently raise ValueError.
- Add a deliberate restart/exit choice.

Caesar Cipher 3 has not been included. Completed TODO instructions were changed to ordinary comments; unfinished TODOs remain. The existing program behavior is preserved.

## Commit history

This history was assembled from my saved exercise files after reaching this point. There were no earlier Day 8 snapshots in PyCharm's course history. The Cipher 2 changes are split into logical increments from the saved code, rather than claimed as original intermediate saves. Commits use their actual creation dates. Course solutions and IDE metadata are excluded.
