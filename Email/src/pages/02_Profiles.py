import streamlit as st
import sqlite3

DB_FILE = "Email_manager.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

st.set_page_config(page_title="Profiles", page_icon="👥")

st.title("👥 Manage Profiles")

# --- Add new profile ---
st.subheader("➕ Add New Profile")
with st.form("add_profile_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    title = st.text_input("Title")
    submitted = st.form_submit_button("Add Profile")
    if submitted:
        if name and email and title:
            conn = get_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO Profiles (name, email, title) VALUES (?, ?, ?)", (name, email, title))
                conn.commit()
                st.success("✅ Profile added successfully!")
            except sqlite3.IntegrityError:
                st.error("❌ This email already exists in profiles!")
            conn.close()
        else:
            st.warning("⚠️ Please fill in all fields.")

# --- View Profiles ---
st.subheader("📋 All Profiles")
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM Profiles")
profiles = cursor.fetchall()
conn.close()

if profiles:
    for profile in profiles:
        prof_id, name, email, title = profile
        with st.expander(f"{name} ({email})"):
            st.write(f"**Title:** {title}")

            # Update form inside expander
            with st.form(f"update_profile_{prof_id}"):
                new_name = st.text_input("Edit Name", value=name)
                new_email = st.text_input("Edit Email", value=email)
                new_title = st.text_input("Edit Title", value=title)
                update_btn = st.form_submit_button("Update")
                if update_btn:
                    conn = get_connection()
                    cursor = conn.cursor()
                    try:
                        cursor.execute(
                            "UPDATE Profiles SET name=?, email=?, title=? WHERE id=?",
                            (new_name, new_email, new_title, prof_id)
                        )
                        conn.commit()
                        st.success("✅ Profile updated!")
                    except sqlite3.IntegrityError:
                        st.error("❌ Email already exists in another profile.")
                    conn.close()
                    st.rerun()

            # Delete button
            if st.button("🗑️ Delete Profile", key=f"delete_{prof_id}"):
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Profiles WHERE id=?", (prof_id,))
                conn.commit()
                conn.close()
                st.warning(f"Profile {name} deleted.")
                st.rerun()
else:
    st.info("No profiles found. Add one above.")
