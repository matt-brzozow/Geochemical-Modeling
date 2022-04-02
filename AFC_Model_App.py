#####################################################################################################
# Libraries
#####################################################################################################

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#####################################################################################################
# Graph Parameters
#####################################################################################################

# plt.rcParams['font.serif'] = 'Times New Roman' # setting the font as time new roman

plt.rcParams['font.sans-serif'] = 'Arial' # setting the font as Arial

plt.rcParams['xtick.direction'] = "in"
plt.rcParams['ytick.direction'] = "in"

plt.rcParams['ytick.right'] = 'False'
plt.rcParams['xtick.top'] = 'False'

plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 12

# plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['figure.titlesize'] = 12
plt.rcParams["axes.unicode_minus"] = 'False'

#####################################################################################################
# Title
#####################################################################################################

st.title("Bulk-rock Geochemical Modeler")

st.write("-------------")
st.write("")

#####################################################################################################
# Initial melt composition
#####################################################################################################


st.header("Initial Composition")
st.write("")

with st.expander("Starting silicate melt composition (Default is OIB)"):

    col1_a, col2_a, col3_a, col4_a = st.columns([1, 1, 1, 1])

    with col1_a:
        Th_sil_i = st.number_input("Th (ppm)", min_value = 0.0, value = 4.0, key = 0)
        Nb_sil_i = st.number_input("Nb (ppm)", min_value = 0.0, value = 48.0, key = 0)
        La_sil_i = st.number_input("La (ppm)", min_value = 0.0, value = 37.0, key = 0)
        Ce_sil_i = st.number_input("Ce (ppm)", min_value = 0.0, value = 80.0, key = 0)
        Pr_sil_i = st.number_input("Pr (ppm)", min_value = 0.0, value = 9.7, key = 0)
        Nd_sil_i = st.number_input("Nd (ppm)", min_value = 0.0, value = 38.5, key = 0)
    with col2_a:
        Zr_sil_i = st.number_input("Zr (ppm)", min_value = 0.0, value = 280.0, key = 0)
        Hf_sil_i = st.number_input("Hf (ppm)", min_value = 0.0, value = 7.8, key = 0)
        Sm_sil_i = st.number_input("Sm (ppm)", min_value = 0.0, value = 10.0, key = 0)
        Eu_sil_i = st.number_input("Eu (ppm)", min_value = 0.0, value = 3.0, key = 0)
        Ti_sil_i = st.number_input("Ti (ppm)", min_value = 0.0, value = 17200.0, key = 0)
        Gd_sil_i = st.number_input("Gd (ppm)", min_value = 0.0, value = 7.62, key = 0)
    with col3_a:
        Tb_sil_i = st.number_input("Tb (ppm)", min_value = 0.0, value = 1.05, key = 0)
        Dy_sil_i = st.number_input("Dy (ppm)", min_value = 0.0, value = 5.6, key = 0)
        Y_sil_i = st.number_input("Y (ppm)", min_value = 0.0, value = 29.0, key = 0)
        Ho_sil_i = st.number_input("Ho (ppm)", min_value = 0.0, value = 1.06, key = 0)
        Er_sil_i = st.number_input("Er (ppm)", min_value = 0.0, value = 2.62, key = 0)
        Tm_sil_i = st.number_input("Tm (ppm)", min_value = 0.0, value = 0.35, key = 0)
    with col4_a:
        Yb_sil_i = st.number_input("Yb (ppm)", min_value = 0.0, value = 2.16, key = 0)
        Lu_sil_i = st.number_input("Lu (ppm)", min_value = 0.0, value = 0.3, key = 0)
        V_sil_i = st.number_input("V (ppm)", min_value = 0.0, value = 500.0, key = 0)
        Sc_sil_i = st.number_input("Sc (ppm)", min_value = 0.0, value = 100.0, key = 0)

initial_melt = {
"Elements":["Th", "Nb", "La", "Ce", "Pr", "Nd", "Zr", "Hf", "Sm", "Eu", "Ti", "Gd", "Tb", "Dy", "Y", "Ho", "Er", "Tm", "Yb", "Lu", "V", "Sc"],
"Concentration (ppm)":[Th_sil_i, Nb_sil_i, La_sil_i, Ce_sil_i, Pr_sil_i, Nd_sil_i, Zr_sil_i, Hf_sil_i, Sm_sil_i, Eu_sil_i, Ti_sil_i, Gd_sil_i, Tb_sil_i, Dy_sil_i, Y_sil_i, Ho_sil_i, Er_sil_i, Tm_sil_i, Yb_sil_i, Lu_sil_i, V_sil_i, Sc_sil_i]
}

initial_melt_df = pd.DataFrame(data = initial_melt)

st.write("")
st.write("--------------")

#####################################################################################################
# RAYLEIGH FRACTIONAL CRYSTALLIZATION MODEL
#####################################################################################################

st.header("Rayleigh Fractional Crystallization")
st.write("")

#####################################################################################################
# Fractionating minerals
#####################################################################################################

st.sidebar.write("**Choose the minerals that are fractionating**")

P_Cpx = st.sidebar.number_input("Clinopyroxene", 0.0, 1.0, 0.0, 0.05)
P_Pl = st.sidebar.number_input("Plagioclase", 0.0, 1.0, 0.0, 0.05)
P_Opx = st.sidebar.number_input("Orthopyroxene", 0.0, 1.0, 0.0, 0.05)
P_Ol = st.sidebar.number_input("Olivine", 0.0, 1.0, 0.0, 0.05)
P_Mt = st.sidebar.number_input("Magnetite", 0.0, 1.0, 0.0, 0.05)
P_Ilm = st.sidebar.number_input("Ilmenite", 0.0, 1.0, 0.0, 0.05)
P_Ap = st.sidebar.number_input("Apatite", 0.0, 1.0, 0.0, 0.05)
P_Chr = st.sidebar.number_input("Chromite", 0.0, 1.0, 0.0, 0.05)
P_Maj_gn = st.sidebar.number_input("Majorite garnet", 0.0, 1.0, 0.0, 0.05)
P_Amp = st.sidebar.number_input("Amphibole", 0.0, 1.0, 0.0, 0.05)

Total = P_Cpx + P_Pl + P_Opx + P_Ol + P_Mt + P_Ilm + P_Ap + P_Chr + P_Maj_gn + P_Amp
st.sidebar.write(f"Total minerals fractionating  =  {Total}")
st.sidebar.write("*The total minerals fractionating should not be greater than 1*")

st.sidebar.write("--------------")
st.sidebar.write("")

st.sidebar.write("**Created by:**")
st.sidebar.write("***Matthew Brzozowski, PhD***")
st.sidebar.write("***matt.brzozow@gmail.com***")

#####################################################################################################
# Partition coefficients
#####################################################################################################

# Partition coefficients for different minerals

# Kd values from Bedard et al. (2009) --> Most minerals
    # The D values are appropriate for a system corresponding to a rock with molar An = 0.709, clinopyroxene Aliv = 0.04, and melt MgO = 5.47 and SiO2 = 53.6 wt.%.
# Kd values from Corgne and Wood (2004) --> Majorite garnet
    # Fe-, Al-rich peridotite
# Kd values from McKenzie and O'Nions (1991) --> Amphibole
    # Basalt

D_Th_Cpx = 0.0225   # Bedard et al. (2009)
D_Nb_Cpx = 0.0098   # Bedard et al. (2009)
D_La_Cpx = 0.1      # Bedard et al. (2009)
D_Ce_Cpx = 0.16     # Bedard et al. (2009)
D_Nd_Cpx = 0.338    # Bedard et al. (2009)
D_Zr_Cpx = 0.022    # Bedard et al. (2009)
D_Sm_Cpx = 0.53     # Bedard et al. (2009)
D_Eu_Cpx = 0.04     # Bedard et al. (2009)
D_Ti_Cpx = 0.213    # Bedard et al. (2009)
D_Gd_Cpx = 0.673    # Bedard et al. (2009)
D_Tb_Cpx = 0.721    # Bedard et al. (2009)
D_Y_Cpx = 0.752     # Bedard et al. (2009)
D_Yb_Cpx = 0.678    # Bedard et al. (2009)
D_Lu_Cpx = 0.642    # Bedard et al. (2009)
D_V_Cpx = 0.49      # Bedard et al. (2009)
D_Pr_Cpx = 0.240    # Bedard et al. (2009)
D_Dy_Cpx = 0.747    # Bedard et al. (2009)
D_Ho_Cpx = 0.751    # Bedard et al. (2009)  
D_Er_Cpx = 0.737    # Bedard et al. (2009)
D_Tm_Cpx = 0.711    # Bedard et al. (2009)
D_Sc_Cpx = 1.11     # Bedard et al. (2009)
D_Hf_Cpx = 0.050    # Bedard et al. (2009)
  
D_Th_Pl = 0.0162    # Bedard et al. (2009)
D_Nb_Pl = 0.00328   # Bedard et al. (2009)
D_La_Pl = 0.0238    # Bedard et al. (2009)
D_Ce_Pl = 0.036     # Bedard et al. (2009)
D_Nd_Pl = 0.0111    # Bedard et al. (2009)
D_Zr_Pl = 0.00048   # Bedard et al. (2009)
D_Sm_Pl = 0.0141    # Bedard et al. (2009)
D_Eu_Pl = 0.0872    # Bedard et al. (2009)
D_Ti_Pl = 0.0243    # Bedard et al. (2009)
D_Gd_Pl = 0.0223    # Bedard et al. (2009)
D_Tb_Pl = 0.0118    # Bedard et al. (2009)
D_Y_Pl = 0.0087     # Bedard et al. (2009)
D_Yb_Pl = 0.0039    # Bedard et al. (2009)
D_Lu_Pl = 0.0038    # Bedard et al. (2009)
D_V_Pl = 0          # Bedard et al. (2009)
D_Pr_Pl = 0.0271    # Bedard et al. (2009)
D_Dy_Pl = 0.0159    # Bedard et al. (2009)
D_Ho_Pl = 0.0256    # Bedard et al. (2009)
D_Er_Pl = 0.0115    # Bedard et al. (2009)
D_Tm_Pl = 0.0192    # Bedard et al. (2009)
D_Sc_Pl = 0.00106   # Bedard et al. (2009)
D_Hf_Pl = 0.0042    # Bedard et al. (2009)

D_Th_Opx = 0.0064   # Bedard et al. (2009)
D_Nb_Opx = 0.015    # Bedard et al. (2009)
D_La_Opx = 0.00328  # Bedard et al. (2009)
D_Ce_Opx = 0.00552  # Bedard et al. (2009)
D_Nd_Opx = 0.0142   # Bedard et al. (2009)
D_Zr_Opx = 0.0167   # Bedard et al. (2009)
D_Sm_Opx = 0.0293   # Bedard et al. (2009)
D_Eu_Opx = 0.0227   # Bedard et al. (2009)
D_Ti_Opx = 0.201    # Bedard et al. (2009)
D_Gd_Opx = 0.051    # Bedard et al. (2009)
D_Tb_Opx = 0.0656   # Bedard et al. (2009)
D_Y_Opx = 0.0953    # Bedard et al. (2009)
D_Yb_Opx = 0.16     # Bedard et al. (2009)
D_Lu_Opx = 0.177    # Bedard et al. (2009)
D_V_Opx = 0.453     # Bedard et al. (2009)
D_Pr_Opx = 0.0090   # Bedard et al. (2009)
D_Dy_Opx = 0.0831   # Bedard et al. (2009)
D_Ho_Opx = 0.102    # Bedard et al. (2009)
D_Er_Opx = 0.121    # Bedard et al. (2009)
D_Tm_Opx = 0.141    # Bedard et al. (2009)
D_Sc_Opx = 1.068    # Bedard et al. (2009)
D_Hf_Opx = 0.0408   # Bedard et al. (2009)

D_Th_Ol = 0.0346    # Bedard et al. (2009)
D_Nb_Ol = 0.00491   # Bedard et al. (2009)
D_La_Ol = 0.00008   # Bedard et al. (2009)
D_Ce_Ol = 0.00019   # Bedard et al. (2009)
D_Nd_Ol = 0.00093   # Bedard et al. (2009)
D_Zr_Ol = 0.0319    # Bedard et al. (2009)
D_Sm_Ol = 0.0031    # Bedard et al. (2009)
D_Eu_Ol = 0.0111    # Bedard et al. (2009)
D_Ti_Ol = 0.0334    # Bedard et al. (2009)
D_Gd_Ol = 0.00784   # Bedard et al. (2009)
D_Tb_Ol = 0.0119    # Bedard et al. (2009)
D_Y_Ol = 0.0222     # Bedard et al. (2009)
D_Yb_Ol = 0.0521    # Bedard et al. (2009)
D_Lu_Ol = 0.0621    # Bedard et al. (2009)
D_V_Ol = 0.15       # Bedard et al. (2009)
D_Pr_Ol = 0.00043   # Bedard et al. (2009)
D_Dy_Ol = 0.0177    # Bedard et al. (2009)
D_Ho_Ol = 0.0247    # Bedard et al. (2009)
D_Er_Ol = 0.0330    # Bedard et al. (2009)
D_Tm_Ol = 0.0423    # Bedard et al. (2009)
D_Sc_Ol = 0.29      # Bedard et al. (2009)
D_Hf_Ol = 0.0139    # Bedard et al. (2009)

D_Th_Mt = 0.0077    # Bedard et al. (2009)
D_Nb_Mt = 0.0764    # Bedard et al. (2009)
D_La_Mt = 0.015     # Bedard et al. (2009)
D_Ce_Mt = 0.016     # Bedard et al. (2009)
D_Nd_Mt = 0.026     # Bedard et al. (2009)
D_Zr_Mt = 0.084     # Bedard et al. (2009)
D_Sm_Mt = 0.024     # Bedard et al. (2009)
D_Eu_Mt = 0.025     # Bedard et al. (2009)
D_Ti_Mt = 1.49      # Bedard et al. (2009)
D_Gd_Mt = 0.018     # Bedard et al. (2009)
D_Tb_Mt = 0.019     # Bedard et al. (2009)
D_Y_Mt = 0.018      # Bedard et al. (2009)
D_Yb_Mt = 0.018     # Bedard et al. (2009)
D_Lu_Mt = 0.018     # Bedard et al. (2009)
D_V_Mt = 0.64       # Bedard et al. (2009)
D_Pr_Mt = 0.018     # Bedard et al. (2009)
D_Dy_Mt = 0.018     # Bedard et al. (2009)
D_Ho_Mt = 0.018     # Bedard et al. (2009)
D_Er_Mt = 0.018     # Bedard et al. (2009)
D_Tm_Mt = 0.018     # Bedard et al. (2009)
D_Sc_Mt = 1.10      # Bedard et al. (2009)
D_Hf_Mt = 0.076     # Bedard et al. (2009)

D_Th_Ilm = 0.105    # Bedard et al. (2009)
D_Nb_Ilm = 1.62     # Bedard et al. (2009)
D_La_Ilm = 0.0027   # Bedard et al. (2009)
D_Ce_Ilm = 0.0046   # Bedard et al. (2009)
D_Nd_Ilm = 0.012    # Bedard et al. (2009)
D_Zr_Ilm = 0.35     # Bedard et al. (2009)
D_Sm_Ilm = 0.025    # Bedard et al. (2009)
D_Eu_Ilm = 0.0028   # Bedard et al. (2009)
D_Ti_Ilm = float()
D_Gd_Ilm = 0.0428   # Bedard et al. (2009)
D_Tb_Ilm = 0.0546   # Bedard et al. (2009)
D_Y_Ilm = 0.0777    # Bedard et al. (2009)
D_Yb_Ilm = 0.125    # Bedard et al. (2009)
D_Lu_Ilm = 0.137    # Bedard et al. (2009)
D_V_Ilm = 10.3      # Bedard et al. (2009)
D_Pr_Ilm = 0.0076   # Bedard et al. (2009)
D_Dy_Ilm = 0.0683   # Bedard et al. (2009)
D_Ho_Ilm = 0.0827   # Bedard et al. (2009)
D_Er_Ilm = 0.0971   # Bedard et al. (2009)
D_Tm_Ilm = 0.111    # Bedard et al. (2009)
D_Sc_Ilm = 1.91     # Bedard et al. (2009)
D_Hf_Ilm = 0.42     # Bedard et al. (2009)

D_Th_Ap = 0.835     # Bedard et al. (2009)
D_Nb_Ap = 0.00295   # Bedard et al. (2009)
D_La_Ap = 2.425     # Bedard et al. (2009)
D_Ce_Ap = 2.78      # Bedard et al. (2009)
D_Nd_Ap = 16.8      # Bedard et al. (2009)
D_Zr_Ap = 0.067     # Bedard et al. (2009)
D_Sm_Ap = 4.67      # Bedard et al. (2009)
D_Eu_Ap = 7.36      # Bedard et al. (2009)
D_Ti_Ap = 0.047     # Bedard et al. (2009)
D_Gd_Ap = 4.05      # Bedard et al. (2009)
D_Tb_Ap = 15.2      # Bedard et al. (2009)
D_Y_Ap = 2.285      # Bedard et al. (2009)
D_Yb_Ap = 1.5       # Bedard et al. (2009)
D_Lu_Ap = 0.96      # Bedard et al. (2009)
D_V_Ap = 0.022      # Bedard et al. (2009)
D_Pr_Ap = 14.0      # Bedard et al. (2009)
D_Dy_Ap = 12.9      # Bedard et al. (2009)
D_Ho_Ap = 10.8      # Bedard et al. (2009)
D_Er_Ap = 8.79      # Bedard et al. (2009)
D_Tm_Ap = 7.14      # Bedard et al. (2009)  
D_Sc_Ap = 0.0258    # Bedard et al. (2009)  
D_Hf_Ap = 89        # Bedard et al. (2009)  

D_Th_Chr = 0.001    # Bedard et al. (2009)
D_Nb_Chr = 0.01     # Bedard et al. (2009)
D_La_Chr = 0.0006   # Bedard et al. (2009)
D_Ce_Chr = 0.0006   # Bedard et al. (2009)
D_Nd_Chr = 0.0006   # Bedard et al. (2009)
D_Zr_Chr = 0.015    # Bedard et al. (2009)
D_Sm_Chr = 0.0006   # Bedard et al. (2009)
D_Eu_Chr = 0.0006   # Bedard et al. (2009)
D_Ti_Chr = 0.125    # Bedard et al. (2009)
D_Gd_Chr = 0.0006   # Bedard et al. (2009)
D_Tb_Chr = 0.0011   # Bedard et al. (2009)
D_Y_Chr = 0.002     # Bedard et al. (2009)
D_Yb_Chr = 0.0045   # Bedard et al. (2009)
D_Lu_Chr = 0.0045   # Bedard et al. (2009)
D_V_Chr = 10        # Bedard et al. (2009)
D_Pr_Chr = 0.0006   # Bedard et al. (2009)
D_Dy_Chr = 0.0015   # Bedard et al. (2009)
D_Ho_Chr = 0.0023   # Bedard et al. (2009)
D_Er_Chr = 0.003    # Bedard et al. (2009)
D_Tm_Chr = 0.0038   # Bedard et al. (2009)
D_Sc_Chr = 0.1      # Bedard et al. (2009)
D_Hf_Chr = 0.015    # Bedard et al. (2009)

D_Th_Maj_gn = float()
D_Nb_Maj_gn = 0.0022   # Bobrov et al. (2014) --> run 2322
D_La_Maj_gn = 0.0011   # Bobrov et al. (2014) --> run 2322
D_Ce_Maj_gn = 0.0016   # Bobrov et al. (2014) --> run 2322
D_Nd_Maj_gn = 0.0058   # Bobrov et al. (2014) --> run 2322
D_Zr_Maj_gn = 0.174    # Bobrov et al. (2014) --> run 2322
D_Sm_Maj_gn = 0.027    # Bobrov et al. (2014) --> run 2322
D_Eu_Maj_gn = 0.059    # Bobrov et al. (2014) --> run 2322
D_Ti_Maj_gn = float()
D_Gd_Maj_gn = 0.099    # Bobrov et al. (2014) --> run 2322
D_Tb_Maj_gn = 0.201    # Bobrov et al. (2014) --> run 2322
D_Y_Maj_gn = 0.556     # Bobrov et al. (2014) --> run 2322
D_Yb_Maj_gn = 1.62     # Bobrov et al. (2014) --> run 2322
D_Lu_Maj_gn = 1.97     # Bobrov et al. (2014) --> run 2322
D_V_Maj_gn = float()
D_Pr_Maj_gn = 0.0022   # Bobrov et al. (2014) --> run 2322
D_Dy_Maj_gn = 0.342    # Bobrov et al. (2014) --> run 2322
D_Ho_Maj_gn = 0.551    # Bobrov et al. (2014) --> run 2322
D_Er_Maj_gn = 0.848    # Bobrov et al. (2014) --> run 2322
D_Tm_Maj_gn = 1.17     # Bobrov et al. (2014) --> run 2322
D_Sc_Maj_gn = 2.69     # Bobrov et al. (2014) --> run 2322
D_Hf_Maj_gn = 0.144    # Bobrov et al. (2014) --> run 2322

D_Th_Amp = float()
D_Nb_Amp = float() 
D_La_Amp = 0.17        # McKenzie and O'Nions (1991)
D_Ce_Amp = 0.26        # McKenzie and O'Nions (1991)
D_Nd_Amp = 0.44        # McKenzie and O'Nions (1991)
D_Zr_Amp = float()     # McKenzie and O'Nions (1991)
D_Sm_Amp = 0.76        # McKenzie and O'Nions (1991)
D_Eu_Amp = 0.88        # McKenzie and O'Nions (1991)
D_Ti_Amp = 0.69        # McKenzie and O'Nions (1991)
D_Gd_Amp = 0.86        # McKenzie and O'Nions (1991)
D_Tb_Amp = 0.83        # McKenzie and O'Nions (1991)
D_Y_Amp = float()      
D_Yb_Amp = 0.59        # McKenzie and O'Nions (1991)
D_Lu_Amp = 0.51        # McKenzie and O'Nions (1991)
D_V_Amp = float()
D_Pr_Amp = 0.35        # McKenzie and O'Nions (1991)
D_Dy_Amp = 0.78        # McKenzie and O'Nions (1991)
D_Ho_Amp = 0.73        # McKenzie and O'Nions (1991)
D_Er_Amp = 0.68        # McKenzie and O'Nions (1991)
D_Tm_Amp = 0.64        # McKenzie and O'Nions (1991)
D_Sc_Amp = float()
D_Hf_Amp = float()

#####################################################################################################
# Bulk partition coefficients
#####################################################################################################

D_Th_bulk = (P_Cpx * D_Th_Cpx) + (P_Pl * D_Th_Pl) + (P_Opx * D_Th_Opx) + (P_Ol * D_Th_Ol) + (P_Mt * D_Th_Mt) + (P_Ilm * D_Th_Ilm) + (P_Ap * D_Th_Ap) + (P_Chr * D_Th_Chr) + (P_Maj_gn * D_Th_Maj_gn) + (P_Amp * D_Th_Amp)
D_Nb_bulk = (P_Cpx * D_Nb_Cpx) + (P_Pl * D_Nb_Pl) + (P_Opx * D_Nb_Opx) + (P_Ol * D_Nb_Ol) + (P_Mt * D_Nb_Mt) + (P_Ilm * D_Nb_Ilm) + (P_Ap * D_Nb_Ap) + (P_Chr * D_Nb_Chr) + (P_Maj_gn * D_Nb_Maj_gn) + (P_Amp * D_Nb_Amp)
D_La_bulk = (P_Cpx * D_La_Cpx) + (P_Pl * D_La_Pl) + (P_Opx * D_La_Opx) + (P_Ol * D_La_Ol) + (P_Mt * D_La_Mt) + (P_Ilm * D_La_Ilm) + (P_Ap * D_La_Ap) + (P_Chr * D_La_Chr) + (P_Maj_gn * D_La_Maj_gn) + (P_Amp * D_La_Amp)
D_Ce_bulk = (P_Cpx * D_Ce_Cpx) + (P_Pl * D_Ce_Pl) + (P_Opx * D_Ce_Opx) + (P_Ol * D_Ce_Ol) + (P_Mt * D_Ce_Mt) + (P_Ilm * D_Ce_Ilm) + (P_Ap * D_Ce_Ap) + (P_Chr * D_Ce_Chr) + (P_Maj_gn * D_Ce_Maj_gn) + (P_Amp * D_Ce_Amp)
D_Pr_bulk = (P_Cpx * D_Pr_Cpx) + (P_Pl * D_Pr_Pl) + (P_Opx * D_Pr_Opx) + (P_Ol * D_Pr_Ol) + (P_Mt * D_Pr_Mt) + (P_Ilm * D_Pr_Ilm) + (P_Ap * D_Pr_Ap) + (P_Chr * D_Pr_Chr) + (P_Maj_gn * D_Pr_Maj_gn) + (P_Amp * D_Pr_Amp)
D_Nd_bulk = (P_Cpx * D_Nd_Cpx) + (P_Pl * D_Nd_Pl) + (P_Opx * D_Nd_Opx) + (P_Ol * D_Nd_Ol) + (P_Mt * D_Nd_Mt) + (P_Ilm * D_Nd_Ilm) + (P_Ap * D_Nd_Ap) + (P_Chr * D_Nd_Chr) + (P_Maj_gn * D_Nd_Maj_gn) + (P_Amp * D_Nd_Amp)
D_Zr_bulk = (P_Cpx * D_Zr_Cpx) + (P_Pl * D_Zr_Pl) + (P_Opx * D_Zr_Opx) + (P_Ol * D_Zr_Ol) + (P_Mt * D_Zr_Mt) + (P_Ilm * D_Zr_Ilm) + (P_Ap * D_Zr_Ap) + (P_Chr * D_Zr_Chr) + (P_Maj_gn * D_Zr_Maj_gn) + (P_Amp * D_Zr_Amp)
D_Hf_bulk = (P_Cpx * D_Hf_Cpx) + (P_Pl * D_Hf_Pl) + (P_Opx * D_Hf_Opx) + (P_Ol * D_Hf_Ol) + (P_Mt * D_Hf_Mt) + (P_Ilm * D_Hf_Ilm) + (P_Ap * D_Hf_Ap) + (P_Chr * D_Hf_Chr) + (P_Maj_gn * D_Hf_Maj_gn) + (P_Amp * D_Hf_Amp)
D_Sm_bulk = (P_Cpx * D_Sm_Cpx) + (P_Pl * D_Sm_Pl) + (P_Opx * D_Sm_Opx) + (P_Ol * D_Sm_Ol) + (P_Mt * D_Sm_Mt) + (P_Ilm * D_Sm_Ilm) + (P_Ap * D_Sm_Ap) + (P_Chr * D_Sm_Chr) + (P_Maj_gn * D_Sm_Maj_gn) + (P_Amp * D_Sm_Amp)
D_Eu_bulk = (P_Cpx * D_Eu_Cpx) + (P_Pl * D_Eu_Pl) + (P_Opx * D_Eu_Opx) + (P_Ol * D_Eu_Ol) + (P_Mt * D_Eu_Mt) + (P_Ilm * D_Eu_Ilm) + (P_Ap * D_Eu_Ap) + (P_Chr * D_Eu_Chr) + (P_Maj_gn * D_Eu_Maj_gn) + (P_Amp * D_Eu_Amp)
D_Ti_bulk = (P_Cpx * D_Ti_Cpx) + (P_Pl * D_Ti_Pl) + (P_Opx * D_Ti_Opx) + (P_Ol * D_Ti_Ol) + (P_Mt * D_Ti_Mt) + (P_Ilm * D_Ti_Ilm) + (P_Ap * D_Ti_Ap) + (P_Chr * D_Ti_Chr) + (P_Maj_gn * D_Ti_Maj_gn) + (P_Amp * D_Ti_Amp)
D_Gd_bulk = (P_Cpx * D_Gd_Cpx) + (P_Pl * D_Gd_Pl) + (P_Opx * D_Gd_Opx) + (P_Ol * D_Gd_Ol) + (P_Mt * D_Gd_Mt) + (P_Ilm * D_Gd_Ilm) + (P_Ap * D_Gd_Ap) + (P_Chr * D_Gd_Chr) + (P_Maj_gn * D_Gd_Maj_gn) + (P_Amp * D_Gd_Amp)
D_Tb_bulk = (P_Cpx * D_Tb_Cpx) + (P_Pl * D_Tb_Pl) + (P_Opx * D_Tb_Opx) + (P_Ol * D_Tb_Ol) + (P_Mt * D_Tb_Mt) + (P_Ilm * D_Tb_Ilm) + (P_Ap * D_Tb_Ap) + (P_Chr * D_Tb_Chr) + (P_Maj_gn * D_Tb_Maj_gn) + (P_Amp * D_Tb_Amp)
D_Dy_bulk = (P_Cpx * D_Dy_Cpx) + (P_Pl * D_Dy_Pl) + (P_Opx * D_Dy_Opx) + (P_Ol * D_Dy_Ol) + (P_Mt * D_Dy_Mt) + (P_Ilm * D_Dy_Ilm) + (P_Ap * D_Dy_Ap) + (P_Chr * D_Dy_Chr) + (P_Maj_gn * D_Dy_Maj_gn) + (P_Amp * D_Dy_Amp)
D_Y_bulk = (P_Cpx * D_Y_Cpx) + (P_Pl * D_Y_Pl) + (P_Opx * D_Y_Opx) + (P_Ol * D_Y_Ol) + (P_Mt * D_Y_Mt) + (P_Ilm * D_Y_Ilm) + (P_Ap * D_Y_Ap) + (P_Chr * D_Y_Chr) + (P_Maj_gn * D_Y_Maj_gn) + (P_Amp * D_Y_Amp)
D_Ho_bulk = (P_Cpx * D_Ho_Cpx) + (P_Pl * D_Ho_Pl) + (P_Opx * D_Ho_Opx) + (P_Ol * D_Ho_Ol) + (P_Mt * D_Ho_Mt) + (P_Ilm * D_Ho_Ilm) + (P_Ap * D_Ho_Ap) + (P_Chr * D_Ho_Chr) + (P_Maj_gn * D_Ho_Maj_gn) + (P_Amp * D_Ho_Amp)
D_Er_bulk = (P_Cpx * D_Er_Cpx) + (P_Pl * D_Er_Pl) + (P_Opx * D_Er_Opx) + (P_Ol * D_Er_Ol) + (P_Mt * D_Er_Mt) + (P_Ilm * D_Er_Ilm) + (P_Ap * D_Er_Ap) + (P_Chr * D_Er_Chr) + (P_Maj_gn * D_Er_Maj_gn) + (P_Amp * D_Er_Amp)
D_Tm_bulk = (P_Cpx * D_Tm_Cpx) + (P_Pl * D_Tm_Pl) + (P_Opx * D_Tm_Opx) + (P_Ol * D_Tm_Ol) + (P_Mt * D_Tm_Mt) + (P_Ilm * D_Tm_Ilm) + (P_Ap * D_Tm_Ap) + (P_Chr * D_Tm_Chr) + (P_Maj_gn * D_Tm_Maj_gn) + (P_Amp * D_Tm_Amp)
D_Yb_bulk = (P_Cpx * D_Yb_Cpx) + (P_Pl * D_Yb_Pl) + (P_Opx * D_Yb_Opx) + (P_Ol * D_Yb_Ol) + (P_Mt * D_Yb_Mt) + (P_Ilm * D_Yb_Ilm) + (P_Ap * D_Yb_Ap) + (P_Chr * D_Yb_Chr) + (P_Maj_gn * D_Yb_Maj_gn) + (P_Amp * D_Yb_Amp)
D_Lu_bulk = (P_Cpx * D_Lu_Cpx) + (P_Pl * D_Lu_Pl) + (P_Opx * D_Lu_Opx) + (P_Ol * D_Lu_Ol) + (P_Mt * D_Lu_Mt) + (P_Ilm * D_Lu_Ilm) + (P_Ap * D_Lu_Ap) + (P_Chr * D_Lu_Chr) + (P_Maj_gn * D_Lu_Maj_gn) + (P_Amp * D_Lu_Amp)
D_V_bulk = (P_Cpx * D_V_Cpx) + (P_Pl * D_V_Pl) + (P_Opx * D_V_Opx) + (P_Ol * D_V_Ol) + (P_Mt * D_V_Mt) + (P_Ilm * D_V_Ilm) + (P_Ap * D_V_Ap) + (P_Chr * D_V_Chr) + (P_Maj_gn * D_V_Maj_gn) + (P_Amp * D_V_Amp)
D_Sc_bulk = (P_Cpx * D_Sc_Cpx) + (P_Pl * D_Sc_Pl) + (P_Opx * D_Sc_Opx) + (P_Ol * D_Sc_Ol) + (P_Mt * D_Sc_Mt) + (P_Ilm * D_Sc_Ilm) + (P_Ap * D_Sc_Ap) + (P_Chr * D_Sc_Chr) + (P_Maj_gn * D_Sc_Maj_gn) + (P_Amp * D_Sc_Amp)

#####################################################################################################
# Residual melt calculation
#####################################################################################################

F_sil_remaining = np.arange(0.1, 1.0+0.001, 0.001)

Th_sil_f = Th_sil_i * (F_sil_remaining ** (D_Th_bulk - 1))
Nb_sil_f = Nb_sil_i * (F_sil_remaining ** (D_Nb_bulk - 1))
La_sil_f = La_sil_i * (F_sil_remaining ** (D_La_bulk - 1))
Ce_sil_f = Ce_sil_i * (F_sil_remaining ** (D_Ce_bulk - 1))
Pr_sil_f = Pr_sil_i * (F_sil_remaining ** (D_Pr_bulk - 1))
Nd_sil_f = Nd_sil_i * (F_sil_remaining ** (D_Nd_bulk - 1))
Zr_sil_f = Zr_sil_i * (F_sil_remaining ** (D_Zr_bulk - 1))
Hf_sil_f = Hf_sil_i * (F_sil_remaining ** (D_Hf_bulk - 1))
Sm_sil_f = Sm_sil_i * (F_sil_remaining ** (D_Sm_bulk - 1))
Eu_sil_f = Eu_sil_i * (F_sil_remaining ** (D_Eu_bulk - 1))
Ti_sil_f = Ti_sil_i * (F_sil_remaining ** (D_Ti_bulk - 1))
Gd_sil_f = Gd_sil_i * (F_sil_remaining ** (D_Gd_bulk - 1))
Tb_sil_f = Tb_sil_i * (F_sil_remaining ** (D_Tb_bulk - 1))
Dy_sil_f = Dy_sil_i * (F_sil_remaining ** (D_Dy_bulk - 1))
Y_sil_f = Y_sil_i * (F_sil_remaining ** (D_Y_bulk - 1))
Ho_sil_f = Ho_sil_i * (F_sil_remaining ** (D_Ho_bulk - 1))
Er_sil_f = Er_sil_i * (F_sil_remaining ** (D_Er_bulk - 1))
Tm_sil_f = Tm_sil_i * (F_sil_remaining ** (D_Tm_bulk - 1))
Yb_sil_f = Yb_sil_i * (F_sil_remaining ** (D_Yb_bulk - 1))
Lu_sil_f = Lu_sil_i * (F_sil_remaining ** (D_Lu_bulk - 1))
V_sil_f = V_sil_i * (F_sil_remaining ** (D_V_bulk - 1))
Sc_sil_f = Sc_sil_i * (F_sil_remaining ** (D_Sc_bulk - 1))

#####################################################################################################
# Cumulate melt calculation
#####################################################################################################

Th_sol = ((1 - (F_sil_remaining ** D_Th_bulk)) / (1 - F_sil_remaining)) * Th_sil_i
Nb_sol = ((1 - (F_sil_remaining ** D_Nb_bulk)) / (1 - F_sil_remaining)) * Nb_sil_i
La_sol = ((1 - (F_sil_remaining ** D_La_bulk)) / (1 - F_sil_remaining)) * La_sil_i
Ce_sol = ((1 - (F_sil_remaining ** D_Ce_bulk)) / (1 - F_sil_remaining)) * Ce_sil_i
Pr_sol = ((1 - (F_sil_remaining ** D_Pr_bulk)) / (1 - F_sil_remaining)) * Pr_sil_i
Nd_sol = ((1 - (F_sil_remaining ** D_Nd_bulk)) / (1 - F_sil_remaining)) * Nd_sil_i
Zr_sol = ((1 - (F_sil_remaining ** D_Zr_bulk)) / (1 - F_sil_remaining)) * Zr_sil_i
Hf_sol = ((1 - (F_sil_remaining ** D_Hf_bulk)) / (1 - F_sil_remaining)) * Hf_sil_i
Sm_sol = ((1 - (F_sil_remaining ** D_Sm_bulk)) / (1 - F_sil_remaining)) * Sm_sil_i
Eu_sol = ((1 - (F_sil_remaining ** D_Eu_bulk)) / (1 - F_sil_remaining)) * Eu_sil_i
Ti_sol = ((1 - (F_sil_remaining ** D_Ti_bulk)) / (1 - F_sil_remaining)) * Ti_sil_i
Gd_sol = ((1 - (F_sil_remaining ** D_Gd_bulk)) / (1 - F_sil_remaining)) * Gd_sil_i
Tb_sol = ((1 - (F_sil_remaining ** D_Tb_bulk)) / (1 - F_sil_remaining)) * Tb_sil_i
Dy_sol = ((1 - (F_sil_remaining ** D_Dy_bulk)) / (1 - F_sil_remaining)) * Dy_sil_i
Y_sol = ((1 - (F_sil_remaining ** D_Y_bulk)) / (1 - F_sil_remaining)) * Y_sil_i
Ho_sol = ((1 - (F_sil_remaining ** D_Ho_bulk)) / (1 - F_sil_remaining)) * Ho_sil_i
Er_sol = ((1 - (F_sil_remaining ** D_Er_bulk)) / (1 - F_sil_remaining)) * Er_sil_i
Tm_sol = ((1 - (F_sil_remaining ** D_Tm_bulk)) / (1 - F_sil_remaining)) * Tm_sil_i
Yb_sol = ((1 - (F_sil_remaining ** D_Yb_bulk)) / (1 - F_sil_remaining)) * Yb_sil_i
Lu_sol = ((1 - (F_sil_remaining ** D_Lu_bulk)) / (1 - F_sil_remaining)) * Lu_sil_i
V_sol = ((1 - (F_sil_remaining ** D_V_bulk)) / (1 - F_sil_remaining)) * V_sil_i
Sc_sol = ((1 - (F_sil_remaining ** D_Sc_bulk)) / (1 - F_sil_remaining)) * Sc_sil_i

#####################################################################################################
# Combine RFC model results
#####################################################################################################

RFC_results_df = pd.DataFrame()
RFC_results_df["F_sil_remaining"] = F_sil_remaining
RFC_results_df["Th_sil_f"] = Th_sil_f
RFC_results_df["Nb_sil_f"] = Nb_sil_f
RFC_results_df["La_sil_f"] = La_sil_f
RFC_results_df["Ce_sil_f"] = Ce_sil_f
RFC_results_df["Pr_sil_f"] = Pr_sil_f
RFC_results_df["Nd_sil_f"] = Nd_sil_f
RFC_results_df["Zr_sil_f"] = Zr_sil_f
RFC_results_df["Hf_sil_f"] = Hf_sil_f
RFC_results_df["Sm_sil_f"] = Sm_sil_f
RFC_results_df["Eu_sil_f"] = Eu_sil_f
RFC_results_df["Ti_sil_f"] = Ti_sil_f
RFC_results_df["Gd_sil_f"] = Gd_sil_f
RFC_results_df["Tb_sil_f"] = Tb_sil_f
RFC_results_df["Dy_sil_f"] = Dy_sil_f
RFC_results_df["Y_sil_f"] = Y_sil_f
RFC_results_df["Ho_sil_f"] = Ho_sil_f
RFC_results_df["Er_sil_f"] = Er_sil_f
RFC_results_df["Tm_sil_f"] = Tm_sil_f
RFC_results_df["Yb_sil_f"] = Yb_sil_f
RFC_results_df["Lu_sil_f"] = Lu_sil_f
RFC_results_df["V_sil_f"] = V_sil_f
RFC_results_df["Sc_sil_f"] = Sc_sil_f
RFC_results_df["La_sil_f/Sm_sil_f"] = RFC_results_df.La_sil_f / RFC_results_df.Sm_sil_f
RFC_results_df["La_sil_f/Lu_sil_f"] = RFC_results_df.La_sil_f / RFC_results_df.Lu_sil_f
RFC_results_df["Gd_sil_f/Yb_sil_f"] = RFC_results_df.Gd_sil_f / RFC_results_df.Yb_sil_f
RFC_results_df["Th_sil_f/Nb_sil_f"] = RFC_results_df.Th_sil_f / RFC_results_df.Nb_sil_f
RFC_results_df["Th_sil_f/La_sil_f"] = RFC_results_df.Th_sil_f / RFC_results_df.La_sil_f
RFC_results_df["Sc_sil_f/Lu_sil_f"] = RFC_results_df.Sc_sil_f / RFC_results_df.Lu_sil_f

RFC_results_df["Th_sil_f_PM"] = Th_sil_f / 0.0795
RFC_results_df["Nb_sil_f_PM"] = Nb_sil_f / 0.658
RFC_results_df["La_sil_f_PM"] = La_sil_f / 0.648
RFC_results_df["Ce_sil_f_PM"] = Ce_sil_f / 1.675
RFC_results_df["Pr_sil_f_PM"] = Pr_sil_f / 0.254
RFC_results_df["Nd_sil_f_PM"] = Nd_sil_f / 1.25
RFC_results_df["Zr_sil_f_PM"] = Zr_sil_f / 10.5
RFC_results_df["Hf_sil_f_PM"] = Hf_sil_f / 0.283
RFC_results_df["Sm_sil_f_PM"] = Sm_sil_f / 0.406
RFC_results_df["Eu_sil_f_PM"] = Eu_sil_f / 0.154
RFC_results_df["Ti_sil_f_PM"] = Ti_sil_f / 1205
RFC_results_df["Gd_sil_f_PM"] = Gd_sil_f / 0.544
RFC_results_df["Tb_sil_f_PM"] = Tb_sil_f / 0.099
RFC_results_df["Dy_sil_f_PM"] = Dy_sil_f / 0.674
RFC_results_df["Y_sil_f_PM"] = Y_sil_f / 4.3
RFC_results_df["Ho_sil_f_PM"] = Ho_sil_f / 0.149
RFC_results_df["Er_sil_f_PM"] = Er_sil_f / 0.438
RFC_results_df["Tm_sil_f_PM"] = Tm_sil_f / 0.068
RFC_results_df["Yb_sil_f_PM"] = Yb_sil_f / 0.441
RFC_results_df["Lu_sil_f_PM"] = Lu_sil_f / 0.0675
RFC_results_df["V_sil_f_PM"] = V_sil_f / 82
RFC_results_df["Sc_sil_f_PM"] = Sc_sil_f / 16.2
RFC_results_df["La_sil_f_PM/Sm_sil_f_PM"] = RFC_results_df.La_sil_f_PM / RFC_results_df.Sm_sil_f_PM
RFC_results_df["La_sil_f_PM/Lu_sil_f_PM"] = RFC_results_df.La_sil_f_PM / RFC_results_df.Lu_sil_f_PM
RFC_results_df["Gd_sil_f_PM/Yb_sil_f_PM"] = RFC_results_df.Gd_sil_f_PM / RFC_results_df.Yb_sil_f_PM
RFC_results_df["Th_sil_f_PM/Nb_sil_f_PM"] = RFC_results_df.Th_sil_f_PM / RFC_results_df.Nb_sil_f_PM
RFC_results_df["Th_sil_f_PM/La_sil_f_PM"] = RFC_results_df.Th_sil_f_PM / RFC_results_df.La_sil_f_PM
RFC_results_df["Sc_sil_f_PM/Lu_sil_f_PM"] = RFC_results_df.Sc_sil_f_PM / RFC_results_df.Lu_sil_f_PM

RFC_results_df["Th_sol"] = Th_sol
RFC_results_df["Nb_sol"] = Nb_sol
RFC_results_df["La_sol"] = La_sol
RFC_results_df["Ce_sol"] = Ce_sol
RFC_results_df["Pr_sol"] = Pr_sol
RFC_results_df["Nd_sol"] = Nd_sol
RFC_results_df["Zr_sol"] = Zr_sol
RFC_results_df["Hf_sol"] = Hf_sol
RFC_results_df["Sm_sol"] = Sm_sol
RFC_results_df["Eu_sol"] = Eu_sol
RFC_results_df["Ti_sol"] = Ti_sol
RFC_results_df["Gd_sol"] = Gd_sol
RFC_results_df["Tb_sol"] = Tb_sol
RFC_results_df["Dy_sol"] = Dy_sol
RFC_results_df["Y_sol"] = Y_sol
RFC_results_df["Ho_sol"] = Ho_sol
RFC_results_df["Er_sol"] = Er_sol
RFC_results_df["Tm_sol"] = Tm_sol
RFC_results_df["Yb_sol"] = Yb_sol
RFC_results_df["Lu_sol"] = Lu_sol
RFC_results_df["V_sol"] = V_sol
RFC_results_df["Sc_sol"] = Sc_sol
RFC_results_df["La_sol/Sm_sol"] = RFC_results_df.La_sol / RFC_results_df.Sm_sol
RFC_results_df["La_sol/Lu_sol"] = RFC_results_df.La_sol / RFC_results_df.Lu_sol
RFC_results_df["Gd_sol/Yb_sol"] = RFC_results_df.Gd_sol / RFC_results_df.Yb_sol
RFC_results_df["Th_sol/Nb_sol"] = RFC_results_df.Th_sol / RFC_results_df.Nb_sol
RFC_results_df["Th_sol/La_sol"] = RFC_results_df.Th_sol / RFC_results_df.La_sol
RFC_results_df["Sc_sol/Lu_sol"] = RFC_results_df.Sc_sol / RFC_results_df.Lu_sol

RFC_results_df["Th_sol_PM"] = Th_sol / 0.0795
RFC_results_df["Nb_sol_PM"] = Nb_sol / 0.658
RFC_results_df["La_sol_PM"] = La_sol / 0.648
RFC_results_df["Ce_sol_PM"] = Ce_sol / 1.675
RFC_results_df["Pr_sol_PM"] = Pr_sol / 0.254
RFC_results_df["Nd_sol_PM"] = Nd_sol / 1.25
RFC_results_df["Zr_sol_PM"] = Zr_sol / 10.5
RFC_results_df["Hf_sol_PM"] = Hf_sol / 0.283
RFC_results_df["Sm_sol_PM"] = Sm_sol / 0.406
RFC_results_df["Eu_sol_PM"] = Eu_sol / 0.154
RFC_results_df["Ti_sol_PM"] = Ti_sol / 1205
RFC_results_df["Gd_sol_PM"] = Gd_sol / 0.544
RFC_results_df["Tb_sol_PM"] = Tb_sol / 0.099
RFC_results_df["Dy_sol_PM"] = Dy_sol / 0.674
RFC_results_df["Y_sol_PM"] = Y_sol / 4.3
RFC_results_df["Ho_sol_PM"] = Ho_sol / 0.149
RFC_results_df["Er_sol_PM"] = Er_sol / 0.438
RFC_results_df["Tm_sol_PM"] = Tm_sol / 0.068
RFC_results_df["Yb_sol_PM"] = Yb_sol / 0.441
RFC_results_df["Lu_sol_PM"] = Lu_sol / 0.0675
RFC_results_df["V_sol_PM"] = V_sol / 82
RFC_results_df["Sc_sol_PM"] = Sc_sol / 16.2
RFC_results_df["La_sol_PM/Sm_sol_PM"] = RFC_results_df.La_sol_PM / RFC_results_df.Sm_sol_PM
RFC_results_df["La_sol_PM/Lu_sol_PM"] = RFC_results_df.La_sol_PM / RFC_results_df.Lu_sol_PM
RFC_results_df["Gd_sol_PM/Yb_sol_PM"] = RFC_results_df.Gd_sol_PM / RFC_results_df.Yb_sol_PM
RFC_results_df["Th_sol_PM/Nb_sol_PM"] = RFC_results_df.Th_sol_PM / RFC_results_df.Nb_sol_PM
RFC_results_df["Th_sol_PM/La_sol_PM"] = RFC_results_df.Th_sol_PM / RFC_results_df.La_sol_PM
RFC_results_df["Sc_sol_PM/Lu_sol_PM"] = RFC_results_df.Sc_sol_PM / RFC_results_df.Lu_sol_PM

RFC_results_df["F_sil_remaining"] = np.round(F_sil_remaining, 4)

with st.expander("RFC Model Results"):
    st.dataframe(RFC_results_df)

    @st.cache
    def convert_df(df):
        return df.to_csv().encode("utf-8")
    
    RFC_results_df_download = convert_df(RFC_results_df)

    st.download_button(label = "Download RFC Results", data = RFC_results_df_download, file_name = "RFC_Model_Results.csv", mime = "text/csv")

st.write("")

#####################################################################################################
# RFC Scatter Plot
#####################################################################################################

RFC_results_df_subset = RFC_results_df[RFC_results_df.F_sil_remaining.isin([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])]

st.subheader("RFC Graphs")
st.write("")

with st.expander("Scatter Plot"):

    element_list = {
    "Th_sil_f_PM":"Th (PM) (Residual)",
    "Nb_sil_f_PM":"Nb (PM) (Residual)",
    "La_sil_f_PM":"La (PM) (Residual)",
    "Ce_sil_f_PM":"Ce (PM) (Residual)",
    "Pr_sil_f_PM":"Pr (PM) (Residual)",
    "Nd_sil_f_PM":"Nd (PM) (Residual)",
    "Zr_sil_f_PM":"Zr (PM) (Residual)",
    "Hf_sil_f_PM":"Hf (PM) (Residual)",
    "Sm_sil_f_PM":"Sm (PM) (Residual)",
    "Eu_sil_f_PM":"Eu (PM) (Residual)",
    "Ti_sil_f_PM":"Ti (PM) (Residual)",
    "Gd_sil_f_PM":"Gd (PM) (Residual)",
    "Tb_sil_f_PM":"Tb (PM) (Residual)",
    "Dy_sil_f_PM":"Dy (PM) (Residual)",
    "Y_sil_f_PM":"Y (PM) (Residual)",
    "Ho_sil_f_PM":"Ho (PM) (Residual)",
    "Er_sil_f_PM":"Er (PM) (Residual)",
    "Tm_sil_f_PM":"Tm (PM) (Residual)",
    "Yb_sil_f_PM":"Yb (PM) (Residual)",
    "Lu_sil_f_PM":"Lu (PM) (Residual)",
    "V_sil_f_PM":"V (PM) (Residual)",
    "Sc_sil_f_PM":"Sc (PM) (Residual)",
    "La_sil_f_PM/Sm_sil_f_PM":"La/Sm (PM) (Residual)",
    "La_sil_f_PM/Lu_sil_f_PM":"La/Lu (PM) (Residual)",
    "Gd_sil_f_PM/Yb_sil_f_PM":"Gd/Yb (PM) (Residual)",
    "Th_sil_f_PM/Nb_sil_f_PM":"Th/Nb (PM) (Residual)",
    "Th_sil_f_PM/La_sil_f_PM":"Th/La (PM) (Residual)",
    "Sc_sil_f_PM/Lu_sil_f_PM":"Sc/Lu (PM) (Residual)",

    "Th_sol_PM":"Th (PM) (Cumulate)",
    "Nb_sol_PM":"Nb (PM) (Cumulate)",
    "La_sol_PM":"La (PM) (Cumulate)",
    "Ce_sol_PM":"Ce (PM) (Cumulate)",
    "Pr_sol_PM":"Pr (PM) (Cumulate)",
    "Nd_sol_PM":"Nd (PM) (Cumulate)",
    "Zr_sol_PM":"Zr (PM) (Cumulate)",
    "Hf_sol_PM":"Hf (PM) (Cumulate)",
    "Sm_sol_PM":"Sm (PM) (Cumulate)",
    "Eu_sol_PM":"Eu (PM) (Cumulate)",
    "Ti_sol_PM":"Ti (PM) (Cumulate)",
    "Gd_sol_PM":"Gd (PM) (Cumulate)",
    "Tb_sol_PM":"Tb (PM) (Cumulate)",
    "Dy_sol_PM":"Dy (PM) (Cumulate)",
    "Y_sol_PM":"Y (PM) (Cumulate)",
    "Ho_sol_PM":"Ho (PM) (Cumulate)",
    "Er_sol_PM":"Er (PM) (Cumulate)",
    "Tm_sol_PM":"Tm (PM) (Cumulate)",
    "Yb_sol_PM":"Yb (PM) (Cumulate)",
    "Lu_sol_PM":"Lu (PM) (Cumulate)",
    "V_sol_PM":"V (PM) (Cumulate)",
    "Sc_sol_PM":"Sc (PM) (Cumulate)",
    "La_sol_PM/Sm_sol_PM":"La/Sm (PM) (Cumulate)",
    "La_sol_PM/Lu_sol_PM":"La/Lu (PM) (Cumulate)",
    "Gd_sol_PM/Yb_sol_PM":"Gd/Yb (PM) (Cumulate)",
    "Th_sol_PM/Nb_sol_PM":"Th/Nb (PM) (Cumulate)",
    "Th_sol_PM/La_sol_PM":"Th/La (PM) (Cumulate)",
    "Sc_sol_PM/Lu_sol_PM":"Sc/Lu (PM) (Cumulate)"
    }

    a1, a2 = st.columns([1,1])

    with a1:
        X_Element_RM = st.selectbox("X-axis (Residual)", ("Th_sil_f_PM", "Nb_sil_f_PM", "La_sil_f_PM", "Ce_sil_f_PM", "Pr_sil_f_PM", "Nd_sil_f_PM", "Zr_sil_f_PM", "Hf_sil_f_PM" , "Sm_sil_f_PM", "Eu_sil_f_PM", "Ti_sil_f_PM" , "Gd_sil_f_PM", "Tb_sil_f_PM", "Dy_sil_f_PM", "Y_sil_f_PM" , "Ho_sil_f_PM", "Er_sil_f_PM", "Tm_sil_f_PM", "Yb_sil_f_PM", "Lu_sil_f_PM", "V_sil_f_PM", "Sc_sil_f_PM" , "La_sil_f_PM/Sm_sil_f_PM", "La_sil_f_PM/Lu_sil_f_PM", "Gd_sil_f_PM/Yb_sil_f_PM", "Th_sil_f_PM/Nb_sil_f_PM", "Th_sil_f_PM/La_sil_f_PM", "Sc_sil_f_PM/Lu_sil_f_PM"),
        format_func = element_list.get)
        X_Element_CM = st.selectbox("X-axis (Cumulate)", ("Th_sol_PM", "Nb_sol_PM", "La_sol_PM", "Ce_sol_PM", "Pr_sol_PM", "Nd_sol_PM", "Zr_sol_PM", "Hf_sol_PM" , "Sm_sol_PM", "Eu_sol_PM", "Ti_sol_PM" , "Gd_sol_PM", "Tb_sol_PM", "Dy_sol_PM", "Y_sol_PM" , "Ho_sol_PM", "Er_sol_PM", "Tm_sol_PM", "Yb_sol_PM", "Lu_sol_PM", "V_sol_PM", "Sc_sol_PM" , "La_sol_PM/Sm_sol_PM", "La_sol_PM/Lu_sol_PM", "Gd_sol_PM/Yb_sol_PM", "Th_sol_PM/Nb_sol_PM", "Th_sol_PM/La_sol_PM", "Sc_sol_PM/Lu_sol_PM"),
        format_func = element_list.get)
        x_min = st.number_input("X min", min_value = 0.0, max_value = 1000000.0, value = 0.1, key = 1, step = 10.0)
        x_max = st.number_input("X max", min_value = 0.0, max_value = 1000000.0, value = 20.0, key = 1, step = 10.0)
        x_scale = st.selectbox("X Scale", ("linear", "log"), key = 1)
    with a2:
        Y_Element_RM = st.selectbox("Y-axis (Residual)", ("Th_sil_f_PM", "Nb_sil_f_PM", "La_sil_f_PM", "Ce_sil_f_PM", "Pr_sil_f_PM", "Nd_sil_f_PM", "Zr_sil_f_PM", "Hf_sil_f_PM" , "Sm_sil_f_PM", "Eu_sil_f_PM", "Ti_sil_f_PM" , "Gd_sil_f_PM", "Tb_sil_f_PM", "Dy_sil_f_PM", "Y_sil_f_PM" , "Ho_sil_f_PM", "Er_sil_f_PM", "Tm_sil_f_PM", "Yb_sil_f_PM", "Lu_sil_f_PM", "V_sil_f_PM", "Sc_sil_f_PM" , "La_sil_f_PM/Sm_sil_f_PM", "La_sil_f_PM/Lu_sil_f_PM", "Gd_sil_f_PM/Yb_sil_f_PM", "Th_sil_f_PM/Nb_sil_f_PM", "Th_sil_f_PM/La_sil_f_PM", "Sc_sil_f_PM/Lu_sil_f_PM"),
        format_func = element_list.get)
        Y_Element_CM = st.selectbox("Y-axis (Cumulate)", ("Th_sol_PM", "Nb_sol_PM", "La_sol_PM", "Ce_sol_PM", "Pr_sol_PM", "Nd_sol_PM", "Zr_sol_PM", "Hf_sol_PM" , "Sm_sol_PM", "Eu_sol_PM", "Ti_sol_PM" , "Gd_sol_PM", "Tb_sol_PM", "Dy_sol_PM", "Y_sol_PM" , "Ho_sol_PM", "Er_sol_PM", "Tm_sol_PM", "Yb_sol_PM", "Lu_sol_PM", "V_sol_PM", "Sc_sol_PM" , "La_sol_PM/Sm_sol_PM", "La_sol_PM/Lu_sol_PM", "Gd_sol_PM/Yb_sol_PM", "Th_sol_PM/Nb_sol_PM", "Th_sol_PM/La_sol_PM", "Sc_sol_PM/Lu_sol_PM"),
        format_func = element_list.get)
        y_min = st.number_input("Y min", min_value = 0.0, max_value = 1000000.0, value = 0.1, key = 1, step = 10.0)
        y_max = st.number_input("Y max", min_value = 0.0, max_value = 1000000.0, value = 20.0, key = 1, step = 10.0)
        y_scale = st.selectbox("Y Scale", ("linear", "log"), key = 1)

    st.write("")

    fig_RFC_scatter, ax = plt.subplots(1,1, figsize = (5,4))
    ax = sns.scatterplot(data = RFC_results_df_subset, x = X_Element_RM, y = Y_Element_RM, hue = "F_sil_remaining", edgecolor = "k", legend = "full")
    ax = sns.scatterplot(data = RFC_results_df_subset, x = X_Element_CM, y = Y_Element_CM, hue = "F_sil_remaining", edgecolor = "k", legend = None, marker = "s")
    ax = plt.xlabel(X_Element_RM)
    ax = plt.ylabel(Y_Element_RM)
    ax = plt.xlim(x_min, x_max)
    ax = plt.ylim(y_min, y_max)
    ax = plt.xscale(x_scale)
    ax = plt.yscale(y_scale)
    ax = plt.axhline(y = 1, color = "grey", linewidth = 0.5, linestyle = "--")
    ax = plt.axvline(x = 1, color = "grey", linewidth = 0.5, linestyle = "--")
    ax = plt.legend(bbox_to_anchor = (1, 0.87), frameon = False, title = "% Sil. Remaining")
    st.write(fig_RFC_scatter)


#####################################################################################################
# RFC REE Diagram
#####################################################################################################

with st.expander("REE Diagram"):

    b1, b2 = st.columns([1, 1])
    with b1:
        y_min = st.number_input("Y min", min_value = 0.0, max_value = 1000000.0, step = 100.0, value = 0.1, key = 2)
    with b2:
        y_max = st.number_input("Y max", min_value = 0.0, max_value = 1000000.0, step = 100.0, value = 10000.0, key = 2)

    st.write("")

    x_ticks = ["La_sil_f_PM", "Ce_sil_f_PM", "Pr_sil_f_PM", "Nd_sil_f_PM", "Sm_sil_f_PM", "Eu_sil_f_PM", "Gd_sil_f_PM", "Tb_sil_f_PM", "Dy_sil_f_PM", "Ho_sil_f_PM", "Er_sil_f_PM", "Tm_sil_f_PM", "Yb_sil_f_PM", "Lu_sil_f_PM"]
    x_tick_labels = ["La", "Ce", "Pr", "Nd", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]

    RFC_results_df_melt = pd.melt(
        RFC_results_df_subset,
        id_vars = ["F_sil_remaining"],
        value_vars = ["La_sil_f_PM", "Ce_sil_f_PM", "Pr_sil_f_PM", "Nd_sil_f_PM", "Sm_sil_f_PM", "Eu_sil_f_PM", "Gd_sil_f_PM", "Tb_sil_f_PM", "Dy_sil_f_PM", "Ho_sil_f_PM", "Er_sil_f_PM", "Tm_sil_f_PM", "Yb_sil_f_PM", "Lu_sil_f_PM"],
        var_name = "element", value_name = "norm_conc")

    fig_RFC_REE, ax2 = plt.subplots(1, 1, figsize = (9, 5))
    ax2 = sns.lineplot(
        data = RFC_results_df_melt,
        x = "element",
        y = "norm_conc",
        estimator = None, units = "F_sil_remaining", color = "r", linewidth = 1, legend = None)
    ax2 = plt.yscale("log")
    ax2 = plt.xlabel("")
    ax2 = plt.ylabel("Residual Melt/Primitive Mantle")
    ax2 = plt.ylim(y_min, y_max)
    ax2 = plt.xticks(ticks = x_ticks, labels = x_tick_labels)
    ax2 = plt.axhline(y = 1, color = "grey", linewidth = 1, linestyle = "--")
    st.write(fig_RFC_REE)

#####################################################################################################
# RFC Spider Plot
#####################################################################################################

with st.expander("Spider Diagram"):

    c1, c2 = st.columns([1, 1])
    with c1:
        y_min = st.number_input("Y min", min_value = 0.0, max_value = 1000000.0, step = 100.0, value = 0.1, key = 3)
    with c2:
        y_max = st.number_input("Y max", min_value = 0.0, max_value = 1000000.0, step = 100.0, value = 10000.0, key = 3)

    st.write("")

    x_ticks = ["Th_sil_f_PM", "Nb_sil_f_PM", "La_sil_f_PM", "Ce_sil_f_PM", "Pr_sil_f_PM", "Nd_sil_f_PM", "Zr_sil_f_PM", "Hf_sil_f_PM", "Sm_sil_f_PM", "Eu_sil_f_PM", "Ti_sil_f_PM", "Gd_sil_f_PM", "Tb_sil_f_PM", "Dy_sil_f_PM", "Y_sil_f_PM", "Ho_sil_f_PM", "Er_sil_f_PM", "Tm_sil_f_PM", "Yb_sil_f_PM", "Lu_sil_f_PM", "V_sil_f_PM", "Sc_sil_f_PM"]
    x_tick_labels = ["Th", "Nb", "La", "Ce", "Pr", "Nd", "Zr", "Hf" , "Sm", "Eu", "Ti", "Gd", "Tb", "Dy", "Y", "Ho", "Er", "Tm", "Yb", "Lu", "V", "Sc"]

    RFC_results_df_melt = pd.melt(
        RFC_results_df_subset,
        id_vars = ["F_sil_remaining"],
        value_vars = ["Th_sil_f_PM", "Nb_sil_f_PM", "La_sil_f_PM", "Ce_sil_f_PM", "Pr_sil_f_PM", "Nd_sil_f_PM", "Zr_sil_f_PM", "Hf_sil_f_PM", "Sm_sil_f_PM", "Eu_sil_f_PM", "Ti_sil_f_PM", "Gd_sil_f_PM", "Tb_sil_f_PM", "Dy_sil_f_PM", "Y_sil_f_PM", "Ho_sil_f_PM", "Er_sil_f_PM", "Tm_sil_f_PM", "Yb_sil_f_PM", "Lu_sil_f_PM", "V_sil_f_PM", "Sc_sil_f_PM"],
        var_name = "element", value_name = "norm_conc")

    fig_RFC_spider, ax3 = plt.subplots(1, 1, figsize = (9, 5))
    ax3 = sns.lineplot(
        data = RFC_results_df_melt,
        x = "element",
        y = "norm_conc",
        estimator = None, units = "F_sil_remaining", color = "r", palette = "autumn", linewidth = 1, legend = None)
    ax3 = plt.yscale("log")
    ax3 = plt.xlabel("")
    ax3 = plt.ylabel("Residual Melt/Primitive Mantle")
    ax3 = plt.ylim(y_min, y_max)
    ax3 = plt.xticks(ticks = x_ticks, labels = x_tick_labels)
    ax3 = plt.axhline(y = 1, color = "grey", linewidth = 1, linestyle = "--")
    st.write(fig_RFC_spider)

st.write("")

st.caption("**Note - No amphibole-melt Kd values for Th, Nb, Zr, Y, Sc, and Hf. No garnet-melt Kd values for Th, Ti, and V. No ilmenite-melt Kd values for Ti.***")

# st.markdown("***No amphibole-melt Kd values for Th, Nb, Zr, Y, Sc, and Hf.***")
# st.write("***No garnet-melt Kd values for Th, Ti, and V.***")
# st.write("***No ilmenite-melt Kd values for Ti.***")

st.write("-----------------------")
st.write("")

#####################################################################################################
# SIMPLE CONTAMINATION MODEL
#####################################################################################################

st.header("Simple Contamination")
st.write("")

#####################################################################################################
# Composition of contaminant
#####################################################################################################

with st.expander("Composition of contaminant"):

    d1, d2, d3, d4 = st.columns([1, 1, 1, 1])

    with d1:
        Th_contam = st.number_input("Th (ppm)", min_value = 0.0, value = float(), key = 4)
        Nb_contam = st.number_input("Nb (ppm)", min_value = 0.0, value = float(), key = 4)
        La_contam = st.number_input("La (ppm)", min_value = 0.0, value = float(), key = 4)
        Ce_contam = st.number_input("Ce (ppm)", min_value = 0.0, value = float(), key = 4)
        Pr_contam = st.number_input("Pr (ppm)", min_value = 0.0, value = float(), key = 4)
        Nd_contam = st.number_input("Nd (ppm)", min_value = 0.0, value = float(), key = 4)
    with d2:
        Zr_contam = st.number_input("Zr (ppm)", min_value = 0.0, value = float(), key = 4)
        Hf_contam = st.number_input("Hf (ppm)", min_value = 0.0, value = float(), key = 4)
        Sm_contam = st.number_input("Sm (ppm)", min_value = 0.0, value = float(), key = 4)
        Eu_contam = st.number_input("Eu (ppm)", min_value = 0.0, value = float(), key = 4)
        Ti_contam = st.number_input("Ti (ppm)", min_value = 0.0, value = float(), key = 4)
        Gd_contam = st.number_input("Gd (ppm)", min_value = 0.0, value = float(), key = 4)
    with d3:
        Tb_contam = st.number_input("Tb (ppm)", min_value = 0.0, value = float(), key = 4)
        Dy_contam = st.number_input("Dy (ppm)", min_value = 0.0, value = float(), key = 4)
        Y_contam = st.number_input("Y (ppm)", min_value = 0.0, value = float(), key = 4)
        Ho_contam = st.number_input("Ho (ppm)", min_value = 0.0, value = float(), key = 4)
        Er_contam = st.number_input("Er (ppm)", min_value = 0.0, value = float(), key = 4)
        Tm_contam = st.number_input("Tm (ppm)", min_value = 0.0, value = float(), key = 4)
    with d4:
        Yb_contam = st.number_input("Yb (ppm)", min_value = 0.0, value = float(), key = 4)
        Lu_contam = st.number_input("Lu (ppm)", min_value = 0.0, value = float(), key = 4)
        V_contam = st.number_input("V (ppm)", min_value = 0.0, value = float(), key = 4)
        Sc_contam = st.number_input("Sc (ppm)", min_value = 0.0, value = float(), key = 4)

contaminant = {
"Elements":["Th", "Nb", "La", "Ce", "Pr", "Nd", "Zr", "Hf", "Sm", "Eu", "Ti", "Gd", "Tb", "Dy", "Y", "Ho", "Er", "Tm", "Yb", "Lu", "V", "Sc"],
"Concentration (ppm)":[Th_contam, Nb_contam, La_contam, Ce_contam, Pr_contam, Nd_contam, Zr_contam, Hf_contam, Sm_contam, Eu_contam, Ti_contam, Gd_contam, Tb_contam, Dy_contam, Y_contam, Ho_contam, Er_contam, Tm_contam, Yb_contam, Lu_contam, V_contam, Sc_contam]
}

contaminant_df = pd.DataFrame(data = contaminant)

#####################################################################################################
# Mixing calculation
#####################################################################################################

F_contam = np.arange(0.1, 1.0+0.001, 0.001)

Th_melt_contam = (Th_contam * F_contam) + (Th_sil_i * (1 - F_contam))
Nb_melt_contam = (Nb_contam * F_contam) + (Nb_sil_i * (1 - F_contam))
La_melt_contam = (La_contam * F_contam) + (La_sil_i * (1 - F_contam))
Ce_melt_contam = (Ce_contam * F_contam) + (Ce_sil_i * (1 - F_contam))
Pr_melt_contam = (Pr_contam * F_contam) + (Pr_sil_i * (1 - F_contam))
Nd_melt_contam = (Nd_contam * F_contam) + (Nd_sil_i * (1 - F_contam))
Zr_melt_contam = (Zr_contam * F_contam) + (Zr_sil_i * (1 - F_contam))
Hf_melt_contam = (Hf_contam * F_contam) + (Hf_sil_i * (1 - F_contam))
Sm_melt_contam = (Sm_contam * F_contam) + (Sm_sil_i * (1 - F_contam))
Eu_melt_contam = (Eu_contam * F_contam) + (Eu_sil_i * (1 - F_contam))
Ti_melt_contam = (Ti_contam * F_contam) + (Ti_sil_i * (1 - F_contam))
Gd_melt_contam = (Gd_contam * F_contam) + (Gd_sil_i * (1 - F_contam))
Tb_melt_contam = (Tb_contam * F_contam) + (Tb_sil_i * (1 - F_contam))
Dy_melt_contam = (Dy_contam * F_contam) + (Dy_sil_i * (1 - F_contam))
Y_melt_contam = (Y_contam * F_contam) + (Y_sil_i * (1 - F_contam))
Ho_melt_contam = (Ho_contam * F_contam) + (Ho_sil_i * (1 - F_contam))
Er_melt_contam = (Er_contam * F_contam) + (Er_sil_i * (1 - F_contam))
Tm_melt_contam = (Tm_contam * F_contam) + (Tm_sil_i * (1 - F_contam))
Yb_melt_contam = (Yb_contam * F_contam) + (Yb_sil_i * (1 - F_contam))
Lu_melt_contam = (Lu_contam * F_contam) + (Lu_sil_i * (1 - F_contam))
V_melt_contam = (V_contam * F_contam) + (V_sil_i * (1 - F_contam))
Sc_melt_contam = (Sc_contam * F_contam) + (Sc_sil_i * (1 - F_contam))

#####################################################################################################
# Combine contamination model results
#####################################################################################################

contamination_results_df = pd.DataFrame()
contamination_results_df["F_contam"] = F_contam
contamination_results_df["Th_melt_contam"] = Th_melt_contam
contamination_results_df["Nb_melt_contam"] = Nb_melt_contam
contamination_results_df["La_melt_contam"] = La_melt_contam
contamination_results_df["Ce_melt_contam"] = Ce_melt_contam
contamination_results_df["Pr_melt_contam"] = Pr_melt_contam
contamination_results_df["Nd_melt_contam"] = Nd_melt_contam
contamination_results_df["Zr_melt_contam"] = Zr_melt_contam
contamination_results_df["Hf_melt_contam"] = Hf_melt_contam
contamination_results_df["Sm_melt_contam"] = Sm_melt_contam
contamination_results_df["Eu_melt_contam"] = Eu_melt_contam
contamination_results_df["Ti_melt_contam"] = Ti_melt_contam
contamination_results_df["Gd_melt_contam"] = Gd_melt_contam
contamination_results_df["Tb_melt_contam"] = Tb_melt_contam
contamination_results_df["Dy_melt_contam"] = Dy_melt_contam
contamination_results_df["Y_melt_contam"] = Y_melt_contam
contamination_results_df["Ho_melt_contam"] = Ho_melt_contam
contamination_results_df["Er_melt_contam"] = Er_melt_contam
contamination_results_df["Tm_melt_contam"] = Tm_melt_contam
contamination_results_df["Yb_melt_contam"] = Yb_melt_contam
contamination_results_df["Lu_melt_contam"] = Lu_melt_contam
contamination_results_df["V_melt_contam"] = V_melt_contam
contamination_results_df["Sc_melt_contam"] = Sc_melt_contam
contamination_results_df["La_melt_contam/Sm_melt_contam"] = contamination_results_df.La_melt_contam / contamination_results_df.Sm_melt_contam
contamination_results_df["La_melt_contam/Lu_melt_contam"] = contamination_results_df.La_melt_contam / contamination_results_df.Lu_melt_contam
contamination_results_df["Gd_melt_contam/Yb_melt_contam"] = contamination_results_df.Gd_melt_contam / contamination_results_df.Yb_melt_contam
contamination_results_df["Th_melt_contam/Nb_melt_contam"] = contamination_results_df.Th_melt_contam / contamination_results_df.Nb_melt_contam
contamination_results_df["Th_melt_contam/La_melt_contam"] = contamination_results_df.Th_melt_contam / contamination_results_df.La_melt_contam
contamination_results_df["Sc_melt_contam/Lu_melt_contam"] = contamination_results_df.Sc_melt_contam / contamination_results_df.Lu_melt_contam

contamination_results_df["Th_melt_contam_PM"] = Th_melt_contam / 0.0795
contamination_results_df["Nb_melt_contam_PM"] = Nb_melt_contam / 0.658
contamination_results_df["La_melt_contam_PM"] = La_melt_contam / 0.648
contamination_results_df["Ce_melt_contam_PM"] = Ce_melt_contam / 1.675
contamination_results_df["Pr_melt_contam_PM"] = Pr_melt_contam / 0.254
contamination_results_df["Nd_melt_contam_PM"] = Nd_melt_contam / 1.25
contamination_results_df["Zr_melt_contam_PM"] = Zr_melt_contam / 10.5
contamination_results_df["Hf_melt_contam_PM"] = Hf_melt_contam / 0.283
contamination_results_df["Sm_melt_contam_PM"] = Sm_melt_contam / 0.406
contamination_results_df["Eu_melt_contam_PM"] = Eu_melt_contam / 0.154
contamination_results_df["Ti_melt_contam_PM"] = Ti_melt_contam / 1205
contamination_results_df["Gd_melt_contam_PM"] = Gd_melt_contam / 0.544
contamination_results_df["Tb_melt_contam_PM"] = Tb_melt_contam / 0.099
contamination_results_df["Dy_melt_contam_PM"] = Dy_melt_contam / 0.674
contamination_results_df["Y_melt_contam_PM"] = Y_melt_contam / 4.3
contamination_results_df["Ho_melt_contam_PM"] = Ho_melt_contam / 0.149
contamination_results_df["Er_melt_contam_PM"] = Er_melt_contam / 0.438
contamination_results_df["Tm_melt_contam_PM"] = Tm_melt_contam / 0.068
contamination_results_df["Yb_melt_contam_PM"] = Yb_melt_contam / 0.441
contamination_results_df["Lu_melt_contam_PM"] = Lu_melt_contam / 0.0675
contamination_results_df["V_melt_contam_PM"] = V_melt_contam / 82
contamination_results_df["Sc_melt_contam_PM"] = Sc_melt_contam / 16.2
contamination_results_df["La_melt_contam_PM/Sm_melt_contam_PM"] = contamination_results_df.La_melt_contam_PM / contamination_results_df.Sm_melt_contam_PM
contamination_results_df["La_melt_contam_PM/Lu_melt_contam_PM"] = contamination_results_df.La_melt_contam_PM / contamination_results_df.Lu_melt_contam_PM
contamination_results_df["Gd_melt_contam_PM/Yb_melt_contam_PM"] = contamination_results_df.Gd_melt_contam_PM / contamination_results_df.Yb_melt_contam_PM
contamination_results_df["Th_melt_contam_PM/Nb_melt_contam_PM"] = contamination_results_df.Th_melt_contam_PM / contamination_results_df.Nb_melt_contam_PM
contamination_results_df["Th_melt_contam_PM/La_melt_contam_PM"] = contamination_results_df.Th_melt_contam_PM / contamination_results_df.La_melt_contam_PM
contamination_results_df["Sc_melt_contam_PM/Lu_melt_contam_PM"] = contamination_results_df.Sc_melt_contam_PM / contamination_results_df.Lu_melt_contam_PM

contamination_results_df["F_contam"] = np.round(F_contam, 4)

with st.expander("Contamination Model Results"):
    st.dataframe(contamination_results_df)

st.write("")

#####################################################################################################
# Contamination scatter plot
#####################################################################################################


contamination_results_df_subset = contamination_results_df[contamination_results_df.F_contam.isin([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])]

st.subheader("Contamination Graphs")
st.write("")

with st.expander("Scatter Plot"):

    contam_element_list = {
    "Th_melt_contam":"Th",
    "Nb_melt_contam":"Nb",
    "La_melt_contam":"La",
    "Ce_melt_contam":"Ce",
    "Pr_melt_contam":"Pr",
    "Nd_melt_contam":"Nd",
    "Zr_melt_contam":"Zr",
    "Hf_melt_contam":"Hf",
    "Sm_melt_contam":"Sm",
    "Eu_melt_contam":"Eu",
    "Ti_melt_contam":"Ti",
    "Gd_melt_contam":"Gd",
    "Tb_melt_contam":"Tb",
    "Dy_melt_contam":"Dy",
    "Y_melt_contam":"Y",
    "Ho_melt_contam":"Ho",
    "Er_melt_contam":"Er",
    "Tm_melt_contam":"Tm",
    "Yb_melt_contam":"Yb",
    "Lu_melt_contam":"Lu",
    "V_melt_contam":"V",
    "Sc_melt_contam":"Sc",
    "La_melt_contam/Sm_melt_contam":"La/Sm",
    "La_melt_contam/Lu_melt_contam":"La/Lu",
    "Gd_melt_contam/Yb_melt_contam":"Gd/Yb",
    "Th_melt_contam/Nb_melt_contam":"Th/Nb",
    "Th_melt_contam/La_melt_contam":"Th/La",
    "Sc_melt_contam/Lu_melt_contam":"Sc/Lu"
    }

    e1, e2 = st.columns([1,1])

    with e1:
        X_Element_contam = st.selectbox("X-axis", ("Th_melt_contam", "Nb_melt_contam", "La_melt_contam", "Ce_melt_contam", "Pr_melt_contam", "Nd_melt_contam", "Zr_melt_contam", "Hf_melt_contam" , "Sm_melt_contam", "Eu_melt_contam", "Ti_melt_contam" , "Gd_melt_contam", "Tb_melt_contam", "Dy_melt_contam", "Y_melt_contam" , "Ho_melt_contam", "Er_melt_contam", "Tm_melt_contam", "Yb_melt_contam", "Lu_melt_contam", "V_melt_contam", "Sc_melt_contam" , "La_melt_contam/Sm_melt_contam", "La_melt_contam/Lu_melt_contam", "Gd_melt_contam/Yb_melt_contam", "Th_melt_contam/Nb_melt_contam", "Th_melt_contam/La_melt_contam", "Sc_melt_contam/Lu_melt_contam"),
        format_func = contam_element_list.get)
        x_min = st.number_input("X min", min_value = 0.0, max_value = 1000000.0, value = 0.1, key = 5, step = 10.0)
        x_max = st.number_input("X max", min_value = 0.0, max_value = 1000000.0, value = 20.0, key = 5, step = 10.0)
        x_scale = st.selectbox("X Scale", ("linear", "log"), key = 5)
    with e2:
        Y_Element_contam = st.selectbox("Y-axis", ("Th_melt_contam", "Nb_melt_contam", "La_melt_contam", "Ce_melt_contam", "Pr_melt_contam", "Nd_melt_contam", "Zr_melt_contam", "Hf_melt_contam" , "Sm_melt_contam", "Eu_melt_contam", "Ti_melt_contam" , "Gd_melt_contam", "Tb_melt_contam", "Dy_melt_contam", "Y_melt_contam" , "Ho_melt_contam", "Er_melt_contam", "Tm_melt_contam", "Yb_melt_contam", "Lu_melt_contam", "V_melt_contam", "Sc_melt_contam" , "La_melt_contam/Sm_melt_contam", "La_melt_contam/Lu_melt_contam", "Gd_melt_contam/Yb_melt_contam", "Th_melt_contam/Nb_melt_contam", "Th_melt_contam/La_melt_contam", "Sc_melt_contam/Lu_melt_contam"),
        format_func = contam_element_list.get)
        y_min = st.number_input("Y min", min_value = 0.0, max_value = 1000000.0, value = 0.1, key = 5, step = 10.0)
        y_max = st.number_input("Y max", min_value = 0.0, max_value = 1000000.0, value = 20.0, key = 5, step = 10.0)
        y_scale = st.selectbox("Y Scale", ("linear", "log"), key = 5)      

    st.write("")

    fig_contam_scatter, ax = plt.subplots(1,1, figsize = (5,4))
    ax = sns.scatterplot(data = contamination_results_df_subset, x = X_Element_contam, y = Y_Element_contam, hue = "F_contam", edgecolor = "k", legend = "full")
    ax = plt.xlabel(X_Element_contam)
    ax = plt.ylabel(Y_Element_contam)
    ax = plt.xlim(x_min, x_max)
    ax = plt.ylim(y_min, y_max)
    ax = plt.xscale(x_scale)
    ax = plt.yscale(y_scale)
    ax = plt.legend(bbox_to_anchor = (1.25, 0.87), frameon = False, title = "% Contam")
    st.write(fig_contam_scatter)

#####################################################################################################
# Contamination REE Diagram
#####################################################################################################

with st.expander("Contamination REE Diagram"):

    f1, f2 = st.columns([1, 1])

    with f1:
        y_min = st.number_input("Y min", min_value = 0.0, max_value = 1000000.0, step = 100.0, value = 0.1, key = 6)
    with f2:
        y_max = st.number_input("Y max", min_value = 0.0, max_value = 1000000.0, step = 100.0, value = 10000.0, key = 6)

    st.write("")

    x_ticks = ["La_melt_contam_PM", "Ce_melt_contam_PM", "Pr_melt_contam_PM", "Nd_melt_contam_PM", "Sm_melt_contam_PM", "Eu_melt_contam_PM", "Gd_melt_contam_PM", "Tb_melt_contam_PM", "Dy_melt_contam_PM", "Ho_melt_contam_PM", "Er_melt_contam_PM", "Tm_melt_contam_PM", "Yb_melt_contam_PM", "Lu_melt_contam_PM"]
    x_tick_labels = ["La", "Ce", "Pr", "Nd", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]

    contamination_results_df_melt = pd.melt(
        contamination_results_df_subset,
        id_vars = ["F_contam"],
        value_vars = ["La_melt_contam_PM", "Ce_melt_contam_PM", "Pr_melt_contam_PM", "Nd_melt_contam_PM", "Sm_melt_contam_PM", "Eu_melt_contam_PM", "Gd_melt_contam_PM", "Tb_melt_contam_PM", "Dy_melt_contam_PM", "Ho_melt_contam_PM", "Er_melt_contam_PM", "Tm_melt_contam_PM", "Yb_melt_contam_PM", "Lu_melt_contam_PM"],
        var_name = "element", value_name = "norm_conc")

    fig_contam_REE, ax2 = plt.subplots(1, 1, figsize = (9, 5))
    ax2 = sns.lineplot(
        data = contamination_results_df_melt,
        x = "element",
        y = "norm_conc",
        estimator = None, units = "F_contam", color = "r", linewidth = 1, legend = None)
    ax2 = plt.yscale("log")
    ax2 = plt.xlabel("")
    ax2 = plt.ylabel("Residual Melt/Primitive Mantle")
    ax2 = plt.ylim(y_min, y_max)
    ax2 = plt.xticks(ticks = x_ticks, labels = x_tick_labels)
    ax2 = plt.axhline(y = 1, color = "grey", linewidth = 1, linestyle = "--")
    st.write(fig_contam_REE)

#####################################################################################################
# Contamination Spider Plot
#####################################################################################################

with st.expander("Spider Diagram"):

    g1, g2 = st.columns([1, 1])
    with g1:
        y_min = st.number_input("Y min", min_value = 0.0, max_value = 1000000.0, step = 100.0, value = 0.1, key = 7)
    with g2:
        y_max = st.number_input("Y max", min_value = 0.0, max_value = 1000000.0, step = 100.0, value = 10000.0, key = 7)

    st.write("")

    x_ticks = ["Th_melt_contam_PM", "Nb_melt_contam_PM", "La_melt_contam_PM", "Ce_melt_contam_PM", "Pr_melt_contam_PM", "Nd_melt_contam_PM", "Zr_melt_contam_PM", "Hf_melt_contam_PM", "Sm_melt_contam_PM", "Eu_melt_contam_PM", "Ti_melt_contam_PM", "Gd_melt_contam_PM", "Tb_melt_contam_PM", "Dy_melt_contam_PM", "Y_melt_contam_PM", "Ho_melt_contam_PM", "Er_melt_contam_PM", "Tm_melt_contam_PM", "Yb_melt_contam_PM", "Lu_melt_contam_PM", "V_melt_contam_PM", "Sc_melt_contam_PM"]
    x_tick_labels = ["Th", "Nb", "La", "Ce", "Pr", "Nd", "Zr", "Hf" , "Sm", "Eu", "Ti", "Gd", "Tb", "Dy", "Y", "Ho", "Er", "Tm", "Yb", "Lu", "V", "Sc"]

    contamination_results_df_melt = pd.melt(
        contamination_results_df_subset,
        id_vars = ["F_contam"],
        value_vars = ["Th_melt_contam_PM", "Nb_melt_contam_PM", "La_melt_contam_PM", "Ce_melt_contam_PM", "Pr_melt_contam_PM", "Nd_melt_contam_PM", "Zr_melt_contam_PM", "Hf_melt_contam_PM", "Sm_melt_contam_PM", "Eu_melt_contam_PM", "Ti_melt_contam_PM", "Gd_melt_contam_PM", "Tb_melt_contam_PM", "Dy_melt_contam_PM", "Y_melt_contam_PM", "Ho_melt_contam_PM", "Er_melt_contam_PM", "Tm_melt_contam_PM", "Yb_melt_contam_PM", "Lu_melt_contam_PM", "V_melt_contam_PM", "Sc_melt_contam_PM"],
        var_name = "element", value_name = "norm_conc")

    fig_contam_spider, ax3 = plt.subplots(1, 1, figsize = (9, 5))
    ax3 = sns.lineplot(
        data = contamination_results_df_melt,
        x = "element",
        y = "norm_conc",
        estimator = None, units = "F_contam", color = "r", palette = "autumn", linewidth = 1, legend = None)
    ax3 = plt.yscale("log")
    ax3 = plt.xlabel("")
    ax3 = plt.ylabel("Residual Melt/Primitive Mantle")
    ax3 = plt.ylim(y_min, y_max)
    ax3 = plt.xticks(ticks = x_ticks, labels = x_tick_labels)
    ax3 = plt.axhline(y = 1, color = "grey", linewidth = 1, linestyle = "--")
    st.write(fig_contam_spider)