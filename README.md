# ML Group Project

![Static Badge](https://img.shields.io/badge/ML-2024_Full-Green) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/iRyougi/ML-Group-Project) ![GitHub License](https://img.shields.io/github/license/iRyougi/ML-Group-Project)

**其他语言版本: [English](README_en.md), [中文](README.md).**

Machine Learning 小组项目，旨在开发一款基于机器学习自动帮助编译器缩进 Python 的插件（VS Code 版本）

## Question - 我们解决了什么问题？

在 Python 编程中，语句的层次关系通常通过缩进来表示，而不像 C 或 Java 那样依赖于分号等明确的符号来区分行结束或语句之间的关系。这一特性虽然简洁明了，但对初学者和大型代码维护来说，却可能引发因缩进不当而导致的语法错误，尤其在代码逻辑复杂时更容易出错。

> [!NOTE]
>
> C 语言通常使用";"来表示层次关系

我们尝试利用机器学习技术来自动识别和纠正代码中的缩进错误。通过分析大量正确缩进与错误缩进的 Python 代码，模型可以学习到不同语句间的正确缩进规则与模式。当检测到潜在的缩进错误时，模型能够提示用户或自动修改，从而降低编码错误率，提高代码的可读性和可维护性。这一应用在提升编程效率和减少新手的学习曲线方面有着广泛的应用潜力。

## 现有解决方案
