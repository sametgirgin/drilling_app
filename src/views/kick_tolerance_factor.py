import streamlit as st

def kick_tolerance_factor():
    st.markdown("<h2 style='text-align: center;'>Kick Tolerance Factor Calculator</h2>", unsafe_allow_html=True)
    st.markdown("""

    Kick Tolerance Factor = (Casing Shoe TVD / Well Depth TVD) × (Maximum Allowable MW − Current MW)

    - Casing Shoe TVD: True Vertical Depth of casing shoe (ft)
    - Well Depth TVD: True Vertical Depth of well (ft)
    - Maximum Allowable MW: Maximum Allowable Mud Weight (ppg)
    - Current MW: Current Mud Weight (ppg)
    """)

    casing_shoe_tvd = st.number_input("Casing Shoe TVD (ft)", min_value=0.0, value=5000.0)
    well_depth_tvd = st.number_input("Well Depth TVD (ft)", min_value=0.01, value=11000.0)
    max_allowable_mw = st.number_input("Maximum Allowable MW (ppg)", min_value=0.0, value=12.9)
    current_mw = st.number_input("Current MW (ppg)", min_value=0.0, value=9.8)

    if st.button("Calculate Kick Tolerance Factor"):
        ktf = (casing_shoe_tvd / well_depth_tvd) * (max_allowable_mw - current_mw)
        st.success(f"**Kick Tolerance Factor: {ktf:.2f} ppg**")