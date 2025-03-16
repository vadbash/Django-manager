function togglePassword(fieldId) {
    var inputField = document.getElementById(fieldId);
    if (inputField.type === "password") {
        inputField.type = "text";
    } else {
        inputField.type = "password";
    }
}
