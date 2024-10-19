import streamlit as slt

def app():

    slt.title("Meet Our Team")

    cols = slt.columns(5)

    # Nahla Bader
    with cols[0]:
        slt.image("nahla.jpg", width=140)
        slt.markdown("**Nahla Bader**")
        slt.write("team leader and UI/UX developer")

    # Ahmed Sakkijha
    with cols[1]:
        slt.image("image00077.jpeg", width=140)
        slt.markdown("**Ahmed Sakkijha**")
        slt.write(" Frontend & Backend web developer")

    # Abdullah El Hakawati
    with cols[2]:
        slt.image("abd.jpeg", width=140)
        slt.markdown("**Abdullah El Hakawati**")
        slt.write("data collecter & ML")

    # Malek Khalil
    with cols[3]:
        slt.image("malek.jpeg", width=140)
        slt.markdown("**Malek Khalil**")
        slt.write("ML engineer")

    # Lara Abed
    with cols[4]:
        slt.image("la.jpeg", width=140)
        slt.markdown("**Lara Abed**")
        slt.write("docuentation & content writer")
