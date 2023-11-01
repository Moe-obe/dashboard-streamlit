import streamlit as st
import plotly.express as px

# Create a function to display the first tab
def tab1():
    st.write("This is Tab 1")
    
    col1, col2 = st.beta_columns(2)
    
    with col1:
        st.plotly_chart(px.scatter(x=[1, 2, 3, 4, 5], y=[2, 4, 1, 6, 3]).update_traces(mode='markers'))
        st.plotly_chart(px.bar(x=["A", "B", "C", "D"], y=[10, 20, 15, 25]))

    with col2:
        st.plotly_chart(px.pie(names=["A", "B", "C", "D"], values=[30, 20, 10, 40]))
        st.plotly_chart(px.line(x=[1, 2, 3, 4, 5], y=[2, 4, 1, 6, 3]))

# Create a function to display the second tab
def tab2():
    st.write("This is Tab 2")
    st.plotly_chart(px.scatter(x=[5, 4, 3, 2, 1], y=[3, 6, 1, 4, 2]).update_traces(mode='markers'))
    st.plotly_chart(px.bar(x=["X", "Y", "Z", "W"], y=[15, 10, 30, 20]))
    st.plotly_chart(px.pie(names=["X", "Y", "Z", "W"], values=[40, 20, 30, 10]))
    st.plotly_chart(px.line(x=[1, 2, 3, 4, 5], y=[3, 2, 1, 4, 5]))

# Create a Streamlit app with tabs
st.title("Streamlit Tabs Example with 4 Plots in Each Tab")
tabs = st.sidebar.selectbox("Select a tab:", ("Tab 1", "Tab 2"))

if tabs == "Tab 1":
    tab1()
elif tabs == "Tab 2":
    tab2()
