document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const messageDiv = document.getElementById('message');

    if (password !== confirmPassword) {
        messageDiv.textContent = 'Passwords do not match!';
        messageDiv.style.color = 'red';
    } else {
        messageDiv.textContent = 'Registration successful!';
        messageDiv.style.color = 'green';
    }
});