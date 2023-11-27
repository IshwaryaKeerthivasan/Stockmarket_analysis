# Amazon Stockmarket Analysis

## Abstract
The project delves deeply into dissecting Amazon's stock market performance using yfinance and statistical methodologies. The analysis scrutinizes both short and long-term Simple Moving Averages (SMA), signaling potential investment paths upon observing SMA intersections. A general guideline recommends a bullish stance when the shorter SMA eclipses the longer SMA. Furthermore, it conducts regression analysis on the SMA-50, uncovering an upward trend in Amazon's stock prices. Ultimately, the project furnishes a comprehensive perspective on Amazon's stock market behavior, equipping investors with valuable insights to inform potential investment strategies.

## Problem Definition
Analyzing Amazon's stock market performance using yfinance and statistical tools to identify trends and potential investment opportunities based on moving averages and regression analysis.

## Motivation
Unlocking investment potential through insightful analysis of Amazon's stock behavior with data-driven precision


## Installation
Install plotly and yfinance

```bash
  pip install plotly yfinance
```
Install TA-Lib in colab

```bash
  !wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
  !tar -xvzf ta-lib-0.4.0-src.tar.gz
  %cd ta-lib
  !./configure --prefix=/usr
  !make
  !make install
  !pip install TA-Lib
```

## Regression analysis for closing stock of Amazon:
<img width="858" alt="image" src="https://github.com/IshwaryaKeerthivasan/Stockmarket_analysis/assets/92322280/8a43bc69-6a7d-497e-b86e-b9ee1c1b4a0f">

## Bibliography
* Yfinance - https://finance.yahoo.com/most-active
* GitHub repository: https://github.com/ranaroussi/yfinance (for technical details, source code, and community contributions)
* TA-Lib Documentation: https://github.com/TA-Lib/ta-lib
* Python Documentation: https://docs.python.org/3/
* Plotly Documentation: https://plotly.com/python/
