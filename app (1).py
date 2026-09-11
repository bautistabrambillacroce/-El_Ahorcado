import streamlit as st
import random

# Configuración de la página
st.set_page_config(
    page_title="Juego del Ahorcado",
    page_icon="🪓",
    layout="centered"
)

# Lista de palabras por categoría
PALABRAS = {
    "🎮 Videojuegos": ["MINECRAFT", "FORTNITE", "POKEMON", "ZELDA", "OVERWATCH", "METROID", "VALORANT", "TERRARIA"],
    "🎬 Películas": ["INCEPTION", "GLADIADOR", "TITANIC", "AVATAR", "INTERSTELLAR", "CORALINE", "MATRIX", "JOKER"],
    "🌍 Países": ["ARGENTINA", "COLOMBIA", "ESPAÑA", "JAPON", "ALEMANIA", "FRANCIA", "MEXICO", "PORTUGAL"],
    "💻 Tecnología": ["PYTHON", "STREAMLIT", "COMPUTADORA", "INTERNET", "PROGRAMACION", "ALGORITMO", "TECLADO", "NUBE"]
}

# Dibujos del ahorcado según los intentos restantes (6 a 0)
AHORCADO_DIBUJOS = [
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """
]

def reiniciar_juego(categoria):
    st.session_state.categoria_actual = categoria
    st.session_state.palabra_secreta = random.choice(PALABRAS[categoria])
    st.session_state.letras_usadas = set()
    st.session_state.intentos_restantes = 6
    st.session_state.juego_terminado = False
    st.session_state.victoria = False

# Estilos CSS personalizados
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .palabra-box {
        font-family: 'Courier New', monospace;
        font-size: 2.5rem;
        letter-spacing: 0.5rem;
        text-align: center;
        background-color: #1e222a;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: #00e676;
    }
</style>
""", unsafe_allow_html=True)

st.title("🪓 Juego del Ahorcado")
st.caption("¡Adivina la palabra antes de que se agoten tus intentos!")

# Selección de categoría
categoria_seleccionada = st.selectbox(
    "Selecciona una categoría:",
    options=list(PALABRAS.keys())
)

# Inicializar o reiniciar si cambia la categoría
if "palabra_secreta" not in st.session_state or st.session_state.get("categoria_actual") != categoria_seleccionada:
    reiniciar_juego(categoria_seleccionada)

# Columnas principales
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Estado")
    st.code(AHORCADO_DIBUJOS[st.session_state.intentos_restantes], language=None)
    st.write(f"❤️ **Intentos restantes:** {st.session_state.intentos_restantes} / 6")

with col2:
    st.subheader("Palabra Secreta")
    
    # Construir palabra oculta
    palabra_oculta = " ".join([letra if letra in st.session_state.letras_usadas else "_" for letra in st.session_state.palabra_secreta])
    st.markdown(f'<div class="palabra-box">{palabra_oculta}</div>', unsafe_allow_html=True)
    
    # Mostrar letras usadas
    letras_usadas_ordenadas = sorted(list(st.session_state.letras_usadas))
    st.write("🔤 **Letras usadas:**", ", ".join(letras_usadas_ordenadas) if letras_usadas_ordenadas else "Ninguna")

# Comprobar estado de victoria
if set(st.session_state.palabra_secreta).issubset(st.session_state.letras_usadas):
    st.session_state.juego_terminado = True
    st.session_state.victoria = True

# Comprobar estado de derrota
if st.session_state.intentos_restantes <= 0:
    st.session_state.juego_terminado = True
    st.session_state.victoria = False

st.divider()

# Teclado interactivo / Control de juego
if not st.session_state.juego_terminado:
    st.subheader("Selecciona una letra:")
    
    # Abecedario en distribución de botones
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    cols = st.columns(9)
    
    for i, letra in enumerate(alfabeto):
        col = cols[i % 9]
        deshabilitado = letra in st.session_state.letras_usadas
        
        if col.button(letra, key=f"btn_{letra}", disabled=deshabilitado, use_container_width=True):
            st.session_state.letras_usadas.add(letra)
            if letra not in st.session_state.palabra_secreta:
                st.session_state.intentos_restantes -= 1
            st.rerun()

else:
    if st.session_state.victoria:
        st.balloons()
        st.success(f"🎉 ¡Felicidades! Adivinaste la palabra: **{st.session_state.palabra_secreta}**")
    else:
        st.error(f"☠️ ¡Has perdido! La palabra era: **{st.session_state.palabra_secreta}**")
        
    if st.button("🔄 Jugar de nuevo", type="primary", use_container_width=True):
        reiniciar_juego(categoria_seleccionada)
        st.rerun()
