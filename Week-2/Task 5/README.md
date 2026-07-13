# Task 5 — Introduction to Power BI

**Project:** Dashboard Making using Power BI & Dataset making using Web Scraping
**Week:** 2
**Tools used:** Power BI Desktop

## Objective
Import and model datasets in Power BI, then build an interactive dashboard using
slicers and filters. (Previously this analysis was done in a Jupyter notebook
`.ipynb` with Python/pandas; this task recreates it as a live Power BI report.)

## Deliverables
- `Blinkit_Dashboard.pbix`
- `Netflix_Dashboard.pbix`

## Datasets Used

### 1. BlinkIT Grocery Data (`BlinkIT_Grocery_Data.xlsx`)
- **Rows / Columns:** 8,523 rows × 12 columns
- **Key fields:** Item Identifier, Item Type (16 categories), Item Fat Content,
  Item Weight, Item Visibility, Outlet Identifier (10 outlets), Outlet Establishment
  Year, Outlet Size, Outlet Location Type, Outlet Type (4 types: Grocery Store,
  Supermarket Type 1/2/3), Sales, Rating

### 2. Netflix Data (`netflix_titles.csv`, plus `NetflixOriginals.csv` and
`netflix-rotten-tomatoes-metacritic-imdb.csv` as supplementary sources)
- **Rows / Columns:** 8,807 rows × 12 columns (main titles file)
- **Key fields:** show_id, type (Movie/TV Show), title, director, cast, country,
  date_added, release_year, rating, duration, listed_in (genre), description

## Steps Performed

1. **Import** — Loaded the Excel and CSV files into Power BI Desktop via
   *Get Data*.
2. **Data Modeling / Cleaning (Power Query)**
   - Standardized inconsistent category labels (e.g. Item Fat Content values).
   - Verified/corrected data types (dates, numbers, text).
   - Removed nulls/duplicates where relevant.
   - Built table relationships in Model view where multiple files were combined.
3. **Dashboard Build**
   - KPI cards (e.g. Total Sales, Average Rating for Blinkit; Total Titles,
     Movies vs TV Shows split for Netflix).
   - Bar/column charts breaking down data by category (Item Type, Outlet Type
     for Blinkit; Genre, Country, Release Year for Netflix).
   - Trend visuals where time-based fields were available.
4. **Interactivity**
   - Added **slicers** (Outlet Type, Outlet Location Type, Item Type / Type,
     Country, Release Year) so users can filter the whole report dynamically.
   - Cross-filtering enabled between visuals on the same page.

## Outcome
Two fully interactive `.pbix` dashboards replacing the earlier static
notebook-based analysis, allowing end users to explore the data themselves
through clicks and filters rather than reading fixed code output.

## Tools
Power BI (Desktop) — Get Data, Power Query, Data Model view, Report view
(slicers, cards, bar/column charts).
