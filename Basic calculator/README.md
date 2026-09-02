# Simple Calculator

A command-line calculator written in Python that supports basic arithmetic operations.

## Features

- Addition
- Division (with zero-division protection)
- Subtraction
- Multiplication
- Input validation (non-numeric input is handled gracefully)

## How to Run

```bash
python calculator.py
```

## Usage

When prompted, enter the letter corresponding to the operation you want:

| Key | Operation |
|-----|-----------|
| `A` | Add       |
| `D` | Divide    |
| `S` | Subtract  |
| `M` | Multiply  |
| `E` | Exit      |

Then enter two numbers when asked. The result will be displayed immediately.

## Example

```
What do you want to do:
1.Add: Write A
...
Chosen: A
Input a number: 10
Input another number: 5
Result: 15
```

## Error Handling

- **Non-numeric input** — prints a warning and returns to the menu without crashing.
- **Division by zero** — caught separately and prints a user-friendly message.
- **Unknown operation** — notifies the user that the input is not recognized.

