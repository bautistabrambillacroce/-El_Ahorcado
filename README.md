# 🪓 Juego del Ahorcado con Streamlit

Un juego interactivo del **Ahorcado** desarrollado en Python en un **único archivo** utilizando la librería [Streamlit](https://streamlit.io/).

---

## 🚀 Características

- **Categorías Temáticas:** Elige entre Videojuegos, Películas, Países y Tecnología.
- **Teclado Interactivo:** Botones intuitivos en pantalla con letras deshabilitadas al usarlas.
- **Visualización en ASCII Art:** Representación gráfica del ahorcado que cambia progresivamente a medida que fallas.
- **Manejo de Estado (`st.session_state`):** Mantiene la partida actual de forma fluida sin perder el contexto al interactuar.
- **Totalmente Autocontenido:** Desarrollado en un único archivo ejecutable (`app.py`).

---

## 📋 Requisitos Previos

Necesitas tener instalado Python 3.8 o superior en tu sistema.

---

## 🛠️ Instalación y Ejecución

1. **Instalar Streamlit:**
   Abre tu terminal o consola y ejecuta:
   ```bash
   pip install streamlit
   ```

2. **Ejecutar la Aplicación:**
   En la misma carpeta donde guardaste el archivo `app.py`, ejecuta:
   ```bash
   streamlit run app.py
   ```

3. **Abrir en el Navegador:**
   Streamlit abrirá automáticamente la aplicación en tu navegador predeterminado (normalmente en `http://localhost:8501`).

---

## 📂 Estructura del Proyecto

```text
.
├── app.py        # Código fuente del juego y la interfaz en Streamlit
└── README.md     # Documentación del proyecto
```

---

## 🎮 Reglas del Juego

1. Selecciona una categoría.
2. Tienes **6 intentos** (corazones) para adivinar la palabra secreta.
3. Haz clic en las letras para intentar adivinar.
4. Si adivinas todas las letras antes de agotar tus intentos, ¡ganas!
