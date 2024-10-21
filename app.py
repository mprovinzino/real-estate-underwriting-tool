import streamlit as st
import pandas as pd

# Set up the page title and layout
st.set_page_config(page_title="Real Estate Underwriting Tool", layout="wide")

# Input Section
st.title("Real Estate Underwriting Tool")

# Property Details
st.header("Property Details")
address = st.text_input("Address", "123 Main St")
state = st.selectbox("State", ["Georgia", "Florida", "Texas", "California"])
market_rent = st.number_input("Market Rent ($)", min_value=0, value=2500)
arv = st.number_input("After Repair Value (ARV) ($)", min_value=0, value=300000)
square_footage = st.number_input("Square Footage of Property", min_value=0, value=1800)

# Rehab Estimation Section
st.header("Rehab Estimation")

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
    "Kitchen & Laundry": [
        {"description": "Appl, Range", "unit": "per", "unit_cost": 750},
        {"description": "Appl, Microwave with vent", "unit": "per", "unit_cost": 375},
        {"description": "Appl, Dishwasher", "unit": "per", "unit_cost": 650},
        {"description": "Cabinets, Regular", "unit": "LF", "unit_cost": 110},
        {"description": "Granite - DFW", "unit": "LF", "unit_cost": 55},
        {"description": "Appl, Wall oven", "unit": "per", "unit_cost": 1100},
        {"description": "Cabinet, base under sink", "unit": "per", "unit_cost": 225},
        {"description": "Sink, Kitchen", "unit": "per", "unit_cost": 225},
    ],
    # Add more sections as needed...
}

# Create columns for better arrangement
col1, col2 = st.columns(2)

# Initialize total rehab cost
total_rehab_cost = 0

# Display sections in columns with expanders
with col1:
    with st.expander("General"):
        for item in rehab_data["General"]:
            # If the unit is 'sqft', use the square footage as the default quantity.
            if item["unit"] == "sqft":
                quantity = st.number_input(
                    f"{item['description']} - Quantity ({item['unit']})",
                    min_value=0.0, value=float(square_footage),
                    key=f"General_{item['description']}_qty"
                )
            else:
                quantity = st.number_input(
                    f"{item['description']} - Quantity ({item['unit']})",
                    min_value=0.0, value=1.0,
                    key=f"General_{item['description']}_qty"
                )
            selected = st.checkbox(
                f"{item['description']} (${item['unit_cost']:.2f} per {item['unit']})",
                key=f"General_{item['description']}"
            )
            if selected:
                total_item_cost = item["unit_cost"] * quantity
                total_rehab_cost += total_item_cost
                st.write(f"**Cost for {item['description']}:** ${total_item_cost:,.2f}")

    with st.expander("Kitchen & Laundry"):
        for item in rehab_data["Kitchen & Laundry"]:
            quantity = st.number_input(
                f"{item['description']} - Quantity ({item['unit']})",
                min_value=0.0, value=1.0,
                key=f"Kitchen_{item['description']}_qty"
            )
            selected = st.checkbox(
                f"{item['description']} (${item['unit_cost']:.2f} per {item['unit']})",
                key=f"Kitchen_{item['description']}"
            )
            if selected:
                total_item_cost = item["unit_cost"] * quantity
                total_rehab_cost += total_item_cost
                st.write(f"**Cost for {item['description']}:** ${total_item_cost:,.2f}")

with col2:
    with st.expander("Electrical"):
        for item in rehab_data["Electrical"]:
            # Use square footage as default quantity if unit is 'sqft'
            if item["unit"] == "sqft":
                quantity = st.number_input(
                    f"{item['description']} - Quantity ({item['unit']})",
                    min_value=0.0, value=float(square_footage),
                    key=f"Electrical_{item['description']}_qty"
                )
            else:
                quantity = st.number_input(
                    f"{item['description']} - Quantity ({item['unit']})",
                    min_value=0.0, value=1.0,
                    key=f"Electrical_{item['description']}_qty"
                )
            selected = st.checkbox(
                f"{item['description']} (${item['unit_cost']:.2f} per {item['unit']})",
                key=f"Electrical_{item['description']}"
            )
            if selected:
                total_item_cost = item["unit_cost"] * quantity
                total_rehab_cost += total_item_cost
                st.write(f"**Cost for {item['description']}:** ${total_item_cost:,.2f}")

# Display the total rehab cost
st.write(f"**Total Rehab Cost:** ${total_rehab_cost:,.2f}")

# ARV-based Offer Calculation
st.header("Offer Calculations")
low_range_offer = arv * 0.65
top_range_offer = arv * 0.78
max_suggested_offer = arv * 0.85

st.write(f"**Low Range Offer (65% of ARV):** ${low_range_offer:,.2f}")
st.write(f"**Top Range Offer (78% of ARV):** ${top_range_offer:,.2f}")
st.write(f"**Max Suggested Offer (85% of ARV):** ${max_suggested_offer:,.2f}")

# Cash Flow and ROI Calculations
st.header("Cash Flow & ROI Estimation")
monthly_rent = st.number_input("Monthly Rent ($)", min_value=0, value=3000)
annual_rent = monthly_rent * 12
total_investment = total_rehab_cost + max_suggested_offer

# Calculate Cap Rate
cap_rate = (annual_rent / total_investment) * 100 if total_investment > 0 else 0
st.write(f"**Cap Rate:** {cap_rate:.2f}%")

# Net Cash Flow estimation with placeholders for expenses
property_management = st.number_input("Property Management (% of Rent)", min_value=0.0, max_value=100.0, value=8.0) / 100
maintenance = st.number_input("Maintenance (% of Rent)", min_value=0.0, max_value=100.0, value=5.0) / 100
vacancy = st.number_input("Vacancy Rate (% of Rent)", min_value=0.0, max_value=100.0, value=5.0) / 100

# Calculate net cash flow considering the expenses
net_cash_flow = annual_rent * (1 - (property_management + maintenance + vacancy))
st.write(f"**Estimated Annual Net Cash Flow:** ${net_cash_flow:,.2f}")
