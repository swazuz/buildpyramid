# Building Pyramids with Python
A demonstration of test driven development (TDD) in Python by building pyramids.

## Introduction

Pyramids have fascinated humanity for millennia, standing as monumental testaments to the ingenuity and architectural prowess of ancient civilizations. The most iconic pyramids are those of ancient Egypt, built as grand funerary edifices for pharaohs and their consorts. These structures, constructed over a span of 2,700 years, from the Old Kingdom to the Ptolemaic period, continue to captivate our imagination.

While the Egyptian pyramids are renowned for their four-sided design, pyramids can also have three sides. A three-sided pyramid, known as a tetrahedron, consists of four triangular faces, whereas the more familiar four-sided pyramid, or square pyramid, has a square base and four triangular faces.

In this project, we delve into the world of virtual pyramids, exploring their geometric properties and constructing them programmatically using Python. Whether you're building a three-sided or four-sided pyramid, the principles of geometry and the allure of these ancient structures remain timeless.

Additionally, this project is set up to demonstrate the principles of **Test-Driven Design (TDD)**. By writing tests before implementing the functionality, we ensure that our code is robust, reliable, and maintainable. This approach not only helps in catching bugs early but also guides the development process, leading to cleaner and more efficient code.

## Initial Functions and Limited Design

This program currently supports two primary functions, demonstrating a limited yet foundational design. These functions are:

1. **Calculate Blocks**:
   - This function calculates the total number of blocks required to build a pyramid of a given height. The calculation is based on the sum of squares of the height levels. For example, a pyramid with a height of 3 will require \(1^2 + 2^2 + 3^2 = 14\) blocks.

2. **Create Worker**:
   - This function creates a worker with a specified name and role. The worker can have roles such as "builder" or "architect". If an invalid role is provided, the function will return `None`.

These functions serve as the building blocks for more complex features and demonstrate the principles of Test-Driven Design (TDD) by ensuring that each function is thoroughly tested before implementation.

## Contributing

We welcome contributions to this project! If you have an idea for a new feature or an improvement, please follow these steps:

1. **Fork the Project**:
   - Fork the repository to your own GitHub account by clicking the "Fork" button at the top right of the repository page.

2. **Clone the Forked Repository**:
   - Clone the forked repository to your local machine:
     ```bash
     git clone https://github.com/your-username/your-repo-name.git
     ```

3. **Create a New Branch**:
   - Create a new branch for your feature or bug fix:
     ```bash
     git checkout -b feature/your-feature-name
     ```

4. **Suggest a Feature**:
   - Open an issue on our GitHub repository to suggest your feature. Provide a clear and detailed description of the feature and its benefits.

5. **Write Tests**:
   - Before implementing the feature, write tests to demonstrate that your feature works as expected. This aligns with our Test-Driven Design (TDD) approach.

6. **Implement the Feature**:
   - Write the code to implement your feature. Ensure that all tests pass before submitting your contribution.

7. **Update Documentation**:
   - Update the README file and any other relevant documentation to include information about your new feature. Make sure to provide clear instructions on how to use it.

8. **Add Your Name to the List of Contributors**:
   - Add your name to the list of contributors in the CONTRIBUTORS.md file. We appreciate your contributions and want to give you credit for your work!

9. **Commit Your Changes**:
   - Commit your changes with a meaningful commit message:
     ```bash
     git commit -m "Add feature: your-feature-name"
     ```

10. **Push to Your Fork**:
    - Push your changes to your forked repository:
      ```bash
      git push origin feature/your-feature-name
      ```

11. **Create a Pull Request**:
    - Open a pull request from your forked repository to the original repository. Provide a clear description of your changes and link to the issue you opened.

### Guidelines

- **Code Quality**: Ensure your code follows the project's coding standards and best practices.
- **Testing**: Write comprehensive tests for your feature. Make sure all existing and new tests pass.
- **Documentation**: Update the documentation to reflect your changes. Provide clear and concise instructions.
- **Commit Messages**: Write meaningful commit messages that describe your changes.

Thank you for contributing to our project! Your efforts help make this project better for everyone.
