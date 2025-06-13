# Python Functions Testing Project

A simple Python project demonstrating function implementation and comprehensive unit testing with exception handling.

## Files

- `fonctions.py` - Contains utility functions with type validation
- `test_fonctions.py` - Unit tests for all functions including exception tests

## Functions

- **additionner(a, b)** - Adds two numbers
- **est_pair(nombre)** - Checks if a number is even
- **valider_email(email)** - Validates email format (contains @ and .)
- **calculer_moyenne(notes)** - Calculates average of a list of grades
- **convertir_temperature(celsius)** - Converts Celsius to Fahrenheit
- **diviser(a, b)** - Divides two numbers (raises exception for division by zero)
- **valider_mot_de_passe(mot_de_passe)** - Validates password length (minimum 8 characters)

## Running Tests

```bash
python test_fonctions.py
```

or

```bash
python -m unittest test_fonctions.py -v
```

## Features

- Type validation with appropriate error messages
- Comprehensive test coverage (27 tests)
- Exception handling for invalid inputs
- Clear documentation and test descriptions