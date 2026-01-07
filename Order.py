import streamlit as st
import fitz
import pymupdf as pdf

############
#Page config
############
st.logo("logo.jpeg")
st.set_page_config(
    page_title="Main Menu"
)

st.image("logo.jpeg")
st.title("Palani's Kitchen")
st.header("Welcome to Palani's Kitchen. A business established since 1965")

###########
#Menu Items#
###########
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

#################
#Total spendings#
#################
items = [idli, dosai, pongal, puri, naan, chapati, prata, curry, meal_veg, meal_nonveg, veg_b, chick_b, mutton_b, fish_b, sweets, crunchy, drinks]
name_label = ["Idli", "Dosai", "Pongal", "Puri", "Naan", "Chapati", "Prata", "Curry", "Meals (Veg)", "Meals (Non-Veg)", "Veg Briyani", "Chicken Briyani", "Mutton Briyani", "Fish Briyani", "Sweets", "Crunchy Snacks", "Drinks"]

total_spending = sum(items)







st.subheader("Submit Order Details")
with st.form("Submit Order", clear_on_submit = True):
    name = st.text_input("Name: ")
    hp_num = st.text_input("Handphone Number ")
    email = st.text_input("Email Address")
    home = st.text_input("Enter your home address")
    st.write(f"The total cost of your order is ${round(total_spending, 2)}0")
    submit = st.form_submit_button("Submit Details")
    if submit == True:
        submit = False


#################
#recipt function#
#################
def recipt(item_list, label, naame, phone, mail, address):
    total_cost = sum(item_list)
    recipt_text = f'''
Hello {naame}!
Email address: {mail}
Contact No. {phone}
Delivery address {address}
{"#"*30}
'''

    for name in label:
        index = label.index(name)
        if item_list[index] > 0:
            recipt_text += f"\n{label[index]}: ${round(item_list[index], 2)}"
    recipt_text += f"\nTotal Cost of Order: ${round(total_cost, 2)}0\n"
    recipt_text += "#"*30
    recipt_text += "\n~~~THANK YOU FOR ORDERING FROM PALANI's KITCHEN~~~"

    return recipt_text

##############
#Generate PDF#
##############
doc = pdf.open()
doc.new_page()
page = doc[0]
image_rectangle = fitz.Rect(450, 20, 550, 120)
page.insert_image(image_rectangle, filename="logo.jpeg")
page.insert_text(pdf.Point(50,50), recipt(items, name_label, name, hp_num, email, home))
doc.save("customer_recipt.pdf")
pdf_bytes = doc.write()

###############
#Recipt Output#
###############
st.download_button(
    label="Download Receipt",
    data=pdf_bytes,
    file_name="customer_receipt.pdf",
    mime="application/pdf"
)
st.write("Thank you for ordering from Palani's Kitchen")
#hello
