import string 
import random
import streamlit as st

import re
# setp 1
def generate_password(length):
    characters = string.digits + string.ascii_letters + "!@#$%^&*"
    return "".join(random.choice(characters) for i in range(length))


# step 2
def check_password_strength(password):
    score = 0
    Common_Passwords = ["12345678","abc123","khan123","pakistan123","password"]
    if password in Common_Passwords:
        return "This password is too common. choose a more unique one.", "weak"

    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    if score == 4:
        return "strong Password!", "strong"
    elif score == 3:
        return "Moderate Password - Consider adding more security features.", "moderate"
    else:
        return "\n".join(feedback), "weak"


check_password = st.text_input("Enter  Your Password", type="password")

if st.button("Check Strength"):
    if check_password:
        result, Strength = check_password_strength(check_password)
        if Strength == "strong":
            st.success(result)
            st.balloons()
        elif Strength == "moderate":
            st.warning(result)
        elif Strength == "weak":
            st.error("weak password . Improve it using these tips:")
            for tip in result.split("\n"):
              st.write("- " + tip)

    else:
        st.warning("Please enter a password.")    


# step 2 comp


# step 1
password_length = st.number_input("Enter the length of password",  min_value=8,max_value=20, value=10 )
if st.button("Generate Password"):
    password = generate_password(password_length)
    st.success (f"{password}")
