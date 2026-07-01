import pandas as pd
import numpy as np


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------- Load & explore ----------

def load_data():
    books = pd.read_csv("data/books.csv")
    borrowings = pd.read_csv("data/borrowings.csv")
    members = pd.read_csv("data/members.csv")
    return books, borrowings, members


def explore(books, borrowings, members):
    for name, df in [("books", books), ("borrowings", borrowings), ("members", members)]:
        section(f"EXPLORE: {name}")
        print(df.shape)
        print(df.dtypes)
        print(df.isnull().sum())
        print(df.head())

