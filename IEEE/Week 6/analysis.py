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


# ---------- Pandas analysis ----------

def run_pandas(books, borrowings, merged):
    results = {}

    section("Borrowings per genre (highest/lowest)")
    results["genre_counts"] = merged["Genre"].value_counts()
    print(results["genre_counts"])

    section("Most frequent borrowers")
    results["top_borrowers"] = merged.groupby(["MemberID", "Name"])["BorrowID"].count().sort_values(ascending=False).head(5)
    print(results["top_borrowers"])

    section("Borrowing by membership type")
    results["by_membership"] = merged.groupby("MembershipType")["BorrowID"].count().sort_values(ascending=False)
    print(results["by_membership"])

    section("Borrowings by publication year")
    results["by_year"] = merged.groupby("PublicationYear")["BorrowID"].count().sort_index()
    print(results["by_year"])

    section("Most popular authors")
    results["top_authors"] = merged.groupby("Author")["BorrowID"].count().sort_values(ascending=False).head(5)
    print(results["top_authors"])

    section("Books never borrowed")
    results["never_borrowed"] = books[~books["BookID"].isin(borrowings["BookID"])][["BookID", "Title", "Author", "Genre"]]
    print(f"{len(results['never_borrowed'])} of {len(books)} books never borrowed")
    print(results["never_borrowed"])

    section("Average borrow duration by genre")
    results["duration_by_genre"] = merged.groupby("Genre")["Duration"].mean().sort_values(ascending=False).round(2)
    print(results["duration_by_genre"])

    section("Genre distribution of the catalog")
    results["genre_distribution"] = books["Genre"].value_counts()
    print(results["genre_distribution"])

    section("Monthly borrowing trend")
    results["monthly_trend"] = borrowings.set_index("BorrowDate").resample("MS")["BorrowID"].count()
    print(results["monthly_trend"])

    # Three additional insights
    section("Extra insight 1: most borrowed titles")
    results["top_books"] = merged.groupby(["BookID", "Title"])["BorrowID"].count().sort_values(ascending=False).head(5)
    print(results["top_books"])

    section("Extra insight 2: borrowing by age group")
    merged["AgeGroup"] = pd.cut(merged["Age"], bins=[0, 18, 30, 45, 60, 120], labels=["<18", "18-30", "31-45", "46-60", "60+"])
    results["by_age_group"] = merged.groupby("AgeGroup", observed=True)["BorrowID"].count()
    print(results["by_age_group"])

    section("Extra insight 3: demand vs supply by genre")
    supply = books.groupby("Genre")["CopiesAvailable"].sum()
    demand = merged.groupby("Genre")["BorrowID"].count()
    demand_supply = pd.DataFrame({"CopiesAvailable": supply, "Borrowings": demand})
    demand_supply["BorrowingsPerCopy"] = (demand_supply["Borrowings"] / demand_supply["CopiesAvailable"]).round(2)
    results["demand_supply"] = demand_supply.sort_values("BorrowingsPerCopy", ascending=False)
    print(results["demand_supply"])

    return results


# ---------- NumPy analysis ----------

def run_numpy(books, borrowings, merged):
    section("NumPy: columns as arrays")
    durations = borrowings["Duration"].to_numpy()
    pages = books["Pages"].to_numpy()
    print("durations:", durations[:5])
    print("pages:", pages[:5])

    section("NumPy: highest/lowest duration")
    print(f"Min: {durations.min()} days | Max: {durations.max()} days")

    section("NumPy: boolean indexing (borrowings > 21 days)")
    long_borrowings = durations[durations > 21]
    print(f"{len(long_borrowings)} of {len(durations)} borrowings lasted > 21 days")

    section("NumPy: sorted array (page counts, descending)")
    print(np.sort(pages)[::-1][:10])

    section("NumPy: vectorized calculation - borrows per copy")
    counts = merged.groupby("BookID")["BorrowID"].count().reindex(books["BookID"], fill_value=0).to_numpy()
    copies = books["CopiesAvailable"].to_numpy()
    pressure = counts / np.where(copies == 0, 1, copies)
    print("Top 5 demand-pressure values:", np.sort(pressure)[::-1][:5])


# ---------- Summary ----------

def print_summary(pandas_results, books):
    section("FINAL SUMMARY")

    g = pandas_results["genre_counts"]
    top_borrower = pandas_results["top_borrowers"].iloc[0]
    never = pandas_results["never_borrowed"]
    d = pandas_results["duration_by_genre"]
    a = pandas_results["top_authors"]
    ds = pandas_results["demand_supply"]

    print(f"1. Most borrowed genre: '{g.idxmax()}' ({g.max()}). Least borrowed: '{g.idxmin()}' ({g.min()}).")
    print(f"2. Top borrower has {top_borrower} borrowings.")
    print(f"3. {len(never)} of {len(books)} books ({len(never)/len(books):.1%}) have never been borrowed.")
    print(f"4. Avg borrow duration ranges from {d.min():.1f} days ('{d.idxmin()}') to {d.max():.1f} days ('{d.idxmax()}').")
    print(f"5. Most borrowed author: '{a.index[0]}' ({a.iloc[0]} borrowings).")
    print(f"6. '{ds['BorrowingsPerCopy'].idxmax()}' has the highest borrows-per-copy ratio ({ds['BorrowingsPerCopy'].max():.2f}), suggesting it may be understocked.")


def main():
    section("LIBRARY MANAGEMENT ANALYSIS")
    books, borrowings, members = load_data()
    explore(books, borrowings, members)

    books, borrowings, members = clean(books, borrowings, members)
    merged = merge_all(books, borrowings, members)

    run_probability(merged, members)
    pandas_results = run_pandas(books, borrowings, merged)
    run_numpy(books, borrowings, merged)
    print_summary(pandas_results, books)


if __name__ == "__main__":
    main()
