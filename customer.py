from services import *
import random 
import pandas as pd

def customer(username, password):
    
    print("In Customer")
    st.title("Welcome to Pharmacy Store")

    st.subheader("Your Order Details")
    order_result = order_view_data(username)
    # st.write(cust_result)
    with st.expander("View All Order Data"):
        order_clean_df = pd.DataFrame(order_result, columns=["Name", "Items", "Qty", "ID"])
        st.dataframe(order_clean_df)

    drugs = drug_view_all_data()
    print(drugs)
    orders = []
    for i,drug in enumerate(drugs):
        print(drug)
        st.subheader(f"Drug: {drug[0]}")
        orders.append(drug[i])
        orders[i] = st.slider(label="Quantity",min_value=0, max_value=10, key= i)
        st.info("When to USE: " + str(drug[2]))
    
    if st.button(label="Buy Now"):
        O_Qty = ""
        for i in len(orders):
            if orders[i]>0:
                O_items+= drug[i][0]
            O_Qty += (str(orders[i]) + ',')
        O_id = username + "#O" + str(random.randint(0,1000000))
        order_add_data(username, O_items, O_Qty, O_id)
            

