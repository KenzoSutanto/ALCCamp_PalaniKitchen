import streamlit as st
st.title("Palani's Kitchen")
st.header("Welcome to Palani's Kitchen. What would you like to order today?")

total_money = 0



st.subheader("Breakfast and Dinner")
idli = st.number_input("Idli ($3.00)", step=1)
dosai = st.number_input("Dosai ($3.00)")
pongal = st.number_input("Pongal ($3.50)")
puri = st.number_input("Puri ($5.50)")

st.subheader("Breads")
naan = st.number_input("Naan ($3.50)")
chapati = st.number_input("Chapati ($4.30)")
prata = st.number_input("Prata $4.50")
curry = st.toggle("Curry")

st.subheader("Lunch")
meal_veg = st.toggle("Regular Meals (Vegetarain) - $11.60")
meak_nonveg = st.toggle("Regular Meals (Non-vegetarian) - $13.10")
veg_b = st.toggle("Vegetable Briyani - $12.30")
chick_b = st.toggle("Chicken Briyani - $15.20")
mutton_b = st.toggle("Mutton Bryani - $15.40")
fish_b = st.toggle("Fish Briyani - $15.90")

st.subheader("Snacks/Drinks")
sweets = st.toggle("Sweets - $2.00")
crunchy = st.toggle("Crunchy Snacks - $2.00")
drinks = st.number_input("Drinks - $1.50")

