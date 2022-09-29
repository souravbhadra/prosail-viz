import streamlit as st
import numpy as np
from prosail import run_prosail
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="PROSAIL-Viz", layout="wide")

st.title("PROSAIL-Viz")
st.write(
    """
    A visualization tool for PROSAIL simulation from given input parameters.
    """
)
    

row1_1, row1_2, row1_3 = st.columns((1, 1, 1))

with st.sidebar:
    n = st.slider(
        "Leaf Structure Index, N",
        min_value=1.0,
        max_value=2.6,
        #value=1.5,
        step=0.001
    )
    cab = st.slider(
        "Chlorophyll a+b Content, cab (ug/cm2)",
        min_value=1.0,
        max_value=80.0,
        #value=np.random.uniform(0.001, 80.0),
        step=0.01
    )
    car = st.slider(
        "Total Carotenoid Content, car (ug/cm2)",
        min_value=1.0,
        max_value=24.0,
        #value=np.random.uniform(1.0, 24.0),
        step=0.01
    )
    ant = st.slider(
        "Total Anthocyanin Content, ant (ug/cm2)",
        min_value=0.001,
        max_value=0.5,
        #value=np.random.uniform(0.001, 0.5),
        step=0.001
    )
    cbrown = st.slider(
        "Brown Pigments, cbrown",
        min_value=0.01,
        max_value=1.0,
        #value=np.random.uniform(0.0, 1.0),
        step=0.01
    )
    cw = st.slider(
        "Equivalent Water Thickness, cw (cm)",
        min_value=0.01,
        max_value=0.08,
        #value=np.random.uniform(0.01, 0.03),
        step=0.001
    )
    cm = st.slider(
        "Leaf Mass per Area, cm (g/cm2)",
        min_value=0.001,
        max_value=0.02,
        #value=np.random.uniform(0.004, 0.0075),
        step=0.001
    )
    hspot = st.slider(
        "Hotspot Parameter, hot",
        min_value=0.01,
        max_value=0.2,
        #value=np.random.uniform(0.01, 0.2),
        step=0.001
    )
    lai = st.slider(
        "Leaf Area Index, lai (m2/m2)",
        min_value=0.5,
        max_value=10.0,
        #value=np.random.uniform(0.0, 7.0),
        step=0.01
    )
    lidfa = st.slider(
        "Average Leaf Inclination Angle, lidfa (degree)",
        min_value=0.1,
        max_value=90.0,
        #value=np.random.uniform(0.1, 90.0),
        step=0.1
    )
    tts = st.slider(
        "Solar Zenith Angle, tts (degrees)",
        min_value=0.0,
        max_value=90.0,
        #value=np.random.uniform(0.0, 90.0),
        step=0.1
    )
    tto = st.slider(
        "Viewing Zenith Angle, tto (degrees)",
        min_value=0.0,
        max_value=90.0,
        #value=np.random.uniform(0.0, 90.0),
        step=0.1
    )
    psi = st.slider(
        "Relative Solar-Sensor Azimuth Angle, psi (degrees)",
        min_value=0.0,
        max_value=360.0,
        #value=np.random.uniform(0.0, 360.0),
        step=1.0
    )


# Read soil spectra
soil = np.load('soil.npy')
spectra = run_prosail(
    n, 
    cab,
    car,
    cbrown,
    cw,
    cm,
    lai,
    lidfa,
    hspot,
    tts,
    tto,
    psi,
    ant,
    prospect_version="D",
    typelidf=2,
    rsoil0=0.1,
    soil_spectrum1=soil,
    factor="SDR"
)
fig = px.line(
    x=np.arange(400, 2501),
    y=spectra,
    template="simple_white"
)
fig.update_traces(line_color='#25523B', line_width=2)

# Edit the layout
fig.update_layout(title='PROSAIL-Simulated Spectra',
                   xaxis_title='Wavelength (nm)',
                   yaxis_title='Reflectance')


st.plotly_chart(fig, use_container_width=True)


    
row2_1, row2_2 = st.columns((2, 1))

with row2_1:
    st.write(
        """
        #### Disclaimer
        This application is only for educational purposes. Use of this application in commercial cases is strictly prohibited.  
        **Map Author:**  *Sourav Bhadra* [souravbhadra.github.io](https://souravbhadra.github.io) | [GitHub](https://github.com/souravbhadra) | [LinkedIn](https://www.linkedin.com/in/bhadrasourav/) | [Twitter](https://twitter.com/sbhadra19)
        **Acknowldgements:** José Gómez-Dans (Creator of [PROSAIL Python Bindings](https://github.com/jgomezdans/prosail))
        """
    )
    
with row2_2:
    st.image('assets/rsl-logo.png')