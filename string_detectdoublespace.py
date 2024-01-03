st = "This is a string to detect double  spaces and replace it with single space."
doublespaces = st.find("  ")
st = st.replace("  ", " ")
print(st)