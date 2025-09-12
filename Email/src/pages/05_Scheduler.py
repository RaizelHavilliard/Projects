import streamlit as st
import sqlite3
from datetime import datetime

DB_FILE = "Email_manager.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

st.set_page_config(page_title="Scheduler", page_icon="⏰")
st.title("⏰ Email Scheduler")

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

# --- Schedule Form ---
st.subheader("📅 Schedule a New Email")

with st.form("schedule_email_form"):
    sender = st.selectbox("Sender", options=users, format_func=lambda u: f"{u[1]} ({u[2]})")
    recipient = st.selectbox("Recipient", options=profiles, format_func=lambda p: f"{p[1]} <{p[2]}>")
    template_choice = st.selectbox("Template (Optional)", ["None"] + [t[1] for t in templates])
    
    subject = st.text_input("Subject")
    body_default = ""
    if template_choice != "None":
        body_default = [t for t in templates if t[1] == template_choice][0][2]
    body = st.text_area("Body", value=body_default)

    date = st.date_input("📅 Date", datetime.now().date())
    time = st.time_input("⏰ Time", datetime.now().time())
    scheduled_for = datetime.combine(date, time)


    submitted = st.form_submit_button("Schedule Email")
    if submitted:
        if subject and body:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Schedules (sender_id, recipient_id, subject, body, scheduled_for)
                VALUES (?, ?, ?, ?, ?)
            """, (sender[0], recipient[0], subject, body, scheduled_for.isoformat()))
            conn.commit()
            conn.close()
            st.success(f"✅ Email scheduled for {scheduled_for}!")
        else:
            st.error("❌ Subject and body are required.")

# --- View Scheduled Emails ---
st.subheader("📋 Scheduled Emails")
conn = get_connection()
cursor = conn.cursor()
cursor.execute("""
    SELECT S.id, U.name, P.name, S.subject, S.scheduled_for, S.status
    FROM Schedules S
    JOIN UserProfile U ON S.sender_id = U.id
    JOIN Profiles P ON S.recipient_id = P.id
    ORDER BY S.scheduled_for
""")
rows = cursor.fetchall()
conn.close()

if rows:
    for r in rows:
        sched_id, sender_name, recipient_name, subject, scheduled_for, status = r
        with st.expander(f"📌 {subject} → {recipient_name} (at {scheduled_for})"):
            st.write(f"**Sender:** {sender_name}")
            st.write(f"**Recipient:** {recipient_name}")
            st.write(f"**Status:** {status}")
            if st.button("🗑️ Cancel", key=f"cancel_{sched_id}"):
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Schedules WHERE id=?", (sched_id,))
                conn.commit()
                conn.close()
                st.warning("❌ Scheduled email canceled.")
                st.rerun()
else:
    st.info("No scheduled emails found.")
