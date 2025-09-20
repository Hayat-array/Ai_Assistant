document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const email = document.getElementById('email').value.toLowerCase().trim();
    const password = document.getElementById('password').value.trim();

    let users = getUsers(); // Get users from localStorage

    if (users[email] && users[email].password === password) {
        alert('Login successful!');
        // Redirect to AI assistant dashboard
        window.location.href = '/';
    } else {
        alert('Invalid email or password.');
    }
});
