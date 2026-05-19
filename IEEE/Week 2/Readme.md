# 🧪 Data Lab System

A mini object-oriented data analysis system built with **pure Python** — no external libraries.  
Simulates a small internal tool for a Data Science team to manage, filter, merge, and compare datasets.

---

## 📁 Project Structure

```
data_lab.py        # All classes and example usage
README.md          # Project documentation
```

---

## 🏗️ Class Overview

```
Data Lab System
│
├── Dataset                        ← Base class
│   ├── Attributes
│   │   ├── name
│   │   ├── data
│   │   ├── rows
│   │   └── columns
│   │
│   ├── Methods
│   │   ├── summary()
│   │   ├── get_column(col)
│   │   ├── average(col)
│   │   ├── filter(col, op, val)   ← returns new Dataset
│   │   ├── merge(other)           ← returns new Dataset
│   │   ├── __len__()
│   │   └── __str__()
│   │
│   └── NumericDataset             ← Inherits from Dataset
│       ├── summary()              ← Overrides parent + adds averages
│       └── highest(col)          ← Returns row with max value
│
└── DataLab                        ← Manages multiple datasets
    ├── Attributes
    │   └── datasets               ← list of Dataset objects
    │
    └── Methods
        ├── add_dataset(ds)
        ├── list_datasets()
        └── compare_averages(col)
```

---

### `Dataset`
The base class. Stores data as a list of dictionaries and provides core analysis methods.

| Method | Description |
|---|---|
| `summary()` | Prints dataset name, row count, columns, and a sample row |
| `get_column(col)` | Returns all values in a given column |
| `average(col)` | Returns the average of a numeric column |
| `filter(col, op, val)` | Returns a **new** filtered Dataset (`>`, `<`, `==`) |
| `merge(other)` | Returns a **new** Dataset combining two datasets |
| `__len__()` | Enables `len(dataset)` |
| `__str__()` | Enables `print(dataset)` with a readable output |

---

### `NumericDataset` *(inherits Dataset)*
Extends `Dataset` with numeric-focused features.

| Method | Description |
|---|---|
| `summary()` | Calls parent summary + prints averages for all numeric columns |
| `highest(col)` | Returns the row with the highest value in a given column |

---

### `DataLab`
The environment that holds and manages multiple datasets.

| Method | Description |
|---|---|
| `add_dataset(ds)` | Adds a dataset to the lab |
| `list_datasets()` | Prints names and row counts of all datasets |
| `compare_averages(col)` | Compares column averages across all datasets and shows the winner |

---

## 🚀 Quick Start

```python
from data_lab import NumericDataset, DataLab

students_data_1 = [
    {"name": "Ali",  "age": 20, "grade": 85},
    {"name": "Sara", "age": 22, "grade": 92},
    {"name": "Omar", "age": 21, "grade": 78},
]

students_data_2 = [
    {"name": "Lina",  "age": 20, "grade": 88},
    {"name": "Yara",  "age": 23, "grade": 95},
    {"name": "Karim", "age": 22, "grade": 74},
]

students1 = NumericDataset("Class A", students_data_1)
students2 = NumericDataset("Class B", students_data_2)

lab = DataLab()
lab.add_dataset(students1)
lab.add_dataset(students2)
```

---

## 💡 Usage Examples

**Filter rows:**
```python
filtered = students1.filter("grade", ">", 80)
print(filtered)
# Dataset 'Class A_filtered' | 2 rows | columns: ['name', 'age', 'grade']
```

**Merge two datasets:**
```python
merged = students1.merge(students2)
print(merged)
# Dataset 'Class A_merged' | 6 rows | columns: ['name', 'age', 'grade']
```

**Get a summary:**
```python
students1.summary()
# ========================================
# Name    : Class A
# Rows    : 3
# Columns : ['name', 'age', 'grade']
# Sample  : {'name': 'Ali', 'age': 20, 'grade': 85}
# ========================================
# Numeric Columns: ['age', 'grade']
#   avg(age) = 21.00
#   avg(grade) = 85.00
# ========================================
```

**Compare averages across datasets:**
```python
lab.compare_averages("grade")
# [DataLab] Comparing 'grade' averages:
#   - 'Class A': avg = 85.00
#   - 'Class B': avg = 85.67
#
#   Winner: 'Class B' with avg = 85.67
```

**Get the top student:**
```python
print(students1.highest("grade"))
# {'name': 'Sara', 'age': 22, 'grade': 92}
```

---

## ✅ Key Design Decisions

- **No external libraries** — built entirely with pure Python
- **Immutable operations** — `filter()` and `merge()` always return a new Dataset, never modifying the original
- **Error handling** — invalid column names and non-numeric operations are handled gracefully without crashing
- **Flexible** — works with any dataset structure (students, sales, employees, etc.)

---

## ⚙️ Requirements

- Python 3.8+
- No pip installs needed

---

## 🗂️ Data Format

Each dataset must be a **list of dictionaries** where all rows share the same keys:

```python
data = [
    {"col1": val1, "col2": val2},
    {"col1": val1, "col2": val2},
]
```

> ⚠️ If any row has different keys, a `ValueError` will be raised on initialization.