import streamlit as st
import numpy as np

# =========================================================
# CONFIGURACIÓN DE LA PÁGINA
# =========================================================

st.set_page_config(
    page_title="VULCANIA AI",
    page_icon="🌋",
    layout="centered"
)

# =========================================================
# TÍTULO
# =========================================================

st.title("🌋 VULCANIA AI")
st.subheader("Centro de Monitoreo Planetario")

st.write(
    "Sistema de simulación y monitoreo de actividad volcánica."
)

st.divider()

# =========================================================
# PARÁMETROS DE MONITOREO
# =========================================================

st.header("📡 Parámetros de Monitoreo")

temperatura = st.slider(
    "🌡️ Temperatura (°C)",
    800,
    1200,
    950
)

presion = st.slider(
    "📈 Presión",
    200,
    500,
    300
)

sismicidad = st.slider(
    "📳 Sismicidad",
    0,
    50,
    20
)

gases = st.slider(
    "💨 Gases",
    300,
    600,
    400
)

st.divider()

# =========================================================
# NIVEL DE ALERTA
# =========================================================

if temperatura > 1050:
    alerta = "Alta"
elif temperatura > 980:
    alerta = "Media"
else:
    alerta = "Baja"

st.header("🚨 Nivel de Alerta")

if alerta == "Baja":

    st.success("🟢 ALERTA BAJA — ESTADO ESTABLE")
    st.image(
        "imagenes/estable.jpg",
        caption="Estado estable"
    )

elif alerta == "Media":

    st.warning("🟡 ALERTA MEDIA — ACTIVIDAD MODERADA")
    st.image(
        "imagenes/media.jpg",
        caption="Actividad volcánica moderada"
    )

else:

    st.error("🔴 ALERTA ALTA — ACTIVIDAD ELEVADA")
    st.image(
        "imagenes/alta.jpg",
        caption="Actividad volcánica elevada"
    )

st.divider()

# =========================================================
# DETECCIÓN DE PATRÓN
# =========================================================

st.header("🔬 Análisis de Señal")

patron_anomalo = abs(np.sin(0.2 * temperatura)) > 0.9

if patron_anomalo:

    st.warning("⚠️ Patrón No Natural Detectado")

    st.image(
        "imagenes/anomalia.jpg",
        caption="Anomalía detectada en la señal"
    )

else:

    st.success("✅ No se detecta un patrón anómalo.")

st.divider()

# =========================================================
# RESUMEN
# =========================================================

st.header("📊 Resumen del Monitoreo")

st.write(f"**Temperatura:** {temperatura} °C")
st.write(f"**Presión:** {presion}")
st.write(f"**Sismicidad:** {sismicidad}")
st.write(f"**Gases:** {gases}")
st.write(f"**Nivel de alerta:** {alerta}")

st.divider()

st.caption(
    "VULCANIA AI — Simulación educativa de monitoreo volcánico"
)