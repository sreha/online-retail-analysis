import pandas as pd
import os

def load_and_clean_data():
    """
    Loads and cleans the Online Retail dataset:
    - Drops rows without CustomerID
    - Removes cancelled orders (InvoiceNo starts with 'C')
    - Filters only valid transactions (positive Quantity and UnitPrice)
    - Creates a TotalPrice column
    - Converts InvoiceDate to datetime
    - Casts CustomerID to string

    Returns:
        pandas.DataFrame: Cleaned dataset
    """
    # Define the relative path to the Excel file
    data_path = os.path.join("..", "data", "Online_Retail.xlsx")

    # Load dataset
    df = pd.read_excel(data_path)

    # Drop rows with missing CustomerID
    df = df.dropna(subset=["CustomerID"])

    # Remove cancelled transactions
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

    # Keep only valid positive transactions
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    # Create TotalPrice column
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    # Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Cast CustomerID to string for consistency
    df["CustomerID"] = df["CustomerID"].astype(str)

    return df

# Optional: for standalone testing
if __name__ == "__main__":
    df = load_and_clean_data()
    print("✅ Data loaded and cleaned. Shape:", df.shape)
    
df.to_csv("../data/cleaned_online_retail.csv", index=False)
