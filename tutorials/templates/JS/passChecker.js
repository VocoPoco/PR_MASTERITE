function checkPasswordStrength() {
    const password = document.getElementById("password").value;
    const strengthIndicator = document.getElementById("password-strength");
  
    // Check password length
    if (password.length < 8) {
      strengthIndicator.innerText = "Password is too short";
      return;
    }
  
    // Check if password contains at least one uppercase letter
    if (!/[A-Z]/.test(password)) {
      strengthIndicator.innerText = "Password should contain at least one uppercase letter";
      return;
    }
  
    // Check if password contains at least one lowercase letter
    if (!/[a-z]/.test(password)) {
      strengthIndicator.innerText = "Password should contain at least one lowercase letter";
      return;
    }
  
    // Check if password contains at least one number
    if (!/\d/.test(password)) {
      strengthIndicator.innerText = "Password should contain at least one number";
      return;
    }
  
    // Check if password contains at least one special character
    if (!/[\W_]/.test(password)) {
      strengthIndicator.innerText = "Password should contain at least one special character";
      return;
    }
  
    strengthIndicator.innerText = "Password is strong!";
  }
  