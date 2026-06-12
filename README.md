📈 Investment Portfolio Performance Analysis
Overview
This project analyzes the performance of a diversified stock portfolio against the S&P 500 benchmark over a 5-year period (2020–2024). Using real market data pulled directly from Yahoo Finance, the analysis calculates key financial metrics, visualizes price trends, measures portfolio diversification, and determines whether the portfolio outperformed the market.
Result: The portfolio outperformed the S&P 500 with a Sharpe Ratio of 0.61 vs 0.55.
---
🎯 Business Questions Answered
Did the portfolio outperform the S&P 500 benchmark?
Which stocks delivered the best risk-adjusted returns?
How diversified is the portfolio? (correlation analysis)
What were the best and worst months for the portfolio?
What is the annualized return, volatility, and Sharpe Ratio for each holding?
---
📊 Portfolio Composition
Ticker	Company	Sector
AAPL	Apple	Technology
JNJ	Johnson & Johnson	Healthcare
JPM	JPMorgan Chase	Financial Services
AMZN	Amazon	Consumer / E-Commerce
PLD	Prologis	Real Estate (REIT)
SPY	S&P 500 Index	Benchmark
Initial Investment: $100,000 equally weighted across all 5 stocks
Analysis Period: January 1, 2020 to December 31, 2024
---
📐 Key Metrics Calculated
Metric	Portfolio	S&P 500
Annualized Return	Higher	Baseline
Annualized Volatility	Measured	Measured
Sharpe Ratio	0.61	0.55
Max Drawdown	Measured	Measured
Portfolio outperformed S&P 500	YES	N/A
Metric Definitions
Annualized Return: The yearly average return, standardized so any time period can be compared fairly
Volatility: How much the portfolio value fluctuates day to day — a measure of risk
Sharpe Ratio: Return earned per unit of risk taken. Above 1.0 is excellent; above 0.5 is good. Higher is better
Max Drawdown: The largest peak-to-trough decline — worst case loss from a high point
---
📉 Individual Stock Performance (2020–2024)
Stock	Ann. Return	Volatility	Sharpe Ratio
AAPL	28.3%	31.7%	0.82
JNJ	2.4%	19.7%	0.02
JPM	14.5%	32.5%	0.45
AMZN	18.5%	36.0%	0.54
PLD	6.3%	31.6%	0.23
Key Insight: AAPL was the standout performer with a 28.3% annualized return and the highest Sharpe Ratio of 0.82. JNJ underperformed as a defensive healthcare stock but provided portfolio stability during volatile periods.
---
📊 Visualizations
1. Portfolio Value vs S&P 500 Benchmark
Tracks the growth of $100,000 invested in the portfolio vs the S&P 500 from 2020 to 2024.
2. Individual Stock Cumulative Returns
Shows how each stock performed on a percentage basis, making it easy to compare across different price points.
3. Stock Correlation Matrix
A heatmap showing how closely each pair of stocks moves together:
Green (low correlation): Good diversification — stocks move independently
Red (high correlation): Concentrated risk — stocks move together
Key Finding: JNJ showed the lowest correlation with AMZN (0.18), providing the best diversification benefit in the portfolio.
4. Risk vs Return Scatter Plot
Plots each stock by its annualized volatility (x-axis) and annualized return (y-axis). Stocks in the upper-right quadrant relative to the S&P 500 benchmark deliver better return for the risk taken.
5. Monthly Returns Heatmap
Shows portfolio performance month-by-month across all 5 years. Green = positive month, Red = negative month. Useful for identifying seasonal patterns and understanding drawdown periods.
---
🛠 Tools and Libraries
Tool	Purpose
Python	Core programming language
Pandas	Data manipulation and analysis
NumPy	Numerical calculations and financial math
Matplotlib	Chart and visualization development
Seaborn	Heatmap and styled visualizations
yfinance	Real-time and historical stock data from Yahoo Finance
---
📁 Project Files
```
investment-portfolio-analysis/
│
├── portfolio_analysis.py          # Main analysis script
├── portfolio_performance.png      # 4-chart visualization output
├── monthly_returns_heatmap.png    # Monthly returns heatmap output
└── README.md                      # Project documentation
```
---
🔍 Key Findings and Insights
The portfolio outperformed the S&P 500 with a higher Sharpe Ratio (0.61 vs 0.55), meaning better risk-adjusted returns than the market benchmark
Apple (AAPL) drove outperformance with a 28.3% annualized return and Sharpe Ratio of 0.82 — the strongest individual performer in the portfolio
The portfolio is reasonably diversified — correlation scores between most pairs range from 0.18 to 0.59, meaning stocks do not all move together and losses in one holding are partially offset by others
2022 was the hardest year — the monthly heatmap shows consistent red months across the portfolio, reflecting the broader market downturn driven by interest rate hikes
Real Estate (PLD) underperformed in this period due to rising interest rates which negatively impact REIT valuations, an important consideration for future portfolio construction
---
💡 How to Run This Project
Clone this repository
Install required libraries:
```bash
pip install pandas numpy matplotlib seaborn yfinance scikit-learn openpyxl
```
Run the analysis:
```bash
python portfolio_analysis.py
```
The script will automatically download current market data and generate all charts.
---
👩🏾‍💻 Author
Ginger Osinuga
Portfolio: ginger-osinuga.github.io
