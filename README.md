 # Exchange Rate Analysis

This Python script retrieves historical exchange rates from the [Exchange Rates API](https://exchangeratesapi.io/) for the Australian Dollar (AUD) to the New Zealand Dollar (NZD). 

It fetches exchange rates for a specified date range provided in command line arguments, plots the exchange rates over time, and calculates statistics such as maximum, minimum, and average exchange rates.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `pandas`, `numpy`, `matplotlib`

## Usage : Run in Local Environment

1. Ensure you have Python 3.x installed on your system.
2. Install the required Python packages using pip:

```bash
pip install requests pandas numpy matplotlib
```

3. Setup environment varibale named `EXCHANGE_API_KEY`
4. Run the script using a Python environment by prividing start_date, end_date parameters:

```bash 
python exchange_rate_analysis.py --start_date 2024-05-01 --end_date 20204-5-31
```

# Description
The script defines two main functions:

1. get_exchange_rates(start_date, end_date, access_key): Retrieves historical exchange rates for AUD to NZD from the Exchange Rates API.
2. plot_exchange_rates(conversion_rates): Plots the historical exchange rates over time and highlights the minimum, maximum, and average rates.
3. The main() function orchestrates the execution of the script. It retrieves exchange rates, converts them to a DataFrame, plots the rates, and calculates statistics.


# Output

1. The script prints a DataFrame containing the retrieved exchange rates along with additional columns for currency_date (converted to datetime) and imported_date (current datetime).
2. It plots the historical exchange rates over time and highlights the minimum, maximum, and average rates.
3. Finally, it calculates and prints the maximum, minimum, and average exchange rates for the specified date range.

# Example output

```bash

DataFrame:
          date     value currency_date              imported_date
0   2024-05-01  1.101557    2024-05-01 2024-05-31 02:11:48.053899
1   2024-05-02  1.101918    2024-05-02 2024-05-31 02:11:48.053899
2   2024-05-03  1.098411    2024-05-03 2024-05-31 02:11:48.053899
3   2024-05-04  1.098910    2024-05-04 2024-05-31 02:11:48.053899
4   2024-05-05  1.100169    2024-05-05 2024-05-31 02:11:48.053899
5   2024-05-06  1.102288    2024-05-06 2024-05-31 02:11:48.053899
6   2024-05-07  1.098797    2024-05-07 2024-05-31 02:11:48.053899
7   2024-05-08  1.095443    2024-05-08 2024-05-31 02:11:48.053899
8   2024-05-09  1.096649    2024-05-09 2024-05-31 02:11:48.053899
9   2024-05-10  1.100075    2024-05-10 2024-05-31 02:11:48.053899
10  2024-05-11  1.101736    2024-05-11 2024-05-31 02:11:48.053899
11  2024-05-12  1.096807    2024-05-12 2024-05-31 02:11:48.053899
12  2024-05-13  1.097637    2024-05-13 2024-05-31 02:11:48.053899
13  2024-05-14  1.096201    2024-05-14 2024-05-31 02:11:48.053899
14  2024-05-15  1.092819    2024-05-15 2024-05-31 02:11:48.053899
15  2024-05-16  1.091075    2024-05-16 2024-05-31 02:11:48.053899
16  2024-05-17  1.092688    2024-05-17 2024-05-31 02:11:48.053899
17  2024-05-18  1.093014    2024-05-18 2024-05-31 02:11:48.053899
18  2024-05-19  1.091956    2024-05-19 2024-05-31 02:11:48.053899
19  2024-05-20  1.092384    2024-05-20 2024-05-31 02:11:48.053899
20  2024-05-21  1.094129    2024-05-21 2024-05-31 02:11:48.053899
21  2024-05-22  1.085145    2024-05-22 2024-05-31 02:11:48.053899
22  2024-05-23  1.082739    2024-05-23 2024-05-31 02:11:48.053899
23  2024-05-24  1.081986    2024-05-24 2024-05-31 02:11:48.053899
24  2024-05-25  1.083395    2024-05-25 2024-05-31 02:11:48.053899
25  2024-05-26  1.082097    2024-05-26 2024-05-31 02:11:48.053899
26  2024-05-27  1.081857    2024-05-27 2024-05-31 02:11:48.053899
27  2024-05-28  1.082661    2024-05-28 2024-05-31 02:11:48.053899
28  2024-05-29  1.081850    2024-05-29 2024-05-31 02:11:48.053899
29  2024-05-30  1.084048    2024-05-30 2024-05-31 02:11:48.053899

Maximum Exchange Rate: 1.102288 (Date: 2024-05-06)
Minimum Exchange Rate: 1.08185 (Date: 2024-05-29)
Average Exchange Rate: 1.09
```

![image](https://github.com/pavanerravelli/ExchangeRateAnalysys/assets/171128460/3a9df6ee-bf0d-4ef4-80e7-c329e3ac31e1)


#License

This project is licensed under the MIT License - see the LICENSE file for details.
