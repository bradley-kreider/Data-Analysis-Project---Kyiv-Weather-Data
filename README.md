# Data Analysis Project — Kyiv Weather Data

A statistical study of historical temperature trends in Kyiv, Ukraine, using 85 years of daily records (1940–2025) pulled from the [Open-Meteo](https://open-meteo.com/) archive. The project tests for a long-term warming trend and compares temperatures across two historical eras.

Completed by Brad Kreider.

## Research Questions

1. Is there a measurable long-term trend in Kyiv's annual mean temperature from 1940 to 2025?
2. Are average daily-maximum temperatures in the recent era (1983–2025) significantly higher than in the earlier era (1940–1982)?

## Data

Daily mean, maximum, and minimum 2 m temperatures for Kyiv (50.45° N, 30.52° E) are retrieved from the Open-Meteo Historical Weather API via `open-meteo.py` and saved to CSV. Daily values are aggregated to annual averages for analysis.

## Methods

Analysis is written in **R** and run inside a Jupyter/Colab notebook through `rpy2`:

- **Linear regression** of annual mean temperature on year to estimate the warming trend, with residual, histogram, and scale-location plots to check model assumptions.
- **Two-sample t-test** (one-sided, equal variance) comparing average daily-maximum temperature between the early era (1940–1982) and late era (1983–2025), supported by histograms and boxplots of each era.

## Repository Contents

| File | Description |
|------|-------------|
| `regression.ipynb` | Main analysis notebook: data prep, regression, diagnostics, and the era comparison |
| `open-meteo.py` | Script that pulls daily Kyiv temperature data from the Open-Meteo archive API |
| `kyiv_temperature_1940_2025.csv` | Cached daily temperature dataset (mean / max / min) |

## Data Source

Weather data © [Open-Meteo.com](https://open-meteo.com/), Historical Weather API.
