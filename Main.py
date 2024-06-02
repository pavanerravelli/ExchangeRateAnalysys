import os
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta
 
def get_exchange_rates(start_date, end_date, access_key):
    conversion_rates = []
    delta = timedelta(days=1)
   
    while start_date <= end_date:
        api_url = f"https://api.exchangeratesapi.io/v1/{start_date}?access_key={access_key}&base=AUD&symbols=NZD"
       
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (e.g., 404, 500)
            data = response.json()
            if data.get("rates") and data.get("rates").get("NZD"):
                conversion_rates.append({"date": data.get("date"), "value": data.get("rates").get("NZD")})
            else:
                print(f"No data available for {start_date}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {start_date}: {e}")
       
        start_date += delta
   
    return conversion_rates
 
def plot_exchange_rates(conversion_rates):
    dates = [data["date"] for data in conversion_rates]
    values = [data["value"] for data in conversion_rates]
    min_rate = min(conversion_rates, key=lambda x: x['value'])
    max_rate = max(conversion_rates, key=lambda x: x['value'])
    average_rate = np.mean(values)
   
    plt.figure(figsize=(12, 6))
    plt.plot(dates, values, marker='o', linestyle='-', label='Exchange Rate')
    plt.axhline(y=min_rate['value'], color='r', linestyle='--', label=f'Min Rate ({min_rate["date"]})')
    plt.axhline(y=max_rate['value'], color='g', linestyle='--', label=f'Max Rate ({max_rate["date"]})')
    plt.axhline(y=average_rate, color='b', linestyle='--', label=f'Average Rate ({average_rate:.2f})')
   
    plt.title('Historical Exchange Rates (AUD to NZD)')
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
 
def main():
    access_key = os.environ.get('EXCHANGE_API_KEY')  # Read access key from environment variable
    if not access_key:
        print("Access key not found. Please set the 'EXCHANGE_API_KEY' environment variable.")
        return
    
    start_date = date(2024, 5, 1)
    end_date = date(2024, 5, 30)
 
    conversion_rates = get_exchange_rates(start_date, end_date, access_key)
   
    if conversion_rates:
        # Convert conversion_rates to a DataFrame
        df = pd.DataFrame(conversion_rates)
        print("DataFrame:")
        print(df)
       
        # Plot exchange rates
        plot_exchange_rates(conversion_rates)
       
        # Calculate and print max, min, and average exchange rates
        max_rate = max(conversion_rates, key=lambda x: x['value'])
        min_rate = min(conversion_rates, key=lambda x: x['value'])
        average_rate = np.mean([data['value'] for data in conversion_rates])
        print(f"Maximum Exchange Rate: {max_rate['value']} (Date: {max_rate['date']})")
        print(f"Minimum Exchange Rate: {min_rate['value']} (Date: {min_rate['date']})")
        print(f"Average Exchange Rate: {average_rate:.2f}")
       
    else:
        print("No valid data available.")
 
if __name__ == "__main__":
    main()
