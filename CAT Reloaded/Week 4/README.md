# CAT Reloaded – Week 4: Pandas (Continued)

Beginner's Task 4 for the **CAT Reloaded Data Science** track.  
Covers advanced Pandas operations using the **Stack Overflow Developer Survey 2019** dataset.

## Topics Covered

- Sorting with `sort_values()` (multi-column, mixed ascending/descending)
- Grouping with `groupby()` and aggregation (`value_counts`, `median`, `count`)
- Filtering grouped data (`str.contains`)
- Concatenating Series with `pd.concat()`
- Handling missing data (`dropna`, `isna`)
- Cleaning columns (`.unique()`, `.replace()`)
- Exporting to Excel (`.to_excel()`)

## Dataset

**Stack Overflow Developer Survey 2019** (~89K responses, 85 columns).

| File | Description |
|------|-------------|
| `survey_results_public.csv` | Main survey results |
| `survey_results_schema.csv` | Column name → question mapping |
| `so_survey_2019.pdf` | Original survey instrument |

> Source: [Stack Overflow Insights](https://insights.stackoverflow.com/survey/2019) — licensed under [ODbL](http://opendatacommons.org/licenses/odbl/1.0/)

