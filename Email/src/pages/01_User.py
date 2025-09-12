import streamlit as st
from utils.helpers import insert, fetch, update, delete 

st.title("User Profile Management")


st.subheader("Add New User")
with st.form("add_user_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
        email = st.text_input("Email")
    with col2:    
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Add User", use_container_width=True)
        
    if submitted:
        if name and email and password:
            insert("UserProfile", {"name": name, "email": email, "password": password})
            st.success(f"User {name} added successfully!")
        else:
            st.error("Please fill in all fields.")


st.subheader("Existing Users")
users = fetch("UserProfile")

if users:
    for u in users:
        st.write(f"ID: {u[0]}, Name: {u[1]}, Email: {u[2]}")
        col1, col2 = st.columns(2)

        # Update button
        if col1.button(f"Update {u[1]}", key=f"update_{u[0]}"):
            with st.form(f"update_form_{u[0]}"):
                new_name = st.text_input("New Name", value=u[1])
                new_email = st.text_input("New Email", value=u[2])
                new_password = st.text_input("New Password", type="password", value=u[3])
                update_submitted = st.form_submit_button("Update")
                if update_submitted:
                    update("UserProfile", {"name": new_name, "email": new_email, "password": new_password}, {"id": u[0]})
                    st.success(f"User {new_name} updated!")

        # Delete button
        if col2.button(f"Delete {u[1]}", key=f"delete_{u[0]}"):
            delete("UserProfile", {"id": u[0]})
            st.warning(f"User {u[1]} deleted!")
else:
    st.info("No users found.")
