// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the order form element
    const orderForm = document.getElementById('tshirt-order-form');
    
    // Add submit event listener to the form
    orderForm.addEventListener('submit', function(event) {
        // Prevent the default form submission
        event.preventDefault();
        
        // Collect form data
        const formData = new FormData(orderForm);
        const orderData = {};
        
        // Convert FormData to object
        for (const [key, value] of formData.entries()) {
            orderData[key] = value;
        }
        
        // Send data to the server
        fetch('/api/orders', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(orderData)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            // Show success message
            alert('Thank you for your order! We will contact you soon to confirm.');
            // Reset the form
            orderForm.reset();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error processing your order. Please try again.');
        });
    });
});
