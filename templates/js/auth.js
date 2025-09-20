// Get all users
function getUsers() {
    return JSON.parse(localStorage.getItem("users")) || {};
}

// Save users
function saveUsers(users) {
    localStorage.setItem("users", JSON.stringify(users));
}
