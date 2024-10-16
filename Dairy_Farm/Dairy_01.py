from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Prices per liter
milk_prices = {
    'buffalo': 80,
    'cow': 100
}

# Route to render the order page
@app.route('/')
def Dairy_Org():
    return render_template('Dairy_Org.html')

# Route to handle the order
@app.route('/order', methods=['POST'])
def order():
    # Getting form data
    name = request.form.get('name')
    address = request.form.get('address')
    phone = request.form.get('phone')
    milk_type = request.form.get('milk_type')
    liters = int(request.form.get('liters'))

    # Calculating total amount
    price_per_liter = milk_prices.get(milk_type)
    total_amount = price_per_liter * liters

    # Creating the WhatsApp message
    message = f"Order received from {name}.\nAddress: {address}\nPhone: {phone}\nMilk Type: {milk_type}\nLiters: {liters}\nTotal: ₹{total_amount}"

    # WhatsApp link
    whatsapp_link = f"https://wa.me/919398491466?text={message}"

    # Redirecting to WhatsApp
    return redirect(whatsapp_link)

if __name__ == '__main__':
    app.run(debug=True)
