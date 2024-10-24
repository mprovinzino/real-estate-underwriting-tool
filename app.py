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
    .small-input input {
        width: 80px !important;
    }
    </style>
    """, unsafe_allow_html=True
)

# Main title
st.markdown('<div class="main-title">Real Estate Underwriting Tool</div>', unsafe_allow_html=True)

# Property Details section
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

# Data for Rehab Estimation with all categories and items
rehab_data = {
    "General": [
        {"description": "Deep clean", "unit": "house", "unit_cost": 450},
        {"description": "Clean appliances", "unit": "per appl", "unit_cost": 100},
        {"description": "Demo", "unit": "Guy/day", "unit_cost": 300},
        {"description": "Trash out", "unit": "Per", "unit_cost": 500},
        {"description": "40 yd dumpster", "unit": "Per", "unit_cost": 725},
        {"description": "Virtual Contingency", "unit": "LS", "unit_cost": 3500},
        {"description": "Termite treatment", "unit": "House", "unit_cost": 375},
        {"description": "GC Permit & Fees", "unit": "LS", "unit_cost": 1500},
    ],
    "Exterior": [
        {"description": "Siding repair", "unit": "", "unit_cost": 600},
        {"description": "Complete New Siding", "unit": "sqft", "unit_cost": 3.05},
        {"description": "Paint garage door (overhead)", "unit": "per door", "unit_cost": 100},
        {"description": "Paint exterior door", "unit": "per door", "unit_cost": 250},
        {"description": "Fascia repair", "unit": "LF", "unit_cost": 8},
        {"description": "Soffit repair", "unit": "LF", "unit_cost": 10},
        {"description": "Exterior Paint", "unit": "sqft", "unit_cost": 2.25},
        {"description": "Yard clean", "unit": "yard", "unit_cost": 250},
    ],
    "Electrical": [
        {"description": "Plugs/switches/coverplates", "unit": "sqft", "unit_cost": 0.45},
        {"description": "Smoke/CO2 Combos", "unit": "per unit", "unit_cost": 50},
        {"description": "Weather head upgrade", "unit": "per unit", "unit_cost": 750},
        {"description": "New Panel Box", "unit": "Per", "unit_cost": 2000},
    ],
    "Plumbing": [
        {"description": "Pipe repair", "unit": "Per spot", "unit_cost": 80},
        {"description": "Sewer scope", "unit": "House", "unit_cost": 375},
        {"description": "Water Heater", "unit": "", "unit_cost": 1300},
    ],
    "Foundation": [
        {"description": "Concrete foundation repair", "unit": "sqft", "unit_cost": 5},
        {"description": "Contingency", "unit": "LS", "unit_cost": 3500},
    ],
    "Roof & Attic": [
        {"description": "General maintenance", "unit": "Whole Rf", "unit_cost": 350},
        {"description": "Full Replacement", "unit": "sqft", "unit_cost": 5},
        {"description": "New decking", "unit": "sqft", "unit_cost": 0.9},
    ],
    "Living Areas": [
        {"description": "Door hardware", "unit": "Per door", "unit_cost": 25},
        {"description": "Interior Paint", "unit": "sqft", "unit_cost": 1.85},
        {"description": "Flooring", "unit": "sqft", "unit_cost": 3.75},
    ],
    "Bathroom": [
        {"description": "Granite top", "unit": "LF", "unit_cost": 100},
        {"description": "Vanity", "unit": "Per", "unit_cost": 450},
        {"description": "Toilet", "unit": "", "unit_cost": 225},
    ],
    "HVAC": [
        {"description": "New HVAC - 3 Ton", "unit": "", "unit_cost": 5750},
        {"description": "New Furnace", "unit": "", "unit_cost": 1500},
        {"description": "Ductwork (new)", "unit": "house", "unit_cost": 1400},
    ],
}

# Rehab Estimation section
with st.expander("**Rehab Estimation**", expanded=True):
    col1, col2 = st.columns(2)
    total_rehab_cost = 0

    sections_group1 = ["General", "Exterior", "Electrical", "Living Areas"]
    sections_group2 = ["Plumbing", "Foundation", "Roof & Attic", "Bathroom", "HVAC"]

    for col, sections in zip([col1, col2], [sections_group1, sections_group2]):
        for section in sections:
            with col:
                st.markdown(f"#### {section} Costs")
                section_total = 0
                for item in rehab_data.get(section, []):
                    quantity = st.number_input(
                        f"{item['description']} - Quantity ({item['unit']})",
                        min_value=0,
                        value=0,
                        step=1,
                        key=f"{section}_{item['description']}_qty",
                        help=f"Unit Cost: ${item['unit_cost']:,.2f} per {item['unit']}"
                    )
                    item_cost = item["unit_cost"] * quantity
                    section_total += item_cost
                st.markdown(f"**Total {section} Cost:** ${section_total:,.2f}")
                total_rehab_cost += section_total

    st.markdown(f"### Total Rehab Cost: ${total_rehab_cost:,.2f}")

# Offer Calculations section
with st.expander("**Offer Calculations**", expanded=True):
    low_range_offer = (estimated_arv * 0.65) - total_rehab_cost
    top_range_offer = (estimated_arv * 0.78) - total_rehab_cost
    max_suggested_offer = (estimated_arv * 0.85) - total_rehab_cost

    st.write(f"**Low Range Offer (65% of ARV - Rehab Total):** ${low_range_offer:,.2f}")
    st.write(f"**Top Range Offer (78% of ARV - Rehab Total):** ${top_range_offer:,.2f}")
    st.write(f"**Max Suggested Offer (85% of ARV - Rehab Total):** ${max_suggested_offer:,.2f}")

# Cash Flow and ROI section
with st.expander("**Cash Flow & ROI Estimation**", expanded=True):
    annual_rent = estimated_rent * 12
    total_investment = total_rehab_cost + max_suggested_offer
    cap_rate = (annual_rent / total_investment) * 100 if total_investment > 0 else 0
    st.write(f"**Cap Rate:** {cap_rate:.2f}%")

    property_management = st.number_input("Property Management (% of Rent)", min_value=0.0, max_value=100.0, value=8.0) / 100
    maintenance = st.number_input("Maintenance (% of Rent)", min_value=0.0, max_value=100.0, value=5.0) / 100
    vacancy = st.number_input("Vacancy Rate (% of Rent)", min_value=0.0, max_value=100.0, value=5.0) / 100

    net_cash_flow = annual_rent * (1 - (property_management + maintenance + vacancy))
    st.write(f"**Estimated Annual Net Cash Flow:** ${net_cash_flow:,.2f}")

# Property Summary, now placed after all calculations
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
            <div class="summary-item">🔧 <strong>Total Rehab Cost:</strong> ${total_rehab_cost:,.2f}</div>
        </div>
        <hr style="border: 1px solid #ddd; margin: 20px 0;">
        <div class="summary-row">
            <div class="summary-item">📉 <strong>Low Range Offer (65%):</strong> ${low_range_offer:,.2f}</div>
            <div class="summary-item">📈 <strong>Top Range Offer (78%):</strong> ${top_range_offer:,.2f}</div>
            <div class="summary-item">🏷️ <strong>Max Suggested Offer (85%):</strong> ${max_suggested_offer:,.2f}</div>
        </div>
    </div>
""", unsafe_allow_html=True)
