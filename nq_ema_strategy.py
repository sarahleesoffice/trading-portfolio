import yfinance as yf import pandas as pd import numpy as np import matplotlib 
matplotlib.use('TkAgg') import matplotlib.pyplot as plt # Configuration - NQ SETUP TICKER = "QQQ"  
# QQQ tracks NASDAQ-100 (NQ equivalent) FAST_EMA = 50 SLOW_EMA = 200 INTERVAL = "1h"  # Change to 
"4h" if you want 4-hour chart PERIOD = "60d" # Risk Management Settings FIXED_STOP_PERCENT = 0.02 # 
2% stop loss for Method 2 RISK_REWARD_RATIO = 2 # 2R target for Method 2 SWING_LOOKBACK = 20 # Look 
back 20 bars for swing highs/lows print(f"Downloading {TICKER} data ({INTERVAL} chart)...") ticker 
= yf.Ticker(TICKER) data = ticker.history(period=PERIOD, interval=INTERVAL) # Calculate EMAs 
data['EMA_50'] = data['Close'].ewm(span=FAST_EMA, adjust=False).mean() data['EMA_200'] = 
data['Close'].ewm(span=SLOW_EMA, adjust=False).mean() # Find swing highs and lows 
data['Swing_High'] = data['High'].rolling(window=SWING_LOOKBACK, center=True).max()
data['Swing_Low'] = data['Low'].rolling(window=SWING_LOOKBACK, center=True).min()

# Generate entry signals
data['Signal'] = 0
data.loc[data['EMA_50'] > data['EMA_200'], 'Signal'] = 1
data.loc[data['EMA_50'] < data['EMA_200'], 'Signal'] = -1
data['Position'] = data['Signal'].diff()

# Find all Golden Cross entries
golden_crosses = data[data['Position'] == 2].copy()

# Simulate trades for both methods
trades_method1 = []  # Swing High/Low
trades_method2 = []  # Fixed 2R

for entry_time in golden_crosses.index:
    entry_price = data.loc[entry_time, 'Close']
    entry_idx = data.index.get_loc(entry_time)
    
    # METHOD 1: Swing High/Low
    # Stop: Most recent swing low before entry
    recent_swing_low = data.loc[:entry_time, 'Swing_Low'].dropna().iloc[-1] if len(data.loc[:entry_time, 'Swing_Low'].dropna()) > 0 else entry_price * 0.95
    # Target: Most recent swing high before entry
    recent_swing_high = data.loc[:entry_time, 'Swing_High'].dropna().iloc[-1] if len(data.loc[:entry_time, 'Swing_High'].dropna()) > 0 else entry_price * 1.10
    
    stop1 = recent_swing_low
    target1 = recent_swing_high
    risk1 = entry_price - stop1
    reward1 = target1 - entry_price
    rr1 = reward1 / risk1 if risk1 > 0 else 0
    
    # METHOD 2: Fixed 2R
    stop2 = entry_price * (1 - FIXED_STOP_PERCENT)
    risk2 = entry_price - stop2
    target2 = entry_price + (risk2 * RISK_REWARD_RATIO)
    
    # Check what happened after entry
    future_data = data.iloc[entry_idx+1:entry_idx+100]  # Look ahead 100 bars
    
    # Method 1 outcome
    hit_stop1 = (future_data['Low'] <= stop1).any()
    hit_target1 = (future_data['High'] >= target1).any()
    
    if hit_stop1 and hit_target1:
        # Which




