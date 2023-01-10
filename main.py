import streamlit as st
import numpy as np
import pandas as pd


# st.set_page_config(
#         page_title="Hello",
#         page_icon="👋",
#     )

def welcome():
    # st.set_page_config(
    #     page_title="Hello",
    #     page_icon="👋",
    # )

    # st.markdown("# Hello")
    st.sidebar.header("Hello")

    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
            forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
            Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


# @st.cache
def some_map(x: int = 10):
    map_data = pd.DataFrame(
        np.random.randn(x, 2) / [50, 50] + [59.95, 30.32],
        columns=['lat', 'lon'])

    st.map(map_data)

# @st.cache
def slider():
    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x * x)
    # print(x)
    return x


if __name__ == "__main__":
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    welcome()
    x = slider()
    some_map(x)

    pass
