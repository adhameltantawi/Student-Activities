# Library Management Analysis

Analyzes how books are borrowed at a local library using Pandas and NumPy,
to surface insights that could help the library improve its services.

## Dataset

`data/` contains three CSV files:

- **books.csv** (400 rows) — BookID, Title, Author, Genre, PublicationYear, Publisher, Pages, Language, CopiesAvailable
- **members.csv** (150 rows) — MemberID, Name, MembershipType, Age, Gender, JoinDate
- **borrowings.csv** (2000 rows) — BorrowID, MemberID, BookID, BorrowDate, ReturnDate

`borrowings` links to `books` via `BookID` and to `members` via `MemberID`.

The data has no missing values, duplicates, or broken references. The only
change made is converting the date columns from text to datetime, since
that's needed to compute borrow duration and monthly trends.

## How to Run

```bash
pip install -r requirements.txt
python analysis.py
```

This prints the dataset exploration, probability calculations, Pandas
analysis, NumPy analysis, and a final summary to the console. Running it
again with no changes produces the same results.

Optional — save the output to a file:
```bash
python analysis.py > output/analysis_report.txt
```

## What's Covered

- Exploration of each table's shape, dtypes, missing values, and preview.
- Probability of borrowing a given genre, of a member having a given
  membership type, and of both conditions holding at once.
- Pandas: most/least borrowed genre, top borrowers, borrowing by
  membership type, borrowings by publication year, top authors, books
  never borrowed, average duration by genre, genre distribution, monthly
  trend, and three extra insights (top titles, borrowing by age group,
  demand vs. supply by genre).
- NumPy: numerical columns as arrays, min/max, boolean indexing, sorting,
  and a vectorized borrows-per-copy metric.
- A final summary of the key takeaways.
