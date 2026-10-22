import streamlit as st

st.set_page_config(page_title="Daily Planner", page_icon="📋", layout="wide")

st.title("📋 Daily planner")
st.caption("A simple starter app for tracking priorities and planning your day.")

with st.sidebar:
    st.header("Your plan")
    focus = st.selectbox("Main focus", ["Deep work", "Meetings", "Learning", "Admin"])
    energy = st.slider("Energy level", 1, 10, 7)
    tasks = st.number_input("Tasks scheduled today", min_value=1, max_value=20, value=3)
    st.button("Save plan", use_container_width=True)

col1, col2, col3 = st.columns(3)
col1.metric("Focus block", "90 min")
col2.metric("Energy", f"{energy}/10")
col3.metric("Tasks", tasks)

st.subheader("Today at a glance")
left, right = st.columns(2)

with left:
    st.markdown(
        """
        ### Priority checklist
        - Review the top goal for the day
        - Block time for your most important task
        - Limit context switching
        """
    )

with right:
    notes = st.text_area(
        "Quick notes",
        "Write a short plan, reminders, or ideas here...",
        height=180,
    )
    st.info(f"Current focus: {focus}")

st.divider()
st.write("Use this template as a starting point and customize it for your own project.")
