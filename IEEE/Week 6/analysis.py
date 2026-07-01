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


# ---------- Clean & merge ----------

def clean(books, borrowings, members):
    # Only issue found: dates are stored as strings. Convert them so date
    # arithmetic (duration, monthly trend) works.
    borrowings["BorrowDate"] = pd.to_datetime(borrowings["BorrowDate"])
    borrowings["ReturnDate"] = pd.to_datetime(borrowings["ReturnDate"])
    members["JoinDate"] = pd.to_datetime(members["JoinDate"])
    borrowings["Duration"] = (borrowings["ReturnDate"] - borrowings["BorrowDate"]).dt.days
    return books, borrowings, members


def merge_all(books, borrowings, members):
    merged = borrowings.merge(books, on="BookID").merge(members, on="MemberID")
    return merged


# ---------- Probability ----------

def run_probability(merged, members):
    section("PROBABILITY")

    genre, membership = "Fantasy", "Student"

    p_genre = (merged["Genre"] == genre).mean()
    p_membership = (members["MembershipType"] == membership).mean()
    p_both = ((merged["Genre"] == genre) & (merged["MembershipType"] == membership)).mean()

    print(f"P(borrowed book is '{genre}') = {p_genre:.4f}")
    print(f"P(member is '{membership}') = {p_membership:.4f}")
    print(f"P(genre='{genre}' and membership='{membership}') = {p_both:.4f}")

