# Week 2 — Dashboards & Web Scraping

**Project:** Dashboard Making using Power BI & Dataset making using Web Scraping
**Tools:** Power BI, Python, BeautifulSoup, Requests, Pandas, Matplotlib, Seaborn

This week's project is split into three tasks: building Power BI dashboards on
existing datasets, scraping a fresh dataset from the web, and analyzing that
scraped dataset for insights.

---

## Task 5 — Introduction to Power BI

**Goal:** Import and model datasets in Power BI, then build an interactive
dashboard with slicers and filters. (Earlier in the course this kind of
analysis was done in a Jupyter notebook `.ipynb` with Python/pandas — this
task rebuilds it as a live, clickable Power BI report instead of static code
output.)

**Deliverables:**
- `Blinkit_Dashboard.pbix`
- `Netflix_Dashboard.pbix`

### Datasets

**1. BlinkIT Grocery Data** (`BlinkIT_Grocery_Data.xlsx`)
- 8,523 rows × 12 columns
- Fields: Item Identifier, Item Type (16 categories), Item Fat Content, Item
  Weight, Item Visibility, Outlet Identifier (10 outlets), Outlet Establishment
  Year, Outlet Size, Outlet Location Type, Outlet Type (Grocery Store,
  Supermarket Type 1/2/3), Sales, Rating

**2. Netflix Data** (`netflix_titles.csv`)
- 8,807 rows × 12 columns
- Fields: show_id, type (Movie/TV Show), title, director, cast, country,
  date_added, release_year, rating, duration, listed_in (genre), description

### Steps Performed
1. **Import** — loaded the Excel/CSV files into Power BI Desktop via *Get Data*.
2. **Data modeling (Power Query)** — standardized inconsistent labels (e.g.
   Item Fat Content values), fixed data types, removed nulls/duplicates, and
   built table relationships in Model view.
3. **Dashboard build** — KPI cards (Total Sales, Average Rating for Blinkit;
   Total Titles, Movies vs TV Shows split for Netflix) and bar/column charts
   broken down by category (Item Type, Outlet Type / Genre, Country, Release
   Year).
4. **Interactivity** — slicers (Outlet Type, Outlet Location Type, Item Type /
   Type, Country, Release Year) with cross-filtering enabled between visuals.

### Outcome
Two interactive `.pbix` dashboards that let a user explore the data themselves
by clicking filters, instead of reading fixed notebook output.

---

## Task 6 — Web Scraping

**Goal:** Collect structured data from online sources using BeautifulSoup and
Requests, and store the results as a CSV.

**Approach:**
1. Sent HTTP requests to the target page(s) using `requests`.
2. Parsed the HTML response with `BeautifulSoup` to locate the relevant
   tables/elements.
3. Extracted structured fields (title, genre, rating/score, runtime, language,
   etc.) into a list of records.
4. Loaded the records into a `pandas` DataFrame and exported to CSV.

**Resulting datasets:**
- `NetflixOriginals.csv` — 584 rows × 6 columns (Title, Genre, Premiere,
  Runtime, IMDB Score, Language)
- `netflix-rotten-tomatoes-metacritic-imdb.csv` — 15,480 rows × 29 columns,
  combining Netflix catalog info with IMDb, Rotten Tomatoes, and Metacritic
  scores, awards, box office, and release dates

---

## Task 7 — Insights & Trends Analysis

**Goal:** Analyze the scraped dataset to identify key patterns, trends, and
outliers, and present findings through charts (Matplotlib/Seaborn).

**Analysis performed on `NetflixOriginals.csv` /
`netflix-rotten-tomatoes-metacritic-imdb.csv`:**
- **Genre trends** — most common genres among Netflix Originals, and how
  average IMDb score varies by genre.
- **Score comparison** — comparing IMDb Score against Rotten Tomatoes and
  Metacritic scores to spot titles that critics and audiences rated very
  differently (outliers).
- **Language distribution** — count of titles by language, highlighting the
  dominance of English-language originals versus international content.
- **Runtime patterns** — distribution of movie runtimes and whether longer
  runtime correlates with higher/lower scores.
- **Release trends over time** — number of titles released per year to show
  Netflix's content output growth.

**Charts produced:** bar charts (genre/language counts), histograms (runtime
and score distributions), and scatter plots (IMDb vs Rotten Tomatoes/
Metacritic scores) using Matplotlib and Seaborn.

## Tools Used
Power BI (Desktop), Python, BeautifulSoup, Requests, Pandas, Matplotlib,
Seaborn
