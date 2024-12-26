from fetch_data import fetch_shale_oil_data
from analysis import generate_shale_oil_report

def main():
    # Define tickers for Shale Oil companies
    tickers = ["EOG", "PXD"]
    
    # Fetch stock data
    shale_data = fetch_shale_oil_data(tickers)
    
    # Generate the report
    if shale_data:
        report = generate_shale_oil_report(shale_data)
        print(report)
    else:
        print("No valid data available for Shale Oil companies.")

if __name__ == "__main__":
    main()
