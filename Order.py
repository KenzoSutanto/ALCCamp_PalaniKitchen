import streamlit as st

#Page config
st.set_page_config(
    page_title="Main Menu"
)


st.title("Palani's Kitchen")
st.header("Welcome to Palani's Kitchen. A business established since 2025?")

total = 0



st.subheader("Breakfast and Dinner")
idli = st.number_input("Idli - $3.00", step=1,) * 3.00
dosai = st.number_input("Dosai - $3.00", step=1) * 3.00
pongal = st.number_input("Pongal - $3.50", step=1) * 3.50
puri = st.number_input("Puri - $5.50", step=1) * 5.50

st.subheader("Breads")
naan = st.number_input("Naan - $3.50", step=1) * 3.50
chapati = st.number_input("Chapati $4.30", step=1) * 4.30
prata = st.number_input("Prata $4.50", step=1) * 4.50
curry = st.number_input("Curry", step=1)

st.subheader("Lunch")
meal_veg = st.number_input("Regular Meals (Vegetarain) - $11.60", step=1) * 11.60
meal_nonveg =st.number_input("Regular Meals (Non-vegetarian) - $13.10", step=1) * 15.10
veg_b = st.number_input("Vegetable Briyani - $12.30", step=1) * 12.30
chick_b = st.number_input("Chicken Briyani - $15.20,", step=1) * 15.20
mutton_b = st.number_input("Mutton Bryani - $15.40", step=1) * 15.40
fish_b = st.number_input("Fish Briyani - $15.90", step=1) * 15.90

st.subheader("Snacks/Drinks")
sweets = st.number_input("Sweets - $2.00", step=1) * 2.00
crunchy = st.number_input("Crunchy Snacks - $2.00", step=1) * 2.00
drinks = st.number_input("Drinks - $1.50", step=1) * 1.50

total =idli+dosai+pongal+puri+naan+chapati+prata+meal_veg+meal_nonveg+veg_b+chick_b+mutton_b+fish_b+sweets+crunchy+drinks
st.subheader(f"Total: ${round(total,4)}") 