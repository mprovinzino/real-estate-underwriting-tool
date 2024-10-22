import streamlit as st
import pandas as pd

# Add CSS styling for consistent look and feel
st.markdown(
    """
    <style>
    .main-title {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #333;
        margin-bottom: 20px;
    }
    .section-header {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ddd;
        font-size: 20px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
        text-align: center;
    }
    .summary-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin: 0 auto;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        width: 100%;
    }
    .summary-title {
        font-size: 22px;
        font-weight: bold;
        color: #333;
        text-align: center;
        margin-bottom: 5px;
    }
    .summary-item {
        font-size: 18px;
        margin-bottom: 8px;
        display: inline-block;
        width: 45%;
        text-align: center;
    }
    .summary-row {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
    }
    </style>
    """, unsafe_allow_html=True
)

# Main title with consistent background styling
st.markdown('<div class="main-title">Real Estate Underwriting Tool</div>', unsafe_allow_html=True)

# Property Details Header with consistent styling
st.markdown('<div class="section-header">Property Details</div>', unsafe_allow_html=True)

# Property Details Inputs
with st.expander("Property Details", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        address = st.text_input("Address", "123 Main St")
        state = st.selectbox("State", ["Georgia", "Florida", "Texas", "California"])
        year_built = st.number_input("Year Built", min_value=1800, max_value=2024, value=1990)
    with col2:
        beds = st.number_input("Number of Beds", min_value=0, value=3)
        baths = st.number_input("Number of Baths", min_value=0.0, value=2.0)
        square_footage = st.number_input("Square Footage of Property", min_value=0, value=1800)
    with col3:
        estimated_arv = st.number_input("Estimated After Repair Value (ARV) ($)", min_value=0, value=300000)
        estimated_rent = st.number_input("Estimated Rent ($)", min_value=0, value=2500)

# Property Summary Header and content
st.markdown(f"""
    <div class="summary-box">
        <div class="summary-title">
            🏡 Property Summary - {address}, {state}
        </div>
        <div class="summary-row">
            <div class="summary-item">🛏️ <strong>Beds:</strong> {beds}</div>
            <div class="summary-item">🛁 <strong>Baths:</strong> {baths}</div>
            <div class="summary-item">📅 <strong>Year Built:</strong> {year_built}</div>
            <div class="summary-item">📏 <strong>Square Footage:</strong> {square_footage} sqft</div>
            <div class="summary-item">💰 <strong>Estimated ARV:</strong> ${estimated_arv:,.2f}</div>
            <div class="summary-item">🏠 <strong>Estimated Rent:</strong> ${estimated_rent:,.2f}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Rehab Estimation Header with consistent styling
st.markdown('<div class="section-header">Rehab Estimation</div>', unsafe_allow_html=True)

# Example data for Rehab Estimation
rehab_data = {
    "General": [
        {"description": "Clean appliances", "unit": "per appl", "unit_cost": 100},
        {"description": "Demo", "unit": "Guy/day", "unit_cost": 300},
        {"description": "Trash out", "unit": "Per", "unit_cost": 500},
        {"description": "40 yd dumpster", "unit": "Per", "unit_cost": 725},
        {"description": "Virtual Contingency", "unit": "LS", "unit_cost": 3500},
        {"description": "Termite treatment", "unit": "House", "unit_cost": 375},
        {"description": "GC Permit & Fees", "unit": "LS", "unit_cost": 1500},
    ],
    "Electrical": [
        {"description": "Plugs/switches/coverplates", "unit": "sqft", "unit_cost": 0.45},
        {"description": "Smoke/CO2 Combos", "unit": "per unit", "unit_cost": 50},
        {"description": "Weather head upgrade", "unit": "per unit", "unit_cost": 750},
        {"description": "GFCI", "unit": "Per", "unit_cost": 65},
        {"description": "Smoke detectors", "unit": "per unit", "unit_cost": 30},
        {"description": "New Panel Box - DFW", "unit": "Per", "unit_cost": 2000},
    ],
    # Add other sections like "Kitchen & Laundry", "Plumbing", "Foundation", etc.
}

# Create columns for better arrangement in the Rehab Estimation section
col1, col2, col3 = st.columns(3)

# Display sections in columns with expanders
with col1:
    for section in ["General", "Electrical"]:
        with st.expander(section):
            for item in rehab_data[section]:
                quantity = st.number_input(
                    f"{item['description']} - Quantity ({item['unit']})",
                    min_value=0.0,
                    value=1.0 if item['unit'] != 'sqft' else float(square_footage),
                    key=f"{section}_{item['description']}_qty"
                )
                selected = st.checkbox(
                    f"{item['description']} (${item['unit_cost']:.2f} per {item['unit']})",
                    key=f"{section}_{item['description']}"
                )
                if selected:
                    total_item_cost = item["unit_cost"] * quantity
                    st.write(f"**Cost for {item['description']}:** ${total_item_cost:,.2f}")

# Add additional columns for other sections like Plumbing, Foundation, etc.

# Display the total rehab cost
# Add calculations and display the result as needed
st.markdown('<div class="section-header">Offer Calculations</div>', unsafe_allow_html=True)
# Add the calculation logic and display

st.markdown('<div class="section-header">Cash Flow & ROI Estimation</div>', unsafe_allow_html=True)
# Add cash flow and ROI calculation logic
