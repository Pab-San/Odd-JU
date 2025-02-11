import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

formations = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6']
titres = ['Informatique', 'Physique', 'Cybersécurité', 'Electronique', 'Numérique', 'Energie']

sdg_colors = {
    1: '#E5243B', 2: '#DDA63A', 3: '#4C9F38', 4: '#C5192D', 5: '#FF3A21',
    6: '#26BDE2', 7: '#FCC30B', 8: '#A21942', 9: '#FD6925', 10: '#DD1367',
    11: '#FD9D24', 12: '#BF8B2E', 13: '#3F7E44', 14: '#0A97D9', 15: '#56C02B',
    16: '#00689D', 17: '#19486A'
}

st.title("Visualisation des ODD")

uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    for i, formation in enumerate(formations):
        odds = df['ODD'].values
        values = df[formation].values
        colors = [sdg_colors[odd] for odd in odds]
        angles = np.linspace(0, 2 * np.pi, len(odds), endpoint=False)

        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'polar': True})
        ax.bar(angles, values, color=colors, alpha=0.8, edgecolor='white', linewidth=0.7, width=0.37)
        
        # Customize the chart and remove the grid
        ax.set_yticklabels([])
        ax.set_xticks(angles)
        ax.set_xticklabels([f'ODD {odd}' for odd in odds], fontsize=9, va='top')
        ax.xaxis.set_tick_params(pad=8)  #
        ax.grid(True, linewidth=0.1)  # Disable the grid
        ax.spines['polar'].set_linewidth(0.1)  # Adjust line thickness

        ax.set_title("\n\n" + titres[i], fontsize=20, pad=30)

        st.pyplot(fig)
