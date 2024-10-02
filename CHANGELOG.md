# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2024-10-02
### Added
- Added `MAX_ROWS` constant to the `Pyramid` class to prevent performance issues with large inputs.
- Modified the `__init__` method to raise a `ValueError` if the number of rows exceeds `MAX_ROWS`.
- Added tests to ensure that an exception is raised when the number of rows exceeds `MAX_ROWS`.
- Added ability to retrieve the number of blocks in any row of the pyramid.
- Added support for triangular and square pyramid shapes.

## [1.0.0] - 2024-09-15
### Added
- Initial release of the `Pyramid` class with support for triangular and square pyramids.
- Methods to calculate total blocks and blocks in a specific row.
