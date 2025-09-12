import streamlit as st
import sqlite3
import yagmail
from datetime import datetime

DB_FILE = "Email_manager.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

st.set_page_config(page_title="Send Email", page_icon="📧")
st.title("📧 Send an Email")

# --- Fetch data ---
def fetch_all(table):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    conn.close()
    return rows

users = fetch_all("UserProfile")
profiles = fetch_all("Profiles")
templates = fetch_all("Templates")

# --- Choose sender (UserProfile) ---
st.subheader("Step 1: Choose Sender Account")
if not users:
    st.warning("⚠️ No user profile found. Please add one first.")
else:
    sender = st.selectbox("Select Sender", options=users, format_func=lambda u: f"{u[1]} ({u[2]})")

# --- Choose recipient (Profiles) ---
st.subheader("Step 2: Choose Recipient")
if not profiles:
    st.warning("⚠️ No profiles found. Please add one first.")
else:
    recipient = st.selectbox("Select Recipient", options=profiles, format_func=lambda p: f"{p[1]} <{p[2]}>")

# --- Choose template (optional) ---
st.subheader("Step 3: Choose Template (Optional)")
template_choice = st.selectbox("Select Template", ["None"] + [t[1] for t in templates])
selected_template = None
if template_choice != "None":
    selected_template = [t for t in templates if t[1] == template_choice][0]
    st.info(f"Loaded template:\n\n{selected_template[2]}")

# --- Write Email ---
st.subheader("Step 4: Write Your Email")
subject = st.text_input("Subject")
body = st.text_area("Body", value=selected_template[2] if selected_template else "")

# --- Send Email ---
if st.button("🚀 Send Email"):
    if not (users and profiles):
        st.error("❌ You must have at least one sender and one recipient.")
    elif not subject or not body:
        st.error("❌ Subject and body are required.")
    else:
        sender_email = sender[2]
        sender_password = sender[3]  # stored in UserProfile
        recipient_email = recipient[2]

        try:
            yag = yagmail.SMTP(user=sender_email, password=sender_password)
            yag.send(to=recipient_email, subject=subject, contents=body)

            # Save to History
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO History (destination, subject, body, sent_at) VALUES (?, ?, ?, ?)",
                (recipient_email, subject, body, datetime.now().isoformat())
            )
            conn.commit()
            conn.close()

            st.success(f"✅ Email sent to {recipient_email} successfully!")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")
