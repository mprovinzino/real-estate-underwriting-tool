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

# Rehab Estimation Section
st.header("Rehab Estimation")

# Data for Rehab Estimation
rehab_data = {
    "General": [
        {"description": "Clean appliances", "unit": "per appl", "unit_cost": 100, "quantity": 1},
        {"description": "Demo", "unit": "Guy/day", "unit_cost": 300, "quantity": 1},
        {"description": "Trash out", "unit": "Per", "unit_cost": 500, "quantity": 1},
        {"description": "40 yd dumpster", "unit": "Per", "unit_cost": 725, "quantity": 1},
        {"description": "Virtual Contingency", "unit": "LS", "unit_cost": 3500, "quantity": 1},
        {"description": "Termite treatment", "unit": "House", "unit_cost": 375, "quantity": 1},
        {"description": "GC Permit & Fees", "unit": "LS", "unit_cost": 1500, "quantity": 1},
    ],
    "Electrical": [
        {"description": "Plugs/switches/coverplates", "unit": "sqft", "unit_cost": 0.45, "quantity": 1800},
        {"description": "Smoke/CO2 Combos", "unit": "per unit", "unit_cost": 50, "quantity": 1},
        {"description": "Weather head upgrade", "unit": "per unit", "unit_cost": 750, "quantity": 1},
        {"description": "GFCI", "unit": "Per", "unit_cost": 65, "quantity": 1},
        {"description": "Smoke detectors", "unit": "per unit", "unit_cost": 30, "quantity": 1},
        {"description": "New Panel Box - DFW", "unit": "", "unit_cost": 2000, "quantity": 1},
    ],
    "Exterior": [
        {"description": "Siding repair", "unit": "", "unit_cost": 600, "quantity": 1},
        {"description": "Complete New Siding", "unit": "sqft", "unit_cost": 3.05, "quantity": 1800},
        {"description": "Paint garage door (overhead)", "unit": "per door", "unit_cost": 100, "quantity": 1},
        {"description": "Paint exterior door", "unit": "per door", "unit_cost": 250, "quantity": 1},
        {"description": "Fascia repair", "unit": "LF", "unit_cost": 8, "quantity": 1},
        {"description": "Soffit repair", "unit": "LF", "unit_cost": 10, "quantity": 1},
        {"description": "Caulk/general maint", "unit": "House", "unit_cost": 350, "quantity": 1},
        {"description": "Exterior Paint - DFW", "unit": "sqft", "unit_cost": 2.25, "quantity": 1724},
        {"description": "Kwikset Smartkey Lockset", "unit": "LS", "unit_cost": 400, "quantity": 1},
        {"description": "Overhead door (Double)", "unit": "per", "unit_cost": 1300, "quantity": 1},
        {"description": "Garage door opener", "unit": "per", "unit_cost": 385, "quantity": 1},
        {"description": "Yard clean", "unit": "yard", "unit_cost": 250, "quantity": 1},
        {"description": "Fence replacement", "unit": "LF", "unit_cost": 24, "quantity": 1},
        {"description": "Trim tree", "unit": "per tree", "unit_cost": 350, "quantity": 1},
    ],
    "Kitchen & Laundry": [
        {"description": "Appl, Range", "unit": "per", "unit_cost": 750, "quantity": 1},
        {"description": "Appl, Microwave with vent", "unit": "per", "unit_cost": 375, "quantity": 1},
        {"description": "Appl, Dishwasher", "unit": "per", "unit_cost": 650, "quantity": 1},
        {"description": "Cabinets, Regular", "unit": "LF", "unit_cost": 110, "quantity": 20},
        {"description": "Granite - DFW", "unit": "LF", "unit_cost": 55, "quantity": 40},
        {"description": "Appl, Wall oven", "unit": "per", "unit_cost": 1100, "quantity": 1},
        {"description": "Cabinet, base under sink", "unit": "per", "unit_cost": 225, "quantity": 1},
        {"description": "Sink, Kitchen", "unit": "per", "unit_cost": 225, "quantity": 1},
    ],
    "Plumbing": [
        {"description": "Pipe repair", "unit": "Per spot", "unit_cost": 80, "quantity": 1},
        {"description": "Sewer scope", "unit": "House", "unit_cost": 375, "quantity": 1},
        {"description": "Sub slab contingency", "unit": "", "unit_cost": 1500, "quantity": 1},
        {"description": "Water Heater - DFW", "unit": "", "unit_cost": 1300, "quantity": 1},
    ],
    "HVAC": [
        {"description": "3 Ton - DFW", "unit": "", "unit_cost": 5750, "quantity": 1},
        {"description": "4 Ton - DFW", "unit": "", "unit_cost": 6250, "quantity": 1},
        {"description": "Furnace - DFW", "unit": "", "unit_cost": 1500, "quantity": 1},
        {"description": "Ductwork (new)", "unit": "house", "unit_cost": 3000, "quantity": 1},
        {"description": "Thermostat", "unit": "per", "unit_cost": 175, "quantity": 1},
        {"description": "Cage for AC unit", "unit": "Per", "unit_cost": 350, "quantity": 1},
    ]
}

# Loop through sections and items, allowing users to select them
total_rehab_cost = 0
for section, items in rehab_data.items():
    st.subheader(section)
    for item in items:
        checkbox_label = f"{item['description']} ({item['unit']}) - ${item['unit_cost']:.2f} per unit"
        selected = st.checkbox(checkbox_label, value=(item['unit_cost'] > 0), key=f"{section}_{item['description']}")
        if selected:
            total_item_cost = item['unit_cost'] * item['quantity']
            total_rehab_cost += total_item_cost
            st.write(f"**Cost for {item['description']}:** ${total_item_cost:,.2f}")

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

