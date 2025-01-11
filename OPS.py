import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
st.title("Sale and Purchased stock Management System")
st.title("Main Dashboard") 

st.write("This is a dashboard to track sales and purchases over.") 

# Sample data for sales and purchases
def create_sample_data():
    sales_data = {
        "Date": [datetime.date(2024, 12, 1), datetime.date(2024, 12, 2), datetime.date(2024, 12, 3)],
        "Amount": [1000, 1500, 1300],
        "Item": ["Item1", "Item2", "Item3"],
        "customer" : ["customer", "customer", "customer"]
        
        
    }
    purchase_data = {
        "Date": [datetime.date(2024, 12, 1), datetime.date(2024, 12, 2), datetime.date(2024, 12, 3)],
        "Amount": [800, 1200, 1100],
        "Item": ["Item1", "Item2", "Item3"],
        "customer" : ["", "", ""]
    }

    sales_df = pd.DataFrame(sales_data)
    purchase_df = pd.DataFrame(purchase_data)

    return sales_df, purchase_df

# Plotting sales and purchase data
def plot_sales_vs_purchase(sales_df, purchase_df):
    plt.figure(figsize=(10, 6))

    # Plot Sales
    plt.plot(sales_df["Date"], sales_df["Amount"], marker='o', label="Sales", color='red')

    # Plot Purchases
    plt.plot(purchase_df["Date"], purchase_df["Amount"], marker='o', label="Purchases", color='green')

    plt.title("Sales vs Purchases old Stock")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

# Main function to run the Streamlit app
def main():
    # Title for the web app
    st.title("Sales and Purchases Dashboard")
    
    # Load sample data
    sales_df, purchase_df = create_sample_data()
    
    # Display sales data
    st.subheader("Sales Data")
    st.write(sales_df)

    # Display purchase data
    st.subheader("Purchase Data")
    st.write(purchase_df)

    # Plot sales vs purchase chart
    st.subheader("Sales vs Purchases Chart")
    plot_sales_vs_purchase(sales_df, purchase_df)

    # Adding new records
    st.subheader("Sale or Purchase")
    
    # Option to add new sale
    with st.form(key='sale_form'):
        sale_date = st.date_input("Sale Date", datetime.date.today())
        sale_amount = st.number_input("Sale Amount", min_value=0)
        sale_item = st.text_input("Item Sold")
        customer = st.text_input("Customer")
        submit_sale = st.form_submit_button("Add Sale")
        if submit_sale:
            new_sale = pd.DataFrame({
                "Date": [sale_date],
                "Amount": [sale_amount],
                "Item": [sale_item],
                "name": [customer]
            })
            sales_df = pd.concat([sales_df, new_sale], ignore_index=True)
            st.success("Sale Added!")

    # Option to add new purchase
    with st.form(key='purchase_form'):
        purchase_date = st.date_input("Purchase Date", datetime.date.today())
        purchase_amount = st.number_input("Purchase Amount", min_value=0)
        purchase_item = st.text_input("Item Purchased")
        customer = st.text_input("Customer")
        submit_purchase = st.form_submit_button("Add Purchase")
        if submit_purchase:
            new_purchase = pd.DataFrame({
                "Date": [purchase_date],
                "Amount": [purchase_amount],
                "Item": [purchase_item],
                "name": [customer]
            })
            purchase_df = pd.concat([purchase_df, new_purchase], ignore_index=True)
            st.success("Purchase Added!")

    # Update the sales and purchase chart after new data
    st.subheader("Updated Sales vs Purchases Chart")
    plot_sales_vs_purchase(sales_df, purchase_df)

if __name__ == "__main__":
    main()
