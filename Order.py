import streamlit as st
import fitz
import pymupdf as pdf
import os

#manual labor for the images suck
############
#Page config
############
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.logo(os.path.join(BASE_DIR, "logo.jpeg"))
st.set_page_config(page_title="Main Menu")

st.image(os.path.join(BASE_DIR, "logo.jpeg"))
st.title("Palani's Kitchen")
st.header("Welcome to Palani's Kitchen. A business established since 1965")

###########
#Menu Items#
###########
dict_food_quantity = {}
st.subheader("Breakfast and Dinner")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.image(os.path.join(BASE_DIR, "images/idli.png"), use_container_width=True)
    idli = st.number_input("Idli - $3.00", step=1,min_value=0, key="idli") * 3.00
with c2:
    st.image(os.path.join(BASE_DIR, "images/dosai.png"), use_container_width=True)
    dosai = st.number_input("Dosai - $3.00", step=1,min_value=0, key="dosai") * 3.00
with c3:
    st.image(os.path.join(BASE_DIR, "images/pongal.png"), use_container_width=True)
    pongal = st.number_input("Pongal - $3.50", step=1,min_value=0, key="pongal") * 3.50
with c4:
    st.image(os.path.join(BASE_DIR, "images/puri.png"), use_container_width=True)
    puri = st.number_input("Puri - $5.50", step=1,min_value=0, key="puri") * 5.50

st.subheader("Breads")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.image(os.path.join(BASE_DIR, "images/naan.png"), use_container_width=True)
<<<<<<< HEAD
    naan = st.number_input("Naan - $3.50", step=1,min_value=0, key="naan") * 3.50
=======
    naan = st.number_input("Garlic Naan - $3.50", step=1, key="naan") * 3.50
>>>>>>> 5506f1dacfddb60b3f02f7097146104ba89dcfc5
with c2:
    st.image(os.path.join(BASE_DIR, "images/chapati.png"), use_container_width=True)
    chapati = st.number_input("Chapati - $4.30", step=1,min_value=0, key="chapati") * 4.30
with c3:
    st.image(os.path.join(BASE_DIR, "images/prata.png"), use_container_width=True)
    prata = st.number_input("Prata - $4.50", step=1,min_value=0, key="prata") * 4.50
with c4:
    st.image(os.path.join(BASE_DIR, "images/curry.png"), use_container_width=True)
<<<<<<< HEAD
    curry = st.number_input("Curry", step=1,min_value=0, key="curry")
=======
    curry = st.number_input("Butter Chicken - $5.70", step=1, key="curry")
>>>>>>> 5506f1dacfddb60b3f02f7097146104ba89dcfc5

st.subheader("Lunch")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.image(os.path.join(BASE_DIR, "images/meal_veg.png"), use_container_width=True)
    meal_veg = st.number_input("Regular Meals (Vegetarian) - $11.60", step=1,min_value=0, key="meal_veg") * 11.60
with c2:
    st.image(os.path.join(BASE_DIR, "images/meal_nonveg.png"), use_container_width=True)
    meal_nonveg = st.number_input("Regular Meals (Non-vegetarian) - $15.10", step=1,min_value=0, key="meal_nonveg") * 15.10
with c3:
    st.image(os.path.join(BASE_DIR, "images/veg_briyani.png"), use_container_width=True)
    veg_b = st.number_input("Vegetable Briyani - $12.30", step=1,min_value=0, key="veg_b") * 12.30
with c4:
    st.image(os.path.join(BASE_DIR, "images/chicken_briyani.png"), use_container_width=True)
    chick_b = st.number_input("Chicken Briyani - $15.20", step=1,min_value=0, key="chick_b") * 15.20

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.image(os.path.join(BASE_DIR, "images/mutton_briyani.png"), use_container_width=True)
    mutton_b = st.number_input("Mutton Briyani - $15.40", step=1,min_value=0, key="mutton_b") * 15.40
with c2:
    st.image(os.path.join(BASE_DIR, "images/fish_briyani.png"), use_container_width=True)
    fish_b = st.number_input("Fish Briyani - $15.90", step=1,min_value=0, key="fish_b") * 15.90

st.subheader("Snacks/Drinks")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.image(os.path.join(BASE_DIR, "images/sweets.png"), use_container_width=True)
<<<<<<< HEAD
    sweets = st.number_input("Sweets - $2.00", step=1,min_value=0, key="sweets") * 2.00
with c2:
    st.image(os.path.join(BASE_DIR, "images/crunchy.png"), use_container_width=True)
    crunchy = st.number_input("Crunchy Snacks - $2.00",min_value=0, step=1, key="crunchy") * 2.00
with c3:
    st.image(os.path.join(BASE_DIR, "images/drinks.png"), use_container_width=True)
    drinks = st.number_input("Drinks - $1.50", step=1,min_value=0, key="drinks") * 1.50
=======
    sweets = st.number_input("Gulab Jamun - $2.00", step=1, key="sweets") * 2.00
with c2:
    st.image(os.path.join(BASE_DIR, "images/crunchy.png"), use_container_width=True)
    crunchy = st.number_input("Murukku - $2.00", step=1, key="crunchy") * 2.00
with c3:
    st.image(os.path.join(BASE_DIR, "images/drinks.png"), use_container_width=True)
    drinks = st.number_input("Fruit Punch - $1.50", step=1, key="drinks") * 1.50
>>>>>>> 5506f1dacfddb60b3f02f7097146104ba89dcfc5

#################
#Total spendings#
#################
items = [
    idli, dosai, pongal, puri,
    naan, chapati, prata, curry,
    meal_veg, meal_nonveg, veg_b, chick_b, mutton_b, fish_b,
    sweets, crunchy, drinks
]

name_label = [
    "Idli", "Dosai", "Pongal", "Puri",
    "Naan", "Chapati", "Prata", "Curry",
    "Meals (Veg)", "Meals (Non-Veg)", "Veg Briyani", "Chicken Briyani",
    "Mutton Briyani", "Fish Briyani", "Sweets", "Crunchy Snacks", "Drinks"
]

total_spending = sum(items)

st.subheader("Submit Order Details")
with st.form("Submit Order", clear_on_submit=True):
    name = st.text_input("Name: ")
    hp_num = st.text_input("Handphone Number ")
    email = st.text_input("Email Address")
    home = st.text_input("Enter your home address")
    st.write(f"The total cost of your order is ${total_spending:.2f}")
    submit = st.form_submit_button("Submit Details")

#################
#recipt function#
#################
def recipt(item_list, label, naame, phone, mail, address):
    total_cost = sum(item_list)
    recipt_text = (
        f"Hello {naame}!\n"
        f"Email address: {mail}\n"
        f"Contact No.: {phone}\n"
        f"Delivery address: {address}\n"
        f"{'#'*30}\n"
    )
    for i in range(len(label)):
        if item_list[i] > 0:
            recipt_text += f"{label[i]}: ${round(item_list[i], 2)}\n"
    recipt_text += f"{'#'*30}\n"
    recipt_text += f"Total Cost of Order: ${round(total_cost, 2)}\n"
    recipt_text += "THANK YOU FOR ORDERING FROM PALANI'S KITCHEN\n"
    return recipt_text

##############
#Generate PDF#
##############
pdf_bytes = None
if submit:
    doc = pdf.open()
    doc.new_page()
    page = doc[0]
    image_rectangle = fitz.Rect(450, 20, 550, 120)
    page.insert_image(image_rectangle, filename="logo.jpeg")
    page.insert_text(pdf.Point(50, 50), recipt(items, name_label, name, hp_num, email, home))
    pdf_bytes = doc.write()
    doc.close()

###############
#Recipt Output#
###############
if pdf_bytes:
    st.download_button(
        label="Download Receipt",
        data=pdf_bytes,
        file_name="customer_receipt.pdf",
        mime="application/pdf"
    )
    st.write("Thank you for ordering from Palani's Kitchen")

