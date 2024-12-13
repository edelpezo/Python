import streamlit as st
import datetime

st.title('Preferencias del Usuario')

# selector de hora
hora = st.time_input("Seleccione la hora para contactarlo:", datetime.time(9, 00))
st.write("Ha solicitado contactarlo desde:", hora, "horas")

# selector de fecha
fec_nac = st.date_input("Ingrese su fecha de nacimiento", value=None)
st.write("Nació el:", fec_nac)

# botón de carga de archivos
st.write("Puede subir múltiples archivos (PDF, JPG):")
uploaded_files = st.file_uploader("", type="pdf, jpg", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

# slider
mes = st.slider("Seleccione el mes de su nacimiento (de un clic sobre la barra gris):", 1,12)
if mes == 1:
    nom_mes= "Enero";
elif mes == 2:
    nom_mes= "Febrero";
elif mes == 3:
    nom_mes= "Marzo";
elif mes == 4:
    nom_mes= "Abril";
elif mes == 5:
    nom_mes= "Mayo";
elif mes == 6:
    nom_mes= "Junio";
elif mes == 7:
    nom_mes= "Julio";
elif mes == 8:
    nom_mes= "Agosto";
elif mes == 9:
    nom_mes= "Septiembre";
elif mes == 10:
    nom_mes= "Octubre";
elif mes == 11:
    nom_mes= "Noviembre";
else:
    nom_mes= "Diciembre";
st.write("Mes elegido:", nom_mes)

    