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

# Main title with consistent background styling
st.markdown('<div class="main-title">Real Estate Underwriting Tool</div>', unsafe_allow_html=True)

# Property Details section with bold text as the expander label
with st.expander("**Property Details**", expanded=True):
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

# Property Summary Header and content including rehab and offer details
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
        {"description": "Deep clean", "unit": "house", "unit_cost": 450},
        {"description": "Clean appliances", "unit": "per appl", "unit_cost": 0},
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
    # Add more categories as needed...
}

# Rehab Estimation section
with st.expander("**Rehab Estimation**", expanded=True):
    col1, col2 = st.columns(2)
    total_rehab_cost = 0

    # Group sections into columns for better layout
    sections_group1 = ["General", "Electrical", "Plumbing"]
    sections_group2 = ["Foundation", "Roof & Attic", "Living Areas"]

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
                total_rehab_cost += section_total

    st.markdown(f"### Total Rehab Cost: ${total_rehab_cost:,.2f}")

# Offer Calculations section with bold text as the expander label
with st.expander("**Offer Calculations**", expanded=True):
    st.info(
        "Each offer price is calculated using the formula: "
        "`Offer Price = (Percentage of ARV) - (Rehab Total)`.\n\n"
        "- **Low Range Offer (65% of ARV)**: Suitable for properties needing extensive work.\n"
        "- **Top Range Offer (78% of ARV)**: Typically for properties in better condition.\n"
        "- **Max Suggested Offer (85% of ARV)**: For properties with minimal repairs required."
    )
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
    maintenance = st.number_input("Maintenance (% of Rent)", min_value=0.0
