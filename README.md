# GENDIFF
### A command-line utility for comparing configuration files.

[![Actions Status](https://github.com/reisenen/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/reisenen/python-project-50/actions)
[![Python CI](https://github.com/reisenen/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/reisenen/python-project-50/actions/workflows/pyci.yml)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=reisenen_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=reisenen_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=reisenen_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=reisenen_python-project-50)

## Description

**gendiff** is a command-line utility that compares two configuration files and displays the differences between them.

The utility supports:

- JSON and YAML input formats
- Recursive comparison of nested structures
- Multiple output formats:
  - `stylish` (default)
  - `plain`
  - `json`

The comparison is performed by building an internal Abstract Syntax Tree (AST), which is then rendered by the selected formatter.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/reisenen/python-project-50.git
cd python-project-50
```

Create a virtual environment and install dependencies:

```bash
make install
```

Run the utility:

```bash
gendiff file1.json file2.json
```

or

```bash
uv run gendiff file1.json file2.json
```

---

## Usage

```text
gendiff [-h] [-f FORMAT] first_file second_file
```

### Arguments

| Argument | Description |
|----------|-------------|
| `first_file` | Path to the first configuration file |
| `second_file` | Path to the second configuration file |

### Options

| Option | Description |
|--------|-------------|
| `-f`, `--format` | Output format (`stylish`, `plain`, `json`) |
| `-h`, `--help` | Show help message |

---

# Examples

## Stylish format (JSON)

Compares two JSON configuration files using the default `stylish` formatter.

[![asciicast](https://asciinema.org/a/UTXBcsfkQ9KQYPph.svg)](https://asciinema.org/a/UTXBcsfkQ9KQYPph)

---

## Stylish format (YAML)

Compares two YAML configuration files.

[![asciicast](https://asciinema.org/a/PyaLALvgoAL3sFUr.svg)](https://asciinema.org/a/PyaLALvgoAL3sFUr)

---

## Recursive comparison

Demonstrates comparison of deeply nested configuration structures.

[![asciicast](https://asciinema.org/a/pDgpzGhgmbuE1C1D.svg)](https://asciinema.org/a/pDgpzGhgmbuE1C1D)

---

## Plain format

Shows differences as human-readable property updates.

```bash
gendiff -f plain file1.yml file2.yml
```

[![asciicast](https://asciinema.org/a/wotvQT5GsFQHarJG.svg)](https://asciinema.org/a/wotvQT5GsFQHarJG)

---

## JSON format

Outputs the generated difference tree as JSON.

```bash
gendiff -f json file1.yml file2.yml
```

[![asciicast](https://asciinema.org/a/gb5GhW4nUJlIO14X.svg)](https://asciinema.org/a/gb5GhW4nUJlIO14X)