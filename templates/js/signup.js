document.getElementById('signupForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const email = document.getElementById('signupEmail').value.toLowerCase().trim();
    const password = document.getElementById('signupPassword').value.trim();
    const fatherName = document.getElementById('signupFatherName').value.trim();

    if (!email || !password || !fatherName) {
        alert("Please fill in all fields");
        return;
    }

    let users = getUsers(); // Get existing users from localStorage

    if (users[email]) {
        alert("Account already exists!");
        return;
    }

    users[email] = { password, fatherName }; // Add new user
    saveUsers(users); // Save to localStorage

    alert("Signup successful! You can now login.");
    window.location.href = 'login.html';
});
