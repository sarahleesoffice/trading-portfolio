import yfinance as yf
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # This fixes the Mac display issue
import matplotlib.pyplot as plt

print("Downloading Apple stock data...")
ticker = yf.Ticker("AAPL")
data = ticker.history(period="1y")

data['Daily_Return'] = data['Close'].pct_change() * 100

print("\n--- Apple Stock Summary (Last Year) ---")
print(f"Starting Price: ${data['Close'].iloc[0]:.2f}")
print(f"Ending Price: ${data['Close'].iloc[-1]:.2f}")
print(f"Average Daily Return: {data['Daily_Return'].mean():.2f}%")
print(f"Highest Price: ${data['Close'].max():.2f}")
print(f"Lowest Price: ${data['Close'].min():.2f}")

# Create the chart
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label='AAPL Closing Price', color='blue', linewidth=2)
plt.title('Apple Stock Price - Last Year', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the chart as a file
plt.savefig('apple_stock_chart.png', dpi=300, bbox_inches='tight')
print("\n✅ Chart saved as 'apple_stock_chart.png'")

# Display the chart
plt.show()

print("✅ Script complete!")
