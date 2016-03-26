# Contributing

The project follows the [Open Knowledge International coding standards](https://github.com/okfn/coding-standards).

## Getting Started

Recommended way to get started is to create and activate a project virtual environment.
To install package and development dependencies into active environment:

```
$ make develop-<git|pypi>
```

There are 2 options:
- use `git` suffix to install packages from GitHub
- use `pypi` suffix to install packages from PyPi

## Testing

To run tests:

```
$ make test
```

Under hood the `behave` BDD framework is used.
To run it manually use:

```
behave <path>
```
