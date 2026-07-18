import streamlit as st

st.set_page_config(page_title="Emotion Detection & Learning Support Engine")

st.title("Emotion Detection & Learning Support Engine")

field = st.selectbox(
    "Select Field",
    ["Student", "Teacher", "Developer", "Other"]
)

problem = st.text_area("Enter your problem")

if st.button("Analyze"):
    st.success("Analysis Completed")
    st.write("Selected Field:", field)
    st.write("Problem:", problem)
