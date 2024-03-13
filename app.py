from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Return the HTML form. This should ideally be separated into its own HTML file and used with render_template
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tip Calculator</title>
    <link rel="stylesheet" href="/static/style.css"> <!-- Ensure you have a style.css file in your static folder -->
</head>
<body>

<div class="container">
    <div class="header">
        <h1>Welcome to the Tip Calculator</h1>
        <p>Seamlessly calculate what you have to pay individually</p>
    </div>
    <div class="calculator-form">
        <form action="/calculate" method="post">
            <input type="number" name="total_bill" placeholder="Total Bill" required>
            <input type="number" name="number_of_people" placeholder="Number of People" required min="1">
            <input type="number" name="tip_percentage" placeholder="Tip Percentage (e.g., 10, 12, 15)" required min="1">
            <button type="submit">Calculate</button>
        </form>
    </div>
</div>

</body>
</html>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    total_bill = float(request.form['total_bill'])
    number_of_people = int(request.form['number_of_people'])
    tip_percentage = int(request.form['tip_percentage'])
    
    tip_amount = (tip_percentage / 100) * total_bill
    total_amount = total_bill + tip_amount
    amount_per_person = round(total_amount / number_of_people, 2)
    
    return f'<h1>Result</h1><p>Each person should pay: ${amount_per_person}</p><a href="/">Calculate Again</a>'

if __name__ == '__main__':
    app.run(debug=True)
