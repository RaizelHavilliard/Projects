import streamlit as st
import sqlite3

DB_FILE = "Email_manager.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

st.set_page_config(page_title="History", page_icon="📜")
st.title("📜 Email History")

# --- Fetch history ---
conn = get_connection()
cursor = conn.cursor()
cursor.execute("""
    SELECT id, destination, subject, body, sent_at 
    FROM History
    ORDER BY sent_at DESC
""")
rows = cursor.fetchall()
conn.close()

if rows:
    for r in rows:
        hist_id, destination, subject, body, sent_at = r
        with st.expander(f"📧 {subject} → {destination} ({sent_at})"):
            st.write(f"**Destination:** {destination}")
            st.write(f"**Subject:** {subject}")
            st.write(f"**Body:**\n\n{body}")
            st.write(f"**Sent At:** {sent_at}")

            # Delete option
            if st.button("🗑️ Delete", key=f"delete_{hist_id}"):
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM History WHERE id=?", (hist_id,))
                conn.commit()
                conn.close()
                st.warning("❌ History entry deleted.")
                st.rerun()
else:
    st.info("No history found yet. Send an email to see it here.")
