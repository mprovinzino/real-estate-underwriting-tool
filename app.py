import streamlit as st

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

# Data for Rehab Estimation
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
    "Plumbing": [
        {"description": "Pipe repair", "unit": "Per spot", "unit_cost": 80},
        {"description": "Sewer scope", "unit": "House", "unit_cost": 375},
        {"description": "Sub slab contingency", "unit": "LS", "unit_cost": 1500},
        {"description": "Water Heater - DFW", "unit": "Per", "unit_cost": 1300},
    ],
    "Kitchen & Laundry": [
        {"description": "Appl, Range", "unit": "per", "unit_cost": 750},
        {"description": "Cabinets, Regular", "unit": "LF", "unit_cost": 110},
        {"description": "Granite - DFW", "unit": "LF", "unit_cost": 55},
        {"description": "Appl, Wall oven", "unit": "per", "unit_cost": 1100},
    ],
    "Foundation": [
        {"description": "Concrete foundation repair - DFW", "unit": "sqft", "unit_cost": 5},
        {"description": "Contingency", "unit": "LS", "unit_cost": 3500},
    ],
    "Roof & Attic": [
        {"description": "General maintenance", "unit": "Whole Rf", "unit_cost": 350},
        {"description": "Full Replacement - DFW", "unit": "sqft", "unit_cost": 5},
    ],
    "Living Areas": [
        {"description": "Interior Paint - DFW", "unit": "sqft", "unit_cost": 1.85},
        {"description": "Flooring - LVP - DFW", "unit": "sqft", "unit_cost": 3.75},
    ],
    "Bathroom": [
        {"description": "Granite top", "unit": "LF", "unit_cost": 100},
        {"description": "Vanity", "unit": "Per", "unit_cost": 450},
    ],
    "HVAC": [
        {"description": "3 Ton - DFW", "unit": "", "unit_cost": 5750},
        {"description": "Service call", "unit": "per unit", "unit_cost": 395},
    ],
}

# Header for Rehab Estimation
st.markdown('<div class="section-header">Rehab Estimation</div>', unsafe_allow_html=True)

# Initialize a total cost for the entire rehab
total_rehab_cost = 0

# Display all categories in a loop
for section, items in rehab_data.items():
    st.markdown(f"#### {section} Costs")
    section_total = 0

    # Loop through each item in the section
    for item in items:
        quantity = st.number_input(
            f"{item['description']} - Quantity ({item['unit']})",
            min_value=0.0,
            value=0.0 if item['unit'] != 'sqft' else float(square_footage),
            key=f"{section}_{item['description']}_qty"
        )
        
        # Calculate the total cost for this item based on quantity
        item_cost = item["unit_cost"] * quantity
        if quantity > 0:
            st.write(f"**Cost for {item['description']}:** ${item_cost:,.2f}")
            section_total += item_cost

    # Display the total cost for this section
    st.markdown(f"**Total {section} Cost:** ${section_total:,.2f}")
    total_rehab_cost += section_total

# Display the overall total rehab cost
st.markdown(f"### Total Rehab Cost: ${total_rehab_cost:,.2f}")

# Offer Calculations Header with consistent styling
st.markdown('<div class="section-header">Offer Calculations</div>', unsafe_allow_html=True)

# Calculate offer ranges based on ARV
low_range_offer = estimated_arv * 0.65
top_range_offer = estimated_arv * 0.78
max_suggested_offer = estimated_arv * 0.85

# Display offer calculations
st.write(f"**Low Range Offer (65% of ARV):** ${low_range_offer:,.2f}")
st.write(f"**Top Range Offer (78% of ARV):** ${top_range_offer:,.2f}")
st.write(f"**Max Suggested Offer (85% of ARV):** ${max_suggested_offer:,.2f}")

# Cash Flow and ROI Calculations Header with consistent styling
st.markdown('<div class="section-header">Cash Flow & ROI Estimation</div>', unsafe_allow_html=True)

# Calculate the annual rent and total investment
annual_rent = estimated_rent * 12
total_investment = total_rehab_cost + max_suggested_offer

# Calculate Cap Rate
cap_rate = (annual_rent / total_investment) * 100 if total_investment > 0 else 0
st.write(f"**Cap Rate:** {cap_rate:.2f}%")

# Inputs for property management, maintenance, and vacancy
property_management = st.number_input("Property Management (% of Rent)", min_value=0.0, max_value=100.0, value=8.0) / 100
maintenance = st.number_input("Maintenance (% of Rent)", min_value=0.0, max_value=100.0, value=5.0) / 100
vacancy = st.number_input("Vacancy Rate (% of Rent)", min_value=0.0, max_value=100.0, value=5.0) / 100

# Calculate net cash flow considering the expenses
net_cash_flow = annual_rent * (1 - (property_management + maintenance + vacancy))
st.write(f"**Estimated Annual Net Cash Flow:** ${net_cash_flow:,.2f}")
