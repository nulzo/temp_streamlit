import streamlit as st
from streamlit_extras.app_logo import add_logo
import pandas as pd
import numpy as np
from streamlit_extras.grid import grid

def app():
    st.title('Contextualized Food Audience Data')
    st.subheader("Welcome to the contextualized food audience data webpage. Here, you'll find insights derived from analyzing data stored in a Google Cloud Platform (GCP) bucket. Our platform leverages advanced analytics techniques to provide you with valuable insights into food target audiences, demographics, categories, emerging trends, and more.")
    st.write("Our platform aggregates and analyzes data stored in a GCP bucket to generate actionable insights for stakeholders in the food industry. By harnessing the power of data analytics, we uncover hidden patterns, trends, and correlations within the dataset, enabling you to make informed decisions and drive business growth.")
    st.write("""- **Food Target Audiences**: Discover key demographic segments and target audiences within the food industry.
  
- **Food Categories Analysis**: Gain insights into food product categories and identify emerging trends.
  
- **Demographic Trends**: Explore demographic trends and preferences related to food consumption.
  
- **Emerging Trends Detection**: Stay ahead of the curve by identifying emerging trends and opportunities in the food market.
""")
    st.info('This is a purely informational message', icon="ℹ️")
    
    random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    my_grid = grid(2, [2, 4, 1], 1, 4, vertical_align="bottom")

    # Row 1:
    my_grid.dataframe(random_df, use_container_width=True)
    my_grid.line_chart(random_df, use_container_width=True)
    # Row 2:
    my_grid.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
    my_grid.text_input("Your name")
    my_grid.button("Send", use_container_width=True)
    # Row 3:
    my_grid.text_area("Your message", height=40)
    # Row 4:
    my_grid.button("Example 1", use_container_width=True)
    my_grid.button("Example 2", use_container_width=True)
    my_grid.button("Example 3", use_container_width=True)
    my_grid.button("Example 4", use_container_width=True)
    # Row 5 (uses the spec from row 1):
    with my_grid.expander("Show Filters", expanded=True):
        st.slider("Filter by Age", 0, 100, 50)
        st.slider("Filter by Height", 0.0, 2.0, 1.0)
        st.slider("Filter by Weight", 0.0, 100.0, 50.0)
    my_grid.dataframe(random_df, use_container_width=True)

if __name__ == '__main__':
    app()