import streamlit as st
from views.calculation_tab1 import calculation_tab1
from views.calculation_tab2 import calculation_tab2
from views.calculation_tab3 import calculation_tab3
from views.influx_height import influx_height
from views.estimate_influx_type import estimate_influx_type  # <-- Add this import
from views.formation_pressure import formation_pressure
from views.gas_cut_pressure_loss import gas_cut_pressure_loss
from views.kick_penetration import kick_penetration
from views.icp_fcp import icp_fcp  # <-- Add this import
from views.kick_tolerance_factor import kick_tolerance_factor

def main():
    main_tabs = [
        "Home",
        "Well Control Formulas"
    ]

    selected_main = st.sidebar.radio("Main Menu", main_tabs)

    if selected_main == "Home":
        st.title("Drilling Formula Calculator")
        # Read and format content.txt
        with open("../content.txt", "r") as f:
            lines = f.readlines()

        formatted = ""
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#"):
                # Make section header (remove # and add Markdown header)
                formatted += f"\n\n### {stripped.lstrip('#').strip()}\n"
            elif stripped:
                # Make bullet point
                formatted += f"- {stripped}\n"
            else:
                formatted += "\n"

        st.markdown(formatted)
    elif selected_main == "Well Control Formulas":
        sub_tabs = [
            "Actual Gas Migration Rate",
            "MISICP",
            "Adjusted MASICP",
            "Influx Height",
            "Estimate Type of Influx (Kick)",
            "Formation Pressure from Kick Analysis",
            "Hydrostatic Pressure Loss Due to Gas Cut Mud",
            "Kick Penetration For Stripping Operation",
            "Initial & Final Circulating Pressure (ICP & FCP)",
            "Kick Tolerance Factor"  # <-- Add this line
        ]
        selected_sub = st.sidebar.radio("Well Control Formulas", sub_tabs)
        if selected_sub == "Actual Gas Migration Rate":
            calculation_tab1()
        elif selected_sub == "MISICP":
            calculation_tab2()
        elif selected_sub == "Adjusted MASICP":
            calculation_tab3()
        elif selected_sub == "Influx Height":
            influx_height()
        elif selected_sub == "Estimate Type of Influx (Kick)":
            estimate_influx_type()
        elif selected_sub == "Formation Pressure from Kick Analysis":
            formation_pressure()
        elif selected_sub == "Gas Cut Pressure Loss":
            gas_cut_pressure_loss()
        elif selected_sub == "Hydrostatic Pressure Loss Due to Gas Cut Mud":
            gas_cut_pressure_loss()
        elif selected_sub == "Kick Penetration For Stripping Operation":
            kick_penetration()  # <-- Add this line
        elif selected_sub == "Initial & Final Circulating Pressure (ICP & FCP)":
            icp_fcp()
        elif selected_sub == "Kick Tolerance Factor":
            kick_tolerance_factor()

if __name__ == "__main__":
    main()