# SpellCheck User Guide

SpellCheck is a Python-based spellcheck tool that provides various algorithms for detecting and correcting spelling errors in text documents.

## Table of Contents

- [SpellCheck User Guide](#spellcheck-user-guide)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)

## Installation

To get started with SpellCheck, follow these steps:

1. Clone the repository: `git clone https://github.com/ibisovrauf/Edit-Distance-SpellCheck.git`
2. Navigate to the project directory: `cd Edit-Distance-SpellCheck`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

To use SpellCheck, you can run it from the command line as follows:

```bash
python spellcheck.py <input> --algorithm [optimized, weighted, normal] --weights
```

`--input`: Specify the path to your input text file.

`--algorithm`: Choose the spellcheck algorithm to use. You can select one of the following options: "optimized," "weighted," or "normal." Each algorithm offers different methods for detecting and correcting spelling errors.

`--weights` (Optional): When using the "weighted" algorithm, you can provide custom weights to adjust the cost of deletion, insertion, and substitution. Weights represent the relative importance of these operations in the spellcheck process. For example, `--weights 0.5 0.3 0.2` would assign a weight of 0.5 to deletion, 0.3 to insertion, and 0.2 to substitution. Customizing weights allows you to fine-tune the spellcheck algorithm to your specific requirements.