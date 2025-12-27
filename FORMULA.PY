import streamlit as st

st.set_page_config(page_title="Arb Dashboard", layout="wide")
st.title("⚽ Arbitrage Trading Dashboard")

bankroll = st.number_input("Bankroll (KSh)", value=15000)

st.subheader("Enter Odds")
col1, col2, col3 = st.columns(3)

with col1:
    o1 = st.number_input("Outcome 1", value=2.05)
with col2:
    ox = st.number_input("Outcome X", value=3.40)
with col3:
    o2 = st.number_input("Outcome 2", value=4.20)

odds = {"1": o1, "X": ox, "2": o2}

inv = arb_percentage(odds)

if inv < 1:
    st.success(f"ARB FOUND: {(1 - inv)*100:.2f}%")
    stakes = calc_stakes(odds, bankroll)
    st.write("Recommended Stakes")
    st.json(stakes)
else:
    st.warning("No arbitrage opportunity")

