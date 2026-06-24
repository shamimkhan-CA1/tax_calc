import streamlit as st


#NTN_No =st.number_input("Enter your NTN Number:")#int(input("Enter your NTN number: ")) 
name = st.text_input("Enter your Name:")#str(input("Enter your name : "))
#Birth_year = st.number_input("Enter your birth year:")#int(input("Enter your year of Birth: "))
#Age = (2026 - Birth_year)
#print("************************Your Tax details are************************")
income = st.number_input("Enter your Income:")#int(input("Please enter your annual income: "))

tax = 0.0
if income <= 600000:
    tax = income * 0
elif income <= 1200000:
    tax = (income-600000) * 0.01
elif income <= 2200000:
    tax = (income-1200000) * 0.11 + 6000
elif income <= 3200000:
    tax = (income-2200000) * 0.23 + 116000
elif income <= 4100000:
    tax = (income-3200000) * 0.3 + 346000
else:
    tax = (income-4100000) * 0.35 + 616000
    
Remainder = income - tax
# Annual_Expenditure = int(input("Your Annual Expenditure is: "))
# if(Remainder>Expenditure):
#     print(f"Increase_in_Assets = Re
#st.success(f"Mr. {name}! your Annual Income is Rs.{income} \nAge: {Age} \nYou pay Rs.{tax} in taxes \nIncome after Tax is Rs.{Remainder}")
st.success(f"Mr. {name}! your Income is Rs.{income}")
st.success(f"Mr. {name}! You pay Rs.{tax} in taxes")
st.success(f"Mr. {name}! Income after Tax is Rs.{Remainder}")