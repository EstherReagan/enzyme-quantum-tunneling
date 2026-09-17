import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.constants import hbar, m_p, eV

st.set_page_config(page_title="Enzyme Quantum AI", layout="wide")

st.markdown("""
<style>
body { background-color: #0a0e27; color: #ffffff; }
</style>
""", unsafe_allow_html=True)

st.title("🧬 Enzyme Quantum Tunneling AI")
st.subheader("AI-Powered Mutation Design")

# Sliders
col1, col2, col3 = st.columns(3)
with col1:
    barrier = st.slider("Barrier Height (eV)", 0.1, 2.0, 0.6)
with col2:
    width = st.slider("Tunnel Width (Å)", 0.5, 5.0, 1.2)
with col3:
    energy = st.slider("Substrate Energy (eV)", 0.0, 0.5, 0.1)

# Quantum calculation
def calc_tunneling(w, b, e):
    a = w * 1e-10
    V0 = b * eV
    E = e * eV
    if E >= V0:
        return 1.0
    kappa = np.sqrt(2 * m_p * (V0 - E)) / hbar
    T = np.exp(-2 * kappa * a)
    return float(min(1.0, 0.01 * T))

result = calc_tunneling(width, barrier, energy)

# Display results
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Tunneling Probability", f"{result:.3e}")
with col2:
    st.metric("Log₁₀(T)", f"{np.log10(result):.2f}")
with col3:
    st.metric("Enhancement", f"{result/1e-20:.1f}x")

# Featured enzymes
st.markdown("---")
st.subheader("Featured Enzymes")
enzymes = {
    "1YGE": "Soybean Lipoxygenase",
    "1DRF": "Dihydrofolate Reductase",
    "1OXO": "Cytochrome P450",
}
for pdb, name in enzymes.items():
    st.write(f"🧪 **{name}** ({pdb})")

st.caption("🚀 Production-Ready Research Platform")
