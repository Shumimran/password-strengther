import streamlit as st
import re   

st.set_page_config(page_title="Password strength checker 🔒")

st.title("🔒 Password Strength Checker")

st.markdown(""" 
## welome to ultimate password strength checker! 👋
Use this simple tool to check the strength of your passward and get suggestion on how to make it stronger🔒 """ ) 

password = st.text_input("Enter your password", type="password")

feedback=[]

score= 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 charactors long.")
    if re.search(r"[A-Z]" ,password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should be contain lowercase and uppercase charactors.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌Password should be contain at least one digit.")
    if re.search(r"[@#$%&*]" , password):
        score += 1
    else:
        feedback.append("❌Password shouid be contain one special charactor (@#$%&*).")
    
    if score == 4:
        feedback.append("✔ Your password is strong! 🎉")
    elif score == 3:
        feedback.append("🟡Your password is medium strength, it could be stronger.")
    else:
        feedback.append("🔴Your password is week. Please mke it stronger.")
        
    if feedback:
        st.markdown("## Improvement suggestion.")
        for tips in feedback:
            st.write(tips)
            
else:
    st.info("Please enter your password to get started.")