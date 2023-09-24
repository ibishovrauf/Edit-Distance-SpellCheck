# SpellCheck Developer Guide

Welcome to the SpellCheck developer guide. This guide is intended for developers who want to contribute to or utilize the `edit-distance` and `spellcheck` functions in the SpellCheck project.

## Table of Contents

- [SpellCheck Developer Guide](#spellcheck-developer-guide)
  - [Table of Contents](#table-of-contents)
  - [Contributing](#contributing)
  - [Using the `edit-distance` functions](#using-the-edit-distance-functions)
    - [Overview](#overview)
    - [Integration](#integration)
    - [Examples](#examples)
  - [Using the spellcheck Module](#using-the-spellcheck-module)
    - [Overview](#overview-1)
    - [Integration](#integration-1)
    - [Command-Line Usage](#command-line-usage)
    - [Examples](#examples-1)
    - [Testing](#testing)

## Contributing

We welcome contributions from the developer community to enhance the functionality and reliability of SpellCheck. Before contributing, please review our [Contributing Guidelines](CONTRIBUTING.md) and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

## Using the `edit-distance` functions

### Overview

The `edit-distance` functions provides various algorithms for calculating the edit distance (Levenshtein distance) between two strings. It is a core component of the SpellCheck project and is used in the spelling correction process.

### Integration

To use the `edit-distance` functions in your own Python project, you can import it as follows:

```python
from spellcheck import edit_distance, weighted_edit_distance, optimized_edit_distance
```
`edit_distance`: Calculates the standard edit distance between two strings.
`weighted_edit_distance`: Calculates the edit distance with custom weights for deletion, insertion, and substitution.
`optimized_edit_distance`: Calculates the optimized edit distance using dynamic programming.
### Examples
Here are some examples of how to use the edit-distance module:
```python
# Calculate the standard edit distance between two strings
distance1 = edit_distance("kitten", "sitting")

# Calculate the weighted edit distance with custom weights
distance2 = weighted_edit_distance("kitten", "sitting", deletion_weight=1, insertion_weight=1, substitution_weight=2)

# Calculate the optimized edit distance
distance3 = optimized_edit_distance("kitten", "sitting")
```

## Using the spellcheck Module

### Overview
The `spellcheck` module in SpellCheck utilizes the edit distance algorithms to perform spelling error detection and correction. This module offers a command-line interface and can be integrated into other projects as well.

### Integration
To use the `spellcheck` module in your Python project, you can import it as follows:
```python
from spellcheck import spell_checker
```
### Command-Line Usage
The spellcheck module can also be run from the command line. Here is an example of how to use it:

```bash
python spellcheck.py input_word --algorithm weighted --weights 0.5 0.3 0.2
```
Or
```
python spellcheck.py input_word --algorithm optimazed
```
### Examples
Here's an example of using the spell_checker function programmatically:
```python
from spellcheck import spell_checker

# Load data (e.g., from JSON)
data = load_data()

# Perform spellchecking
result = spell_checker("kitten", data, optimized=True)

print(f"Corrected   word: {result['to']}\
                    probability: {result['probability']}\
                    cost: {result['cost']}")
```

### Testing
We maintain a suite of tests to ensure the correctness and reliability of the edit-distance and spellcheck modules. Developers are encouraged to write additional tests when contributing new features or making changes.

To run the tests, use the following command:

```bash
python -m unittest discover tests/
```