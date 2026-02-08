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

### 3. [Macro Liquidity Sweep Backtester](https://github.com/sarahleesoffice/Macro_Liquidity_Sweep-_Backtester)

A quantitative backtesting engine that tests **macro liquidity sweep setups** on NQ (Nasdaq E-mini Futures) across 4 years of 1-minute data on a simulated **$100K FTMO prop firm account**.

The goal: find the optimal combination of **time window + news catalyst** that produces the highest win rate.

#### Strategy Logic

```
Liquidity Sweep  →  Market Structure Shift (MSS)  →  Fair Value Gap (FVG) Entry
```

1. **Sweep** — Price wicks beyond a key swing level (multi-timeframe) to grab liquidity, then closes back inside
2. **MSS** — Displacement candle breaks recent structure in the opposite direction, confirming the reversal
3. **FVG** — Fair Value Gap forms after the MSS; entry is placed at the gap
4. **SL** — 3 handles below/above the sweep candle
5. **TP** — Nearest swing body on the other side of the trade

All setups require a minimum 1:1 risk-reward ratio.

#### Research Design

**Phase 1 — Time Window Analysis**

| Window | Time (EST) | Description |
|--------|-----------|-------------|
| **A** | 8:30 – 9:10 | Pre-Market / News |
| **B** | 9:30 – 10:00 | Silver Bullet |
| **C** | 10:00 – 11:00 | NY AM Session |

**Phase 2 — News Catalyst Cross-Reference**

Each window is cross-referenced with economic events (CPI, NFP, FOMC, Core PCE, etc.) to find which news + time combinations produce the highest probability setups.

#### Results (409 trades, Jan 2022 – Dec 2025)

| Window | Win Rate | Profit Factor | Trades |
|--------|----------|--------------|--------|
| **A** | 60.7% | 3.16 | 183 |
| **B** | 49.4% | 2.47 | 77 |
| **C** | 38.3% | 1.32 | 149 |

**Overall**: 50.4% WR | $259.72 expectancy per trade | Avg Win $948 vs Avg Loss $439 (2.16:1)

**FTMO Compliant**: Max drawdown $1,154 | Max daily loss $1,291

**Top combos:**
- Window A + No-News days → **71% win rate**
- Window A + CPI days → **75% win rate**
- Window A + Core PCE days → **75% win rate**

#### Project Structure

```
├── ict_2022_backtest.py        # Main backtest engine (bar-by-bar simulation)
├── download_data.py            # Downloads QQQ 1-min data from Alpaca or Polygon.io
├── generate_news_calendar.py   # Generates news_calendar.csv (FOMC, CPI, NFP, etc.)
├── news_calendar.csv           # 1,636 economic events (2022-2025)
└── .gitignore
```

#### Data

Uses **QQQ** (Nasdaq 100 ETF) as a free proxy for NQ futures, scaled **x40** to NQ price levels at load time.

- **Source**: Alpaca Markets (free tier) or Polygon.io
- **Bars**: 855,796 one-minute candles
- **Period**: January 2022 – December 2025
- **Trading Days**: 1,003

#### Risk Management (FTMO Rules)

| Parameter | Value |
|-----------|-------|
| Risk per trade | 0.5% ($500) |
| Max drawdown | $10,000 (from starting balance) |
| Max daily loss | $5,000 |
| Max daily attempts | 3 |
| Position sizing | Flat (from starting balance, no compounding) |
| Daily rule | Stop after first win ("one and done") |

#### Key Technical Details

- **Multi-timeframe swing detection** — Resamples 1m data to 5m / 15m / 1h / 4h and identifies swing highs/lows on each timeframe
- **Bar-by-bar simulation** — No vectorized shortcuts; trades are managed tick-by-tick with realistic SL/TP fills
- **Timezone handling** — Properly handles EST/EDT transitions with UTC-first parsing
- **Sweep cooldown** — 20-bar minimum between same-direction sweeps to prevent duplicate entries
- **Nearest TP targeting** — Collects all valid swing targets and selects the nearest one (not most recent)

- **Skills**: Quantitative Research, Backtesting, Futures Trading, Risk Management, Price Action

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
- Built full macro liquidity sweep backtester across 4 years / 409 trades with 60.7% win rate on best window
- Identified highest-probability time window + news catalyst combinations through quantitative research

## Background
Preparing for quantitative trading internships at firms like Citadel, Jane Street, and Two Sigma. Building practical experience with algorithmic trading, risk management, and data analysis.

## Contact
sarah.m.lee.office@gmail.com
