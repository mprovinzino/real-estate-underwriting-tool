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

# Repair Costs Section
st.header("Repair Costs")
# Create a DataFrame to store repair costs dynamically
repair_items = {
    "Category": ["General", "Electrical", "Plumbing", "Foundation", "Roof", "Exterior"],
    "Unit Cost": [0, 0, 0, 0, 0, 0],
    "Quantity": [0, 0, 0, 0, 0, 0]
}
df = pd.DataFrame(repair_items)
# Let the user input values directly using text input and number input
for index, row in df.iterrows():
    df.at[index, "Unit Cost"] = st.number_input(f"Unit Cost for {row['Category']}", value=row["Unit Cost"])
    df.at[index, "Quantity"] = st.number_input(f"Quantity for {row['Category']}", value=row["Quantity"])

# Display the updated dataframe as a table
st.write("Updated Repair Costs Table")
st.table(df)

# Calculate Total Repair Costs
df['Total Cost'] = df['Unit Cost'] * df['Quantity']
total_repair_cost = df['Total Cost'].sum()
st.write(f"**Total Repair Cost:** ${total_repair_cost:,.2f}")

# ARV-based Offer Calculation
st.header("Offer Calculations")
low_range_offer = arv * 0.65
top_range_offer = arv * 0.78
max_suggested_offer = arv * 0.85

st.write(f"**Low Range Offer (65% of ARV):** ${low_range_offer:,.2f}")
st.write(f"**Top Range Offer (78% of ARV):** ${top_range_offer:,.2f}")
st.write(f"**Max Suggested Offer (85% of ARV):** ${max_suggested_offer:,.2f}")

# Display the DataFrame for better visualization
st.subheader("Detailed Repair Costs")
st.write(df)

# Cash Flow and ROI Calculations
st.header("Cash Flow & ROI Estimation")
monthly_rent = st.number_input("Monthly Rent ($)", min_value=0, value=3000)
annual_rent = monthly_rent * 12
total_investment = total_repair_cost + max_suggested_offer

cap_rate = (annual_rent / total_investment) * 100 if total_investment > 0 else 0
st.write(f"**Cap Rate:** {cap_rate:.2f}%")

# Net Cash Flow estimation with placeholders for expenses
property_management = st.number_input("Property Management (% of Rent)", min_value=0.0, max_value=100.0, value=8.0) / 100
maintenance = st.number_input("Maintenance (% of Rent)", min_value=0.0, max_value=100.0, value=5.0) / 100
vacancy = st.number_input("Vacancy Rate (% of Rent)", min_value=0.0, max_value=100.0, value=5.0) / 100

net_cash_flow = annual_rent * (1 - (property_management + maintenance + vacancy))
st.write(f"**Estimated Annual Net Cash Flow:** ${net_cash_flow:,.2f}")
