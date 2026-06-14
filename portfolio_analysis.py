# ============================================================
# Investment Portfolio Performance Analysis
# Author: Ginger Osinuga
# Description: Analyzes stock portfolio performance vs S&P 500
# Tools: Python, Pandas, NumPy, Matplotlib, Seaborn, yfinance
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

# ── SETTINGS ──────────────────────────────────────────────
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ── PORTFOLIO DEFINITION ───────────────────────────────────
# A diversified portfolio across tech, healthcare, finance,
# consumer, and real estate sectors
TICKERS = {
    'AAPL':  'Apple (Tech)',
    'JNJ':   'Johnson & Johnson (Healthcare)',
    'JPM':   'JPMorgan Chase (Finance)',
    'AMZN':  'Amazon (Consumer)',
    'PLD':   'Prologis (Real Estate REIT)',
    'SPY':   'S&P 500 Benchmark'
}

PORTFOLIO_TICKERS = ['AAPL', 'JNJ', 'JPM', 'AMZN', 'PLD']
BENCHMARK = 'SPY'
START_DATE = '2020-01-01'
END_DATE   = '2024-12-31'
INITIAL_INVESTMENT = 100000  # $100,000 equally split

print("=" * 60)
print("  INVESTMENT PORTFOLIO PERFORMANCE ANALYSIS")
print("=" * 60)
print(f"\nPortfolio: {', '.join(PORTFOLIO_TICKERS)}")
print(f"Benchmark: {BENCHMARK} (S&P 500)")
print(f"Period: {START_DATE} to {END_DATE}")
print(f"Initial Investment: ${INITIAL_INVESTMENT:,}\n")

# ── DOWNLOAD DATA ──────────────────────────────────────────
print("Downloading historical price data...")
all_tickers = PORTFOLIO_TICKERS + [BENCHMARK]
raw = yf.download(all_tickers, start=START_DATE, end=END_DATE,
                  auto_adjust=True, progress=False)
prices = raw['Close'].dropna()
print(f"Data loaded: {len(prices)} trading days\n")

# ── DAILY RETURNS ──────────────────────────────────────────
returns = prices.pct_change().dropna()

# ── PORTFOLIO RETURNS (equal weight) ──────────────────────
port_returns = returns[PORTFOLIO_TICKERS].mean(axis=1)
bench_returns = returns[BENCHMARK]

# ── CUMULATIVE RETURNS ─────────────────────────────────────
port_cumulative  = (1 + port_returns).cumprod()
bench_cumulative = (1 + bench_returns).cumprod()

port_value  = INITIAL_INVESTMENT * port_cumulative
bench_value = INITIAL_INVESTMENT * bench_cumulative

# ── PERFORMANCE METRICS ────────────────────────────────────
TRADING_DAYS = 252

def annualized_return(cum_series):
    total = cum_series.iloc[-1] - 1
    years = len(cum_series) / TRADING_DAYS
    return (1 + total) ** (1 / years) - 1

def annualized_volatility(daily_returns):
    return daily_returns.std() * np.sqrt(TRADING_DAYS)

def sharpe_ratio(daily_returns, risk_free=0.04):
    excess = daily_returns - risk_free / TRADING_DAYS
    return (excess.mean() / excess.std()) * np.sqrt(TRADING_DAYS)

def max_drawdown(cum_series):
    rolling_max = cum_series.cummax()
    drawdown = (cum_series - rolling_max) / rolling_max
    return drawdown.min()

# Portfolio metrics
p_ann_ret  = annualized_return(port_cumulative)
p_vol      = annualized_volatility(port_returns)
p_sharpe   = sharpe_ratio(port_returns)
p_drawdown = max_drawdown(port_cumulative)
p_final    = port_value.iloc[-1]

# Benchmark metrics
b_ann_ret  = annualized_return(bench_cumulative)
b_vol      = annualized_volatility(bench_returns)
b_sharpe   = sharpe_ratio(bench_returns)
b_drawdown = max_drawdown(bench_cumulative)
b_final    = bench_value.iloc[-1]

print("=" * 60)
print(f"{'METRIC':<30} {'PORTFOLIO':>12} {'S&P 500':>12}")
print("-" * 60)
print(f"{'Annualized Return':<30} {p_ann_ret:>11.1%} {b_ann_ret:>11.1%}")
print(f"{'Annualized Volatility':<30} {p_vol:>11.1%} {b_vol:>11.1%}")
print(f"{'Sharpe Ratio':<30} {p_sharpe:>12.2f} {b_sharpe:>12.2f}")
print(f"{'Max Drawdown':<30} {p_drawdown:>11.1%} {b_drawdown:>11.1%}")
print(f"{'Final Portfolio Value':<30} ${p_final:>10,.0f} ${b_final:>10,.0f}")
print(f"{'Total Return':<30} {(p_final/INITIAL_INVESTMENT-1):>11.1%} {(b_final/INITIAL_INVESTMENT-1):>11.1%}")
print("=" * 60)

# ── INDIVIDUAL STOCK METRICS ───────────────────────────────
print("\nINDIVIDUAL STOCK PERFORMANCE")
print("-" * 60)
print(f"{'Stock':<10} {'Ann. Return':>12} {'Volatility':>12} {'Sharpe':>10}")
print("-" * 60)
for ticker in PORTFOLIO_TICKERS:
    r = returns[ticker]
    c = (1 + r).cumprod()
    print(f"{ticker:<10} {annualized_return(c):>11.1%} "
          f"{annualized_volatility(r):>11.1%} "
          f"{sharpe_ratio(r):>10.2f}")

# ── VISUALIZATION 1: Portfolio vs Benchmark ────────────────
fig, axes = plt.subplots(2, 2, figsize=(18, 13))
fig.suptitle('Investment Portfolio Performance Analysis (2020-2024)',
             fontsize=16, fontweight='bold', y=1.02)

# Chart 1: Portfolio Value Over Time
ax1 = axes[0, 0]
ax1.plot(port_value.index, port_value.values,
         color='#2E86AB', linewidth=2.5, label='My Portfolio')
ax1.plot(bench_value.index, bench_value.values,
         color='#E84855', linewidth=2, linestyle='--', label='S&P 500')
ax1.axhline(INITIAL_INVESTMENT, color='gray', linestyle=':', alpha=0.5)
ax1.fill_between(port_value.index, INITIAL_INVESTMENT,
                 port_value.values, alpha=0.1, color='#2E86AB')
ax1.set_title('Portfolio Value vs S&P 500 Benchmark', fontweight='bold')
ax1.set_ylabel('Portfolio Value ($)')
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
ax1.legend(fontsize=10)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Chart 2: Cumulative Returns Comparison
ax2 = axes[0, 1]
for ticker in PORTFOLIO_TICKERS:
    c = (1 + returns[ticker]).cumprod() - 1
    ax2.plot(c.index, c.values * 100,
             linewidth=1.5, label=ticker, alpha=0.8)
bench_cum = (1 + bench_returns).cumprod() - 1
ax2.plot(bench_cum.index, bench_cum.values * 100,
         color='black', linewidth=2.5, linestyle='--',
         label='S&P 500', alpha=0.9)
ax2.axhline(0, color='gray', linestyle=':', alpha=0.5)
ax2.set_title('Individual Stock Cumulative Returns (%)', fontweight='bold')
ax2.set_ylabel('Cumulative Return (%)')
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))
ax2.legend(fontsize=8, ncol=2)
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Chart 3: Correlation Heatmap
ax3 = axes[1, 0]
corr_matrix = returns[PORTFOLIO_TICKERS].corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='RdYlGn',
            center=0, vmin=-1, vmax=1, ax=ax3,
            square=True, linewidths=0.5,
            annot_kws={'size': 10, 'weight': 'bold'})
ax3.set_title('Stock Correlation Matrix\n(Green = Diversified, Red = Correlated)',
              fontweight='bold')

# Chart 4: Risk vs Return Scatter
ax4 = axes[1, 1]
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#3B1F2B']
for i, ticker in enumerate(PORTFOLIO_TICKERS):
    r = returns[ticker]
    c = (1 + r).cumprod()
    x = annualized_volatility(r) * 100
    y = annualized_return(c) * 100
    ax4.scatter(x, y, s=200, color=colors[i], zorder=5)
    ax4.annotate(ticker, (x, y),
                textcoords="offset points", xytext=(8, 5),
                fontsize=10, fontweight='bold')

# Add benchmark
bx = annualized_volatility(bench_returns) * 100
by = annualized_return(bench_cumulative) * 100
ax4.scatter(bx, by, s=250, color='black', marker='D', zorder=5)
ax4.annotate('S&P 500', (bx, by),
            textcoords="offset points", xytext=(8, 5),
            fontsize=10, fontweight='bold')

ax4.set_title('Risk vs Return by Stock\n(Higher Right = Better Risk-Adjusted Return)',
              fontweight='bold')
ax4.set_xlabel('Annualized Volatility (Risk %)')
ax4.set_ylabel('Annualized Return %')
ax4.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))
ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))
ax4.axhline(by, color='gray', linestyle=':', alpha=0.4)
ax4.axvline(bx, color='gray', linestyle=':', alpha=0.4)

plt.tight_layout()
plt.savefig('portfolio_performance.png', dpi=150,
            bbox_inches='tight', facecolor='white')
plt.show()
print("\nChart saved as portfolio_performance.png")

# ── MONTHLY RETURNS HEATMAP ────────────────────────────────
fig2, ax = plt.subplots(figsize=(14, 5))
monthly = port_returns.resample('ME').apply(
    lambda x: (1 + x).prod() - 1)
monthly_df = monthly.to_frame(name='Return')
monthly_df['Year']  = monthly_df.index.year
monthly_df['Month'] = monthly_df.index.strftime('%b')

pivot = monthly_df.pivot_table(
    values='Return', index='Year', columns='Month')
month_order = ['Jan','Feb','Mar','Apr','May','Jun',
               'Jul','Aug','Sep','Oct','Nov','Dec']
pivot = pivot.reindex(columns=[m for m in month_order if m in pivot.columns])

sns.heatmap(pivot * 100, annot=True, fmt='.1f',
            cmap='RdYlGn', center=0,
            linewidths=0.5, ax=ax,
            annot_kws={'size': 9},
            cbar_kws={'label': 'Monthly Return %'})
ax.set_title('Portfolio Monthly Returns Heatmap (%)\nGreen = Positive Month, Red = Negative Month',
             fontsize=14, fontweight='bold')
ax.set_xlabel('')
ax.set_ylabel('Year')

plt.tight_layout()
plt.savefig('monthly_returns_heatmap.png', dpi=150,
            bbox_inches='tight', facecolor='white')
plt.show()
print("Monthly heatmap saved as monthly_returns_heatmap.png")

print("\nAnalysis complete!")
print(f"Portfolio outperformed S&P 500: "
      f"{'YES' if p_ann_ret > b_ann_ret else 'NO'}")
print(f"Sharpe Ratio comparison: Portfolio {p_sharpe:.2f} vs "
      f"S&P 500 {b_sharpe:.2f}")
