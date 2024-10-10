import streamlit as st
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
   page_title="Lotka Volterra model",
   layout="wide",
)

r"""
# Lotkův-Volterrův model

Lotkův-Volterrův model dravce a kořisti s lovem je soustava diferenciálních rovnic následujícího tvaru.

$$
\frac{\mathrm dx}{\mathrm dt} = ax - bxy - hx\\[10px]
\frac{\mathrm dy}{\mathrm dt} = -cy + dxy - hy
$$
"""

c1,c2 = st.columns(2)

with c1:
    tmax = st.number_input("Konec času", value=20)
    xmax = st.number_input("Maximum populace kořisti", value =10)
    ymax = st.number_input("Maximum populace dravce", value = 10)

    c01,c02 = st.columns(2)
    with c01:
        a = st.slider("a (vitalita kořisti)", 0.0, 5., 2.)
        b = st.slider("b (působení dravce na kořist)", 0.0, 5., 1.)
    with c02:
        c = st.slider("c (úmrtnost dravce bez kořisti)", 0.0, 5., 2.)
        d = st.slider("d (profit dravce z přítomnosti kořisti)", 0.0, 5., .5)
    h = st.slider("h (intenzita lovu konstantním úsilím)", 0.0, 5., 1.)

def prey(x,y):
    return a*x - b*x*y - h*x

def predator(x,y):
    return -c*y+d*x*y - h*y

def model(t,X):
    x,y = X
    return [prey(x,y),predator(x,y)]

meze = [0,tmax]
pocatecni_podminka = [7, 2]

t = np.linspace(*meze, 300)
sol = solve_ivp(
    model, 
    meze, # interval pro reseni
    pocatecni_podminka, # pocatecni podminka
    t_eval=t
)

fig, ax = plt.subplots()
plt.plot(t, sol.y.T)
plt.xlabel('čas')
plt.legend(['kořist', 'dravec'], shadow=True)
plt.title('Lotkův-Volterrův model dravce a kořisti')
ax.set(ylim=(0,np.max([xmax,ymax])))
ax.grid()

with c2:
    st.pyplot(fig)

