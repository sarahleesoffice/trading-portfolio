# Quantitative Trading Portfolio

Python-based trading strategies and analysis tools for equity and futures markets.

## Projects

### 1. Stock Price Tracker (`stock_tracker_chart.py`)
- Downloads real-time stock data using yfinance API
- Calculates daily returns and statistical metrics  
- Generates professional price charts with matplotlib
- **Skills**: Python, Pandas, Data Visualization

![Apple Stock Chart](apple_stock_chart.png)

### 2. NQ EMA Strategy (`nq_visual.py`, `nq_ema_strategy.py`)
- 50/200 EMA crossover strategy on NASDAQ-100 (QQQ) 1-hour timeframe
- **Tested two risk management approaches:**
  - **Method 1 (Swing High/Low)**: 100% win rate, +1.99% return (3 trades)
  - **Method 2 (Fixed 2R)**: 0% win rate, -2.57% return (3 trades)
- **Key Finding**: Swing high/low targets significantly outperformed fixed percentage targets, suggesting that NQ price action respects technical support/resistance levels more reliably than arbitrary percentage-based stops
- Includes automated entry signals, stop loss placement, and take profit targeting
- **Skills**: Risk Management, Backtesting, Futures Trading, Technical Analysis

![NQ Strategy Chart](nq_chart.png)

### 3. [Macro Liquidity Sweep Backtester](https://github.com/sarahleesoffice/Macro_Liquidity_Sweep-_Backtester) (`ict_2022_backtest.py`)
- Full ICT 2022 Model backtester: **Liquidity Sweep → MSS → FVG entry** on NQ futures
- Bar-by-bar simulation across **4 years of 1-minute data** (855K bars, 2022–2025)
- Multi-timeframe swing detection (5m / 15m / 1h / 4h) via pandas resampling
- **Phase 1**: Tests 3 time windows — Window A (8:30–9:10) achieved **60.7% win rate, 3.16 profit factor**
- **Phase 2**: Cross-references windows with news catalysts (CPI, NFP, FOMC) — best combo: **Window A + CPI days → 75% win rate**
- FTMO $100K prop firm compliant: 0.5% risk, $10K max DD, daily loss circuit breaker
- **409 trades | 50.4% WR | $259 expectancy/trade | Avg Win $948 vs Avg Loss $439 (2.16:1 R:R)**
- **Skills**: Quantitative Research, Backtesting, Futures Trading, Risk Management, ICT Price Action

## Technologies Used
- **Python 3.13**
- **yfinance** - Real-time market data
- **Pandas** - Time series data manipulation & multi-timeframe resampling
- **Matplotlib** - Professional chart generation
- **Plotly** - Interactive HTML equity curves
- **NumPy** - Numerical computing
- **Alpaca API** - Historical 1-minute market data

## Setup & Usage
```bash
# Install dependencies
pip3 install yfinance pandas matplotlib numpy

# Run stock tracker
python3 stock_tracker_chart.py

# Run NQ strategy analysis
python3 nq_ema_strategy.py
```

## Key Results
- Developed working backtesting framework for strategy validation
- Achieved 100% win rate on swing-based stop loss methodology
- Demonstrated ability to compare multiple approaches and select optimal solution
- Built full ICT 2022 Model backtester across 4 years / 409 trades with 60.7% win rate on best window
- Identified highest-probability time window + news catalyst combinations through quantitative research

## Background
Preparing for quantitative trading internships at firms like Citadel, Jane Street, and Two Sigma. Building practical experience with algorithmic trading, risk management, and data analysis.

## Contact
sarah.m.lee.office@gmail.com
