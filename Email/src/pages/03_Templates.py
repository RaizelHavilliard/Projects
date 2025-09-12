import streamlit as st
import sqlite3

DB_FILE = "Email_manager.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

st.set_page_config(page_title="Templates", page_icon="📝")

st.title("📝 Manage Email Templates")

# --- Add New Template ---
st.subheader("➕ Add New Template")
with st.form("add_template_form"):
    title = st.text_input("Template Title")
    body = st.text_area("Template Body", height=200)
    submitted = st.form_submit_button("Add Template")
    if submitted:
        if title and body:
            conn = get_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO Templates (title, body) VALUES (?, ?)", (title, body))
                conn.commit()
                st.success("✅ Template added successfully!")
            except sqlite3.IntegrityError:
                st.error("❌ A template with this title already exists!")
            conn.close()
        else:
            st.warning("⚠️ Please fill in all fields.")

# --- View Templates ---
st.subheader("📋 All Templates")
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM Templates")
templates = cursor.fetchall()
conn.close()

if templates:
    for template in templates:
        temp_id, title, body = template
        with st.expander(f"{title}"):
            st.write(f"**Body:**\n\n{body}")

            # Update form
            with st.form(f"update_template_{temp_id}"):
                new_title = st.text_input("Edit Title", value=title)
                new_body = st.text_area("Edit Body", value=body, height=150)
                update_btn = st.form_submit_button("Update")
                if update_btn:
                    conn = get_connection()
                    cursor = conn.cursor()
                    try:
                        cursor.execute(
                            "UPDATE Templates SET title=?, body=? WHERE id=?",
                            (new_title, new_body, temp_id)
                        )
                        conn.commit()
                        st.success("✅ Template updated!")
                    except sqlite3.IntegrityError:
                        st.error("❌ A template with this title already exists!")
                    conn.close()
                    st.rerun()

            # Delete button
            if st.button("🗑️ Delete Template", key=f"delete_{temp_id}"):
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Templates WHERE id=?", (temp_id,))
                conn.commit()
                conn.close()
                st.warning(f"Template '{title}' deleted.")
                st.rerun()
else:
    st.info("No templates found. Add one above.")
