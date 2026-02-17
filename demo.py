# import streamlit as st
# import pandas as pd
# import numpy as np
# import time

# # FIXED: Changed 'icon' to 'page_icon'
# st.set_page_config(page_title="My Data App", page_icon="📊")

# st.title("🚀 Aditya's Data Dashboard")

# # Sidebar for controls
# st.sidebar.header("Settings")
# data_size = st.sidebar.slider("Select number of rows", 10, 100, 50)

# st.subheader("1. Randomly Generated Data")
# # Generate data
# chart_data = pd.DataFrame(
#     np.random.randn(data_size, 3),
#     columns=['A', 'B', 'C']
# )

# # Display table and chart
# st.dataframe(chart_data)
# st.line_chart(chart_data)

# # Interactive button
# if st.button('Run Analysis'):
#     st.balloons()
#     st.success("Analysis Complete!")


import streamlit as st

# 1. Initialize session state to track login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 2. Define the login function
def login():
    st.title("🔐 User Login")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            # Replace 'admin' and 'password123' with your desired credentials
            if username == "admin" and password == "12345":
                st.session_state.logged_in = True
                st.success("Logged in successfully!")
                st.rerun() # Refresh the page to show the main content
            else:
                st.error("Invalid username or password")

# 3. Logic to show either the Login page or the Main App
if not st.session_state.logged_in:
    login()
else:
    # --- THIS IS YOUR MAIN APP CONTENT ---
    st.title("🚀 Welcome to the Dashboard")
    st.write(f"Hello, Admin! You are now viewing protected content.")
    
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
    
    # Add your charts or videos here
    st.info("Your main app features go here.")
