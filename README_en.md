# ML Group Project

![Static Badge](https://img.shields.io/badge/ML-2024_Full-Green) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/iRyougi/ML-Group-Project) ![GitHub License](https://img.shields.io/github/license/iRyougi/ML-Group-Project)

**Read this in other languages: [English](README_en.md), [中文](README.md).**

## Question - What are we trying to solve?

In Python, the separation of statements is usually expressed through indentation, unlike in C or Java that relies on explicit charaters such as semicolons to distinguish the end of a line or the relationship between statements. Although this feature is easy to understand, syntax errors caused by improper indentation can be a major problem for both new and old programmers alike, whether it is starting on a new project or maintaining large-scale code, especially when these errors are hidden within complex code.

> [!NOTE]
>
> C language usually use ";" to define the relationships between statements

We attempt to leverage machine learning techniques to automatically identify and correct indentation errors in Python code. By analyzing a large number of correctly indented and incorrectly indented Python codes, the model can learn the correct indentation rules and the relationships between different statements. In practice, when potential indentation errors are detected, the model can prompt the user or correct automatically, thereby reducing the chances of error and improving the readability and maintainability of the code. This application has broad application potential in improving programming efficiency and reducing the learning curve for novices.

## Existing solutions

### Automatic parsing

**IS-CFG Indentation Sensitive Context-Free Grammar** is a method that specifically handles Python's indentation issues. It formalizes Python's indentation through some grammatical rules, and develops a parser to ensure that the indentation of the code meets the standard. To put it simply, IS-CFG will use NEWLINE to separate statements, INDENT and DEDENT to indicate the increase and decrease of indentation spaces, and symbols such as =, >, and ≥ to define indentation relationships.

The **advantage** of IS-CFG is that it expresses Python's indentation rules very accurately, which can avoid ambiguities caused by indentation in the code. Efficient parsers can be built on IS-CFG to automatically check and parse the code to ensure that the indentation of the code complies with the specification. In addition, consistent indentation improves the readability and maintainability of code and avoids syntax errors caused by indentation. IS-CFG is also suitable for developing code formatting tools tailored towards specification requirements to automatically adjust the indentation of the code with one click. 

However, IS-CFG also has some **disadvantages**. It has a high learning curve, understanding and mastering these rules requires solid theoretical foundation, which is difficult for beginners. In addition, developing a parser or code formatting tool based on IS-CFG requires a certain amount of technical investment, meaning the development cost is not low.

------

### Visual inspection

**Stereo Vision Algorithm** is another method that helps find indentation problems by importing Python code into a spreadsheet and displaying the indentation levels in different visual ways. Specifically, the alogorithm first converts the code into a spreadsheet format. Each line of code corresponds to a row in the spreadsheet. The **number of leading spaces** (the number of consecutive spaces at the beginning of a line of code or text) of the line of code is displayed in the cell. Next, the indentation level is displayed in two ways: "left eye view" and "right eye view". In the "left eye view", the program converts the number of spaces into indentation levels: the number of indentation blocks is equal to the number of spaces before the current line of code divided by the default number of indentation spaces (for example, 8 spaces is one level of indentation). Another indent block is added if there is a remainder. In the "right eye view", the number of indented blocks is directly equal to the number of spaces before the code line divided by the default number of indented spaces, without adding a remainder, making the display more intuitive. If the number of indented blocks on the same line in the left and right views is different, it may suggest an indentation error and programmers can quickly facilitate subsequent adjustments.

```python
# main block（no indentation）
def example_function():
    # One level of indentation indicates that this code belongs to the example_function function
    if condition:
        # Second level indentation indicates that this code belongs to the if statement block
        do_something()
```

The **advantage** of this method is its intuitiveness. Indentation errors is clear at a glance in the spreadsheet, and the comparison of the two views indicates the error location clearly, and the function of automatically correcting small indentation errors can save time.

However, its **disadvantage** is that you need to manually export the code to a spreadsheet, which may not be convenient for large projects or frequently edited code. In addition, it can only correct small-scale indentation errors, and manual adjustments are still required for longer pieces of code.

## How to achieve our goals?

### Crawlers and data sets

To achieve the goal of automatically correcting indentation errors in Python code, we adopted a systematic data collection and processing method. First, we used a web crawler to search for a large number of correct code examples from multiple Python quiz websites to build a prototype of our data set. Then, after manual screening, we separated and deleted the code files that were only applicable to Python 2.0 because these codes did not meet our training needs. For the remaining code files, some were manully editted to introduce indentation errors. This resulted in a data set with both correctly and incorrectly indented code samples.

Finally, we obtained a complete data set containing "correct code files", "code files with indentation errors", and "correct output". This approach provides machine learning models with targeted training material, allowing the models to effectively learn how to identify and correct indentation errors in code.

> [!NOTE]
>
> During the data crawling process, we encountered some challenges. First of all, some codes are only applicable to Python 2.0. These codes contain syntax that is incompatible with Python 3.x and do not meet our training needs. Secondly, some of the crawled files contained CSS files that were mistakenly marked as `.py` files, causing the contents of these files to be rendered incorrectly.
>
> We used manual elimination to solve the challenges. Through manual screening, we excluded Python 2.0-specific code and incorrectly tagged CSS files. In addition, we increased the amount of data crawled to ensure that after deleting files that did not meet the requirements, the data set was still large enough to support training the model. This approach helped us build a high-quality code dataset suitable for Python 3.x, thereby improving training results and model accuracy.

### Standards for the dataset

#### structure

- Dataset
  - exercise_1 -- folder
    - exercise_1.py -- correct code file（reference）
    - exercise_1_e.py -- code file with indentation errors
    - result_1.json -- correct output
  - exercise_2 -- folder
  - exercise_3 -- folder
  - ......

**Training set：at least 100 files**

#### Standard for the document



## Result analysis

## future work
