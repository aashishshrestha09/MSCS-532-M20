# Assignment 2: Analyzing and Implementing Divide-and-Conquer Algorithms

## Overview

This project implements and benchmarks two classic divide-and-conquer algorithms:

- **Merge Sort**
- **Quick Sort**

Both algorithms are implemented in Python and tested against various datasets (sorted, reverse sorted, and random).

## Installation

### Pre-requisites

- Install [`python`](https://www.python.org/downloads/).
- Install [`pip`](https://pip.pypa.io/en/stable/installation/).

## Development

### Setup

1. Clone this repository

   ```bash
    git clone https://github.com/aashishshrestha09/MSCS-532-M20.git
    cd MSCS-532-M20/weeks-3-4/assignment-2
   ```

2. Create virtual environment for this project: `python3 -m venv .venv`.
3. Activate the virtual environment: `. .venv/bin/activate`.
4. Install as editable with "dev" packages: `pip install --editable ".[dev]"`.

### Run program

```sh
python main.py
```

## Project Structure

```
.
├── img
│   ├── sorting_performance_random.png
│   ├── sorting_performance_reverse.png
│   └── sorting_performance_sorted.png
├── main.py
├── pyproject.toml
├── README.md
├── sorting_algorithms
│   ├── __init__.py
│   ├── merge_sort_algorithm.py
│   └── quick_sort_algorithm.py
└── utils
    ├── __init__.py
    ├── dataset_utils.py
    ├── metrics_utils.py
    └── plot_utils.py
```
