import streamlit as st
st.title('Datos del usuario')
col1, col2 = st.columns(2)

with col1:  # number_input
    edad = st.number_input("Ingrese su edad:", 0, 100)

with col2:  # text_input
    nombre = st.text_input("Nombres y apellidos:", max_chars=30, 
        placeholder="Ingrese su nombre completo")

col1, col2 = st.columns(2)
with col1: # radio
    genero = st.radio("Género:",
    [":blue[Hombre]",":red[Mujer]",":rainbow[Otro]"],index=None)
    
with col2: # checkbox
    pais = st.selectbox("Seleccione su país:",
    ("Ecuador", "Colombia", "Brasil", "Perú", "Chile"))

col1, col2 = st.columns(2)
with col1: # radio
    agree = st.checkbox("Aceptar términos y condiciones")
    if agree:
        st.write("Ha aceptado")

with col2:# botón
    if st.button("Enviar"):
        col2.markdown("Su información se ha enviado")