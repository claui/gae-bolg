# Gae Bolg

## Setting up Gae Bolg

To set up Gae Bolg, you need three things:

1. The Python version manager `pyenv`.

2. A system-wide Python installation.

3. The Python dependency manager `poetry`.

### Installing pyenv

The Python version manager `pyenv` makes sure you can always keep
the exact Python version required by Gae Bolg,
regardless of your system Python.

#### Installing pyenv on Windows

While `pyenv` doesn’t support Windows, you can use a drop-in
replacement called `pyenv-win`.

To install `pyenv-win` on Windows, go to
[github.com/pyenv-win/pyenv-win](https://github.com/pyenv-win/pyenv-win#installation)
and follow one of the installation methods.

#### Installing pyenv on Linux

To install `pyenv` on Linux or WSL2, first make sure Python 3 is
installed. Then follow the *Basic GitHub Checkout* method described
at [github.com/pyenv/pyenv](https://github.com/pyenv/pyenv#basic-github-checkout).

#### Installing pyenv on macOS

To install `pyenv` on macOS, run:

```
brew install pyenv
```

#### Checking your system-wide pyenv installation

To verify your `pyenv` is working, run:

```
pyenv --version
```

### Checking your system-wide Python installation

Make sure you have Python 3.7 or higher installed on your system
and available in your PATH.

To check, run:

```
python --version
```

If that fails, try:

```
python3 --version
```

Proceed after you’ve confirmed one of those to work.

### Installing Poetry

You’ll need `poetry` to manage development dependencies and the venv.

To install Poetry on Windows, use one of the
[installation methods](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
described in Poetry’s documentation.

To install Poetry on macOS, run:

```
brew install poetry
```

If you’re on Linux or WSL2, use your system package manager to
install Poetry.

Alternatively, use one of the
[installation methods](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
described in Poetry’s documentation.

#### Checking your Poetry installation

To verify Poetry is working, run:

```
poetry --version
```

### Setting up your virtual environment

To set up your virtual environment, follow these steps:

1. Go to the project root directory.

2. Run `pyenv install -s`.

3. Run `pyenv exec pip install poetry`.

4. Run `pyenv exec poetry install`.

You need to do the above steps only once.

To update your dependencies after a `git pull`, run `poetry update`.

## Development scripts and tasks

To see a list of available tasks, run: `poetry run poe tasks`

## Running Gae Bolg

To execute Gae Bolg, run:

```
poetry run poe cli
```

## Contributing to Gae Bolg

### Running the tests

To execute the tests, run:

```
poetry run poe tests
```

To execute a single test, run e. g.:

```
poetry run poe tests -vv tests/test_api.py::test_hello
```

### Running the linter

To execute the linter, run:

```
poetry run poe linter
```

### Running the static type check

To execute the static type check, run:

```
poetry run poe typecheck
```

### Running the entire CI pipeline locally

If you have [act](https://github.com/nektos/act) installed, run:

```sh
act --container-options "-v act-toolcache:/opt/hostedtoolcache"
```

See also
issue [nektos/act#1987](https://github.com/nektos/act/issues/1987).

### Generating project documentation

To generate project documentation and open it in your browser, run:

```
poetry run poe doc
```

## Maintenance

### Refreshing dependencies

If you get errors after a Git pull, refresh your dependencies:

```
poetry update
```

### Rebuilding the virtual environment

If you’ve run `poetry update` and you still get errors, rebuild
the virtual environment:

```
poetry install
```

### Checking Gae Bolg’s dependencies for vulnerabilities

To check Gae Bolg’s dependencies for known vulnerabilities, run:

```
poetry run poe check
```

### Checking Gae Bolg’s dependencies for compatible updates

To check Gae Bolg’s dependencies for compatible updates, run:

```
poetry update --dry-run
```

## License

Copyright (c) 2023 Claudia Pellegrino

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
For a copy of the License, see [LICENSE](LICENSE).
