# 📈 Investment Portfolio Performance Analysis

## Overview
This project analyzes the performance of a diversified stock portfolio against the S&P 500 benchmark over a 5-year period (2020–2024). Using real market data pulled directly from Yahoo Finance, the analysis calculates key financial metrics, visualizes price trends, measures portfolio diversification, and determines whether the portfolio outperformed the market.

**Result: The portfolio outperformed the S&P 500 with a Sharpe Ratio of 0.61 vs 0.55.**

## 🎯 Business Questions Answered
- Did the portfolio outperform the S&P 500 benchmark?
- Which stocks delivered the best risk-adjusted returns?
- How diversified is the portfolio?
- What were the best and worst months for the portfolio?
- What is the annualized return, volatility, and Sharpe Ratio for each holding?

## 📊 Portfolio Composition

| Ticker | Company | Sector |
|--------|---------|--------|
| AAPL | Apple | Technology |
| JNJ | Johnson & Johnson | Healthcare |
| JPM | JPMorgan Chase | Financial Services |
| AMZN | Amazon | Consumer / E-Commerce |
| PLD | Prologis | Real Estate (REIT) |
| SPY | S&P 500 Index | Benchmark |

**Initial Investment:** $100,000 equally weighted
**Analysis Period:** January 1, 2020 to December 31, 2024

## 📐 Key Metrics

| Metric | Portfolio | S&P 500 |
|--------|-----------|---------|
| Sharpe Ratio | 0.61 | 0.55 |
| Portfolio Outperformed | YES | Baseline |

- **Annualized Return:** Yearly average return standardized for fair comparison
- **Volatility:** How much the portfolio fluctuates day to day, a measure of risk
- **Sharpe Ratio:** Return earned per unit of risk. Above 0.5 is good, above 1.0 is excellent
- **Max Drawdown:** Largest peak-to-trough decline

## 📉 Individual Stock Performance (2020–2024)

| Stock | Ann. Return | Volatility | Sharpe Ratio |
|-------|-------------|------------|--------------|
| AAPL | 28.3% | 31.7% | 0.82 |
| JNJ | 2.4% | 19.7% | 0.02 |
| JPM | 14.5% | 32.5% | 0.45 |
| AMZN | 18.5% | 36.0% | 0.54 |
| PLD | 6.3% | 31.6% | 0.23 |

**Key Insight:** AAPL was the standout performer with a 28.3% annualized return and Sharpe Ratio of 0.82.

## 📊 Visualizations

**1. Portfolio Value vs S&P 500 Benchmark**
Tracks the growth of $100,000 invested in the portfolio vs the S&P 500 from 2020 to 2024.

**2. Individual Stock Cumulative Returns**
Shows how each stock performed on a percentage basis across the full period.

**3. Stock Correlation Matrix**
Heatmap showing how closely each pair of stocks moves together. Green = diversified, Red = correlated.

**4. Risk vs Return Scatter Plot**
Plots each stock by volatility vs return. Stocks above the S&P 500 line deliver better return for the risk taken.

**5. Monthly Returns Heatmap**
Month-by-month portfolio performance across all 5 years. Green = positive month, Red = negative month.

## 🔍 Key Findings

1. The portfolio outperformed the S&P 500 with a Sharpe Ratio of 0.61 vs 0.55
2. Apple drove outperformance with a 28.3% annualized return
3. JNJ had the lowest correlation with AMZN (0.18), providing the best diversification benefit
4. 2022 was the hardest year reflecting the market downturn from interest rate hikes
5. Real Estate (PLD) underperformed due to rising interest rates impacting REIT valuations

## 🛠 Tools Used

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical calculations |
| Matplotlib | Chart development |
| Seaborn | Heatmap and styled visualizations |
| yfinance | Historical stock data from Yahoo Finance |

## 💡 How to Run

```bash
pip install pandas numpy matplotlib seaborn yfinance scikit-learn openpyxl
python portfolio_analysis.py
