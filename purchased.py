import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
st.title("Purchased stock Management System")

def create_sample_data():
    purchase_data = {
        "Date": [datetime.date(2024, 12, 1), datetime.date(2024, 12, 2), datetime.date(2024, 12, 3)],
        "Amount": [ 100, 200, 300],
        "Item": ["", "", ""],
        "customer": ["", "", ""],
        "product": ["", "", ""]
    }
    purchase_df = pd.DataFrame(purchase_data)
    return purchase_df
    st.subheader("Updated Purchase Data")
    st.write(purchase_df)



def plot_sales_vs_purchase(purchase_df):
    plt.figure(figsize=(10, 6))
    plt.plot(purchase_df["Date"], purchase_df["Amount"], marker='o', label="Purchases", color='green')
    plt.title("Purchases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

def main():
    st.title("Purchases Dashboard")
    
    # Load sample data
    purchase_df = create_sample_data()
    
    # Display purchase data
    st.subheader("Purchase Data")
    st.write(purchase_df)

    # Plot sales vs purchase chart
    st.subheader("Purchases Chart")
    plot_sales_vs_purchase(purchase_df)

    # Adding new records
    st.subheader("Add a New Purchase")
    with st.form(key='purchase_form'):
        purchase_date = st.date_input("Purchase Date", datetime.date.today())
        purchase_amount = st.number_input("Purchase Amount", min_value=0)
        purchase_item = st.text_input("Item Purchased")
        customer = st.text_input("Customer")
        product = st.text_input("Product_Name")
        submit_purchase = st.form_submit_button("Add Purchase")
        if submit_purchase:
            new_purchase = pd.DataFrame({
                "Date": [purchase_date],
                "Amount": [purchase_amount],
                "Item": [purchase_item],
                "customer": [customer],
                "product": [product]
            })
            purchase_df = pd.concat([purchase_df, new_purchase], ignore_index=True)
            st.success("Purchase Added!")

    # Delete an item
    st.subheader("Delete a Purchase")
    if not purchase_df.empty:
        item_to_delete = st.selectbox("Select Item to Delete", purchase_df["Item"].unique())
        if st.button("Delete Item"):
            purchase_df = purchase_df[purchase_df["Item"] != item_to_delete]
            st.success(f"Item '{item_to_delete}' deleted!")
    else:
        st.warning("No items to delete.")

    # Display updated purchase data
    st.subheader("Updated Purchase Data")
    st.write(purchase_df)

    # Plot updated sales vs purchase chart
    st.subheader("Updated Purchases Chart")
    plot_sales_vs_purchase(purchase_df)

if __name__ == "__main__":
    main()