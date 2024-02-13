import streamlit as st
from services import *
import pandas as pd

def drugs_add():
    st.subheader("Add Drugs")
    col1, col2 = st.columns(2)

    with col1:
        drug_name = st.text_area("Enter the Drug Name")
        drug_expiry = st.date_input("Expiry Date of Drug (YYYY-MM-DD)")
        drug_mainuse = st.text_area("When to Use")
    with col2:
        drug_quantity = st.text_area("Enter the quantity")
        drug_id = st.text_area("Enter the Drug id (example:#D1)")

    if st.button("Add Drug"):
        drug_add_data(drug_name, drug_expiry, drug_mainuse, drug_quantity, drug_id)
        st.success("Successfully Added Data")

def drugs_view():
    st.subheader("Drug Details")
    drug_result = drug_view_all_data()
    with st.expander("View All Drug Data"):
        drug_clean_df = pd.DataFrame(drug_result, columns=["Name", "Expiry Date", "Use", "Quantity", "ID"])
        st.dataframe(drug_clean_df)
    with st.expander("View Drug Quantity"):
        drug_name_quantity_df = drug_clean_df[['Name', 'Quantity']]
        st.dataframe(drug_name_quantity_df)

def drugs_update():
    st.subheader("Update Drug Details")
    d_id = st.text_area("Drug ID")
    d_use = st.text_area("Drug Use")
    if st.button(label='Update'):
        drug_update(d_use, d_id)

def drugs_delete():
    st.subheader("Delete Drugs")
    did = st.text_area("Drug ID")
    if st.button(label="Delete"):
        drug_delete(did)

def customers_view():
    st.subheader("Customer Details")
    cust_result = customer_view_all_data()
    with st.expander("View All Customer Data"):
        cust_clean_df = pd.DataFrame(cust_result, columns=["Name", "Password", "Email-ID", "Area", "Number"])
        st.dataframe(cust_clean_df)

def customers_update():
    st.subheader("Update Customer Details")
    cust_email = st.text_area("Email")
    cust_number = st.text_area("Phone Number")
    if st.button(label='Update'):
        customer_update(cust_email, cust_number)

def customers_delete():
    st.subheader("Delete Customer")
    cust_email = st.text_area("Email")
    if st.button(label="Delete"):
        customer_delete(cust_email)

def orders_view():
    st.subheader("Order Details")
    order_result = order_view_all_data()
    with st.expander("View All Order Data"):
        order_clean_df = pd.DataFrame(order_result, columns=["Name", "Items", "Qty", "ID"])
        st.dataframe(order_clean_df)

def about():
    st.subheader("DBMS Mini Project")
    st.subheader("By Aditi (226), Anweasha (235) & Vijay (239)")

def admin():
    st.title("Pharmacy Database Dashboard")
    menu = ["Drugs", "Customers", "Orders", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Drugs":
        sub_menu = ["Add", "View", "Update", "Delete"]
        sub_choice = st.sidebar.selectbox("SubMenu", sub_menu)
        if sub_choice == "Add":
            drugs_add()
        elif sub_choice == "View":
            drugs_view()
        elif sub_choice == "Update":
            drugs_update()
        elif sub_choice == "Delete":
            drugs_delete()

    elif choice == "Customers":
        sub_menu = ["View", "Update", "Delete"]
        sub_choice = st.sidebar.selectbox("SubMenu", sub_menu)
        if sub_choice == "View":
            customers_view()
        elif sub_choice == "Update":
            customers_update()
        elif sub_choice == "Delete":
            customers_delete()

    elif choice == "Orders":
        sub_menu = ["View"]
        sub_choice = st.sidebar.selectbox("SubMenu", sub_menu)
        if sub_choice == "View":
            orders_view()

    elif choice == "About":
        about()

if __name__ == "__main__":
    admin()
