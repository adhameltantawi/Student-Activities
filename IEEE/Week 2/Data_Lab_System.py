# Data Lab System


class Dataset:

    def __init__(self, name, data):
        # Validate all rows share the same keys
        first_keys = set(data[0].keys())
        for row in data:
            if set(row.keys()) != first_keys:
                raise ValueError("All rows must have the same columns!")

        self.name    = name
        self.data    = data
        self.rows    = len(data)
        self.columns = list(data[0].keys())

    def summary(self):
        # Print basic info about the dataset
        print("=" * 40)
        print(f"Name    : {self.name}")
        print(f"Rows    : {self.rows}")
        print(f"Columns : {self.columns}")
        print(f"Sample  : {self.data[0]}")
        print("=" * 40)

    def get_column(self, column_name):
        # Return all values in the given column
        if column_name not in self.columns:
            raise KeyError(f"Column '{column_name}' not found! Available: {self.columns}")
        return [row[column_name] for row in self.data]

    def average(self, column_name):
        # Return the average of a numeric column
        try:
            values = self.get_column(column_name)
        except KeyError as e:
            print(f"[Error] {e}")
            return None

        if not all(isinstance(v, (int, float)) for v in values):
            print(f"[Warning] Column '{column_name}' is not numeric.")
            return None

        return sum(values) / len(values)

    def filter(self, column_name, operator, value):
        # Filter rows by condition and return a new Dataset (original unchanged)
        if column_name not in self.columns:
            raise KeyError(f"Column '{column_name}' not found!")

        if operator == ">":
            result = [row for row in self.data if row[column_name] > value]
        elif operator == "<":
            result = [row for row in self.data if row[column_name] < value]
        elif operator == "==":
            result = [row for row in self.data if row[column_name] == value]
        else:
            raise ValueError(f"Operator '{operator}' not supported. Use: '>', '<', '=='")

        if not result:
            print("[Info] No rows matched the filter.")
            result = [dict.fromkeys(self.columns, None)]

        return Dataset(self.name + "_filtered", result)

    def merge(self, other):
        # Combine two datasets into a new one (both originals unchanged)
        if sorted(self.columns) != sorted(other.columns):
            raise ValueError("Cannot merge: datasets have different columns!")

        return Dataset(self.name + "_merged", self.data + other.data)

    def __len__(self):
        # Allows: len(dataset)
        return self.rows

    def __str__(self):
        # Allows: print(dataset)
        return f"Dataset '{self.name}' | {self.rows} rows | columns: {self.columns}"


class NumericDataset(Dataset):
    # Extends Dataset with numeric-focused features

    def __init__(self, name, data):
        super().__init__(name, data)

    def summary(self):
        super().summary()   # Call parent summary first

        # Find and print averages for all numeric columns
        numeric_cols = [
            col for col in self.columns
            if all(isinstance(row[col], (int, float)) for row in self.data)
        ]
        print(f"Numeric Columns: {numeric_cols}")
        for col in numeric_cols:
            print(f"  avg({col}) = {self.average(col):.2f}")
        print("=" * 40)

    def highest(self, column_name):
        # Return the row with the highest value in the given column
        try:
            values = self.get_column(column_name)
        except KeyError as e:
            print(f"[Error] {e}")
            return None

        if not all(isinstance(v, (int, float)) for v in values):
            print(f"[Warning] Column '{column_name}' is not numeric.")
            return None

        max_value = max(values)
        return next(row for row in self.data if row[column_name] == max_value)


class DataLab:
    # Environment that holds and compares multiple datasets

    def __init__(self):
        self.datasets = []

    def add_dataset(self, dataset):
        # Add a Dataset or NumericDataset to the lab
        self.datasets.append(dataset)
        print(f"[DataLab] Added: '{dataset.name}'")

    def list_datasets(self):
        # Print names of all datasets in the lab
        print("\n[DataLab] Datasets:")
        for i, ds in enumerate(self.datasets, 1):
            print(f"  {i}. {ds.name} ({len(ds)} rows)")
        print()

    def compare_averages(self, column_name):
        # Compare column averages across all datasets and show the winner
        print(f"\n[DataLab] Comparing '{column_name}' averages:")
        results = []

        for ds in self.datasets:
            if column_name not in ds.columns:
                print(f"  - '{ds.name}': column not found, skipped.")
                continue

            avg = ds.average(column_name)
            if avg is None:
                continue

            print(f"  - '{ds.name}': avg = {avg:.2f}")
            results.append((ds.name, avg))

        if results:
            best = max(results, key=lambda x: x[1])
            print(f"\n  Winner: '{best[0]}' with avg = {best[1]:.2f}\n")


# Example Usage 

students_data_1 = [
    {"name": "Ali",   "age": 20, "grade": 85},
    {"name": "Sara",  "age": 22, "grade": 92},
    {"name": "Omar",  "age": 21, "grade": 78},
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
lab.list_datasets()

filtered = students1.filter("grade", ">", 80)
print(filtered)

merged = students1.merge(students2)
print(merged)

students1.summary()

lab.compare_averages("grade")

print("Top student:", students1.highest("grade"))
print("Rows:", len(students1))
print(students1)