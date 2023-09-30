# SpellCheck 
SpellCheck is an advanced Python-based spellcheck tool designed to improve the accuracy of written content by detecting and correcting spelling errors in text documents. It offers a range of spellcheck algorithms, including optimized edit distance, weighted edit distance, and traditional edit distance, to cater to various text correction needs.

## Purpose
The primary purpose of SpellCheck is to provide users with a versatile and reliable solution for enhancing the quality of written content. Whether you're a writer, student, or developer, SpellCheck helps you:

- **Correct Spelling Errors**: SpellCheck identifies and corrects spelling mistakes in text, ensuring that your documents are free from embarrassing errors.

- **Customize Algorithms**: Choose from different spellcheck algorithms based on your specific requirements. Optimize the spellcheck process with custom weights or rely on traditional edit distance calculations.

- **Boost Writing Efficiency**: By automating the spellchecking process, SpellCheck saves you time and effort, allowing you to focus on creating error-free content.

- **Integrate with Ease**: Developers can easily integrate SpellCheck into their Python projects, leveraging its powerful spellcheck capabilities.

- **Tailor to Your Needs**: Fine-tune the spellcheck tool to suit your particular use case, whether you need precise corrections or a faster spellcheck process.

SpellCheck aims to be    your go-to solution for enhancing the correctness and professionalism of your written materials, ultimately improving communication and comprehension.

## Table of Contents

- [SpellCheck](#spellcheck)
  - [Purpose](#purpose)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)

## Installation

To get started with the project, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/project-name.git`
2. Navigate to the project directory: `cd project-name`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

To use SpellCheck, you can run it from the command line as follows:



```bash
python spellcheck.py <input> --algorithm [optimized, weighted, normal] --weights
```

`--input`: Specify the path to your input text file.

`--algorithm`: Choose the spellcheck algorithm to use. You can select one of the following options: "optimized," "weighted," or "normal." Each algorithm offers different methods for detecting and correcting spelling errors.

`--weights` (Optional): When using the "weighted" algorithm, you can provide custom weights to adjust the cost of deletion, insertion, and substitution. Weights represent the relative importance of these operations in the spellcheck process. For example, `--weights 0.5 0.3 0.2` would assign a weight of 0.5 to deletion, 0.3 to insertion, and 0.2 to substitution. Customizing weights allows you to fine-tune the spellcheck algorithm to your specific requirements.