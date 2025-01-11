import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
st.title("Sale stock Management System")

# Sample data for sales and purchases
def create_sample_data():
    sales_data = {
        "Date": [datetime.date(2024, 12, 1), datetime.date(2024, 12, 2), datetime.date(2024, 12, 3)],
        "Amount": [1000, 1500, 1300],
        "Item": ["Item1", "Item2", "Item3"],
        "Customer": ["customer1", "customer2", "customer3"]
    }
    sales_df = pd.DataFrame(sales_data)
    return sales_df

# Plotting sales and purchase data
def plot_sales_vs_purchase(sales_df):
    plt.figure(figsize=(10, 6))
    plt.plot(sales_df["Date"], sales_df["Amount"], marker='o', label="Sales", color='red')
    plt.title("Sales vs Purchases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

def main():
    # Title for the web app
    st.title("Sales  Dashboard")
    
    # Load sample data
    if 'sales_df' not in st.session_state:
        st.session_state.sales_df = create_sample_data()
    
    # Display sales data
    st.subheader("Sales Data")
    st.write(st.session_state.sales_df)

    # Plot sales vs purchase chart
    st.subheader("Sales vs Purchases Chart")
    plot_sales_vs_purchase(st.session_state.sales_df)

    # Adding new records
    st.subheader("Add a New Sale or Purchase")
    
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
                "Customer": [customer]
            })
            st.session_state.sales_df = pd.concat([st.session_state.sales_df, new_sale], ignore_index=True)
            st.success("Sale Added!")

    # Option to delete an item
    st.subheader("Delete an Item")
    with st.form(key='delete_form'):
        item_to_delete = st.text_input("Enter the Item Name to Delete")
        submit_delete = st.form_submit_button("Delete Item")
        if submit_delete:
            if item_to_delete in st.session_state.sales_df['Item'].values:
                st.session_state.sales_df = st.session_state.sales_df[st.session_state.sales_df['Item'] != item_to_delete]
                st.success(f"Item '{item_to_delete}' Deleted!")
            else:
                st.error(f"Item '{item_to_delete}' not found!")

    # Display updated sales data
    st.subheader("Updated Sales Data")
    st.write(st.session_state.sales_df)

    # Plot updated sales vs purchase chart
    st.subheader("Updated Sales vs Purchases Chart")
    plot_sales_vs_purchase(st.session_state.sales_df)

if __name__ == "__main__":
    main()