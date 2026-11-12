import streamlit as st
from Gymview import GymMemberManagement

donor_instance =GymMemberManagement()
tab1 ,tab2 =st.tabs(["Add Member","View Member"])

with tab1:
    st.header("Add New Member.....!")
    name =st.text_input("Enter the Member Name")
    place =st.text_input("Enter the Member Place")
    mobile =st.text_input("Enter Member Phone Number")
    plan =st.selectbox("Select Plan" ,["8 month","1 month","3 month","9 month ","6 month","5 month"])
    fee =st.text_input("Enter Fee")
    last_donation =st.date_input("Enter Last Donation Date")
    if st.button("Submit"):
        donor_instance.post(name=name ,place=place,mobile=mobile,plan=plan,fee=fee,last_donation=last_donation)
        st.success("Member Installed Sucessfully....!")
    
with tab2:
    st.header("View Member Details.....!")    