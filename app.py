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
beds = st.number_input("Number of Beds", min_value=0, value=3)
baths = st.number_input("Number of Baths", min_value=0.0, value=2.0)
year_built = st.number_input("Year Built", min_value=1800, max_value=2024, value=1990)
square_footage = st.number_input("Square Footage of Property", min_value=0, value=1800)
estimated_arv = st.number_input("Estimated After Repair Value (ARV) ($)", min_value=0, value=300000)
estimated_rent = st.number_input("Estimated Rent ($)", min_value=0, value=2500)

# Use the estimated ARV and rent in calculations where appropriate
arv = estimated_arv
market_rent = estimated_rent

# Display entered property details for review
st.write(f"**Property Details:** {beds} beds | {baths} baths | Built in {year_built} | {square_footage} sqft")

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
    "Plumbing": [
        {"description": "Pipe repair", "unit": "Per spot", "unit_cost": 80},
        {"description": "Sewer scope", "unit": "House", "unit_cost": 375},
        {"description": "Sub slab contingency", "unit": "", "unit_cost": 1500},
        {"description": "Water Heater - DFW", "unit": "", "unit_cost": 1300},
    ],
    "Foundation": [
        {"description": "Concrete foundation repair - DFW", "unit": "sqft", "unit_cost": 5},
        {"description": "Contingency", "unit": "LS", "unit_cost": 3500},
    ],
    "Roof & Attic": [
        {"description": "General maintenance", "unit": "Whole Rf", "unit_cost": 350},
        {"description": "Full Replacement - DFW", "unit": "sqft", "unit_cost": 5},
        {"description": "New decking", "unit": "sqft", "unit_cost": 0.90},
    ],
    "Living Areas": [
        {"description": "Interior Paint - DFW", "unit": "sqft", "unit_cost": 1.85},
        {"description": "Flooring - LVP - DFW", "unit": "sqft", "unit_cost": 3.75},
        {"description": "Drywall repair", "unit": "Per", "unit_cost": 150},
        {"description": "Window blinds", "unit": "Window", "unit_cost": 85},
    ],
    "Bathroom": [
        {"description": "Granite top", "unit": "LF", "unit_cost": 100},
        {"description": "Vanity", "unit": "Per", "unit_cost": 450},
        {"description": "Bathroom sink", "unit": "Per sink", "unit_cost": 85},
        {"description": "Shower surround", "unit": "Per", "unit_cost": 1100},
    ],
    "HVAC": [
        {"description": "3 Ton - DFW", "unit": "", "unit_cost": 5750},
        {"description": "4 Ton - DFW", "unit": "", "unit_cost": 6250},
        {"description": "Furnace - DFW", "unit": "", "unit_cost": 1500},
        {"description": "Ductwork (new)", "unit": "house", "unit_cost": 3000},
        {"description": "Thermostat", "unit": "per", "unit_cost": 175},
    ],
}

# Create columns for better arrangement
col1, col2, col3 = st.columns(3)

# Initialize total rehab cost
total_rehab_cost = 0

# Display sections in columns with expanders
with col1:
    for section in ["General", "Kitchen & Laundry", "Plumbing"]:
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
                    total_rehab_cost += total_item_cost
                    st.write(f"**Cost for {item['description']}:** ${total_item_cost:,.2f}")

# Continue with col2 and col3 for other sections...
# Display the total rehab cost
st.write(f"**Total Rehab Cost:** ${total_rehab_cost:,.2f}")

# ARV-based Offer Calculation
st.header("Offer Calculations")
low_range_offer = estimated_arv * 0.65
top_range_offer = estimated_arv * 0.78
max_suggested_offer = estimated_arv * 0.85

st.write(f"**Low Range Offer (65% of ARV):** ${low_range_offer:,.2f}")
st.write(f"**Top Range Offer (78% of ARV):** ${top_range_offer:,.2f}")
st.write(f"**Max Suggested Offer (85% of ARV):** ${max_suggested_offer:,.2f}")

# Cash Flow and ROI Calculations
st.header("Cash Flow & ROI Estimation")
monthly_rent = st.number_input("Monthly Rent ($)", min_value=0, value=estimated_rent)
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
