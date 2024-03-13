document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {
        const totalBill = parseFloat(document.querySelector('input[name="total_bill"]').value);
        const numberOfPeople = parseInt(document.querySelector('input[name="number_of_people"]').value);
        const tipPercentage = parseInt(document.querySelector('input[name="tip_percentage"]').value);
        
        const tipAmount = (tipPercentage / 100) * totalBill;
        const totalAmount = totalBill + tipAmount;
        const amountPerPerson = (totalAmount / numberOfPeople).toFixed(2);
        
        document.getElementById('result').innerHTML = `Each person should pay: $${amountPerPerson}`;
        
        // Prevent form submission
        return false;
    };
});
