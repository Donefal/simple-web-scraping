# Simple Web Scraping Experiment
**Website:** https://www.scrapethissite.com/pages/simple/

- **Goals of the project :** To find top 10 country with the most dense population

## Workflow:
- Scrape the website using requests and Beautiful soup, then export it into an excel. File: `scrape.ipynb`
- Manually clean the excel output (Period to comma in number formatting, and also extracting the scientific notation)
- Import it all into a PostgreSQL using SQLalchemy. File: `databse.py`
- Visualize the data into a bar char using simple Matplot. File: `vizualization.py`

**Final Product:** `top_country.png`


