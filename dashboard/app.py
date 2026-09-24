import os, requests, streamlit as st
st.set_page_config(page_title='India AI TrafficBrain',page_icon='🚦',layout='wide')
st.title('🚦 India AI TrafficBrain'); st.caption('AI-driven traffic-control research dashboard')
api=os.getenv('TRAFFICBRAIN_API','http://localhost:8000')
a,b,c=st.columns(3); a.metric('Scope','India-wide'); b.metric('Mode','Simulation'); c.metric('Safety','Constrained')
if st.button('Run simulation',type='primary'):
    try:
        r=requests.get(f'{api}/simulate',timeout=20); r.raise_for_status(); st.json(r.json())
    except Exception as e: st.error(f'API unavailable: {e}')
st.divider(); st.subheader('Research pipeline'); st.write('Camera/Tracker → State → Temporal GNN → Multi-Agent RL → Safety Shield → Digital Twin → Evaluation')
