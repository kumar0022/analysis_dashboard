# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Set Streamlit page configuration
# st.set_page_config(page_title="Alert Data Dashboard", layout="wide")

# # Function to clean the data
# def clean(df):
#     df = df.dropna(how='all')  # Drop rows with all NaN values
#     header_row = ['Date', 'Time', 'Region', 'Signal', 'Loss Score', 'Discord Score']
#     df_clean = df[~df['Date'].isin(header_row)]  # Remove rows with unwanted headers
#     return df_clean

# # Streamlit UI
# st.title("📊 Alert Data Analysis Dashboard")

# # File Upload
# uploaded_file = st.sidebar.file_uploader("📂 Upload an Excel file", type=["xlsx"])


# # Sidebar navigation
# st.sidebar.header("🔍 Select Analysis Type")
# analysis_type = st.sidebar.radio("Choose an analysis:", [
#     "Analyze Most Occurring Signals in Region",
#     "Analyze Number of Alerts in Region",
#     "Total Alerts with Date Wise"
# ])

# if not uploaded_file:
#     st.warning('Upload xlsx File')
#     st.stop()


# if uploaded_file:
#     # Load and clean data
#     df_alert = pd.read_excel(uploaded_file)
#     df_alert = clean(df_alert)
#     df_alert['Date'] = pd.to_datetime(df_alert['Date'], format='%d-%m-%Y', errors='coerce')
    
#     # Select Graph Type
#     graph_type = st.sidebar.selectbox("📊 Select Graph Type", ["Bar Chart", "Line Plot"])

#     def format_graph(fig):
#         """Function to update the graph's layout and increase text size."""
#         fig.update_layout(
#             xaxis_title_font_size=20,
#             yaxis_title_font_size=20,
#             xaxis_tickfont_size=16,  # Increase X-axis number size
#             yaxis_tickfont_size=16,  # Increase Y-axis number size
#             title_font_size=22  # Increase Title Font Size
#         )
#         fig.update_traces(textfont_size=18)  # Increase Number Size Inside Graph
#         return fig

#     # --- Analysis 1: Most Occurring Signals ---
#     if analysis_type == "Analyze Most Occurring Signals in Region":
#         df_alert_filtered = df_alert[df_alert['Signal'].str.contains(":", na=False)]
#         signal_counts = df_alert_filtered.groupby(['Region', 'Signal']).size().reset_index(name='Count')
        
#         regions = df_alert_filtered['Region'].unique()
#         selected_region = st.selectbox("🌍 Select a Region", regions)

#         if selected_region:
#             region_data = signal_counts[signal_counts['Region'] == selected_region].sort_values(by='Count', ascending=False)
#             st.write(f"### 📈 Most Occurring Signals in {selected_region}")

#             if graph_type == "Bar Chart":
#                 fig = px.bar(region_data, x='Signal', y='Count', text='Count',
#                              title=f'Most Occurring Signals in {selected_region}',
#                              labels={'Signal': 'Signal', 'Count': 'Occurrences'},
#                              color='Count', color_continuous_scale='Blues', height=900, width=1600)
#             else:
#                 fig = px.line(region_data, x='Signal', y='Count', text='Count',
#                               title=f'Most Occurring Signals in {selected_region}',
#                               labels={'Signal': 'Signal', 'Count': 'Occurrences'},
#                               markers=True, height=900, width=1600)

#             fig = format_graph(fig)  # Apply font size formatting
#             fig.update_layout(xaxis_tickangle=-65)
#             st.plotly_chart(fig, use_container_width=True)

#     # --- Analysis 2: Number of Alerts per Region ---
#     elif analysis_type == "Analyze Number of Alerts in Region":
#         df_alert['Time'] = df_alert['Time'].astype(str).str.strip()
#         df_alert = df_alert.dropna(subset=['Date', 'Time'])
#         df_alert['Timestamp'] = pd.to_datetime(df_alert['Date'].dt.date.astype(str) + ' ' + df_alert['Time'], errors='coerce')
#         df_alert = df_alert.dropna(subset=['Timestamp'])

#         region_alert_count = df_alert[['Timestamp', 'Region']].drop_duplicates().groupby('Region').size().reset_index(name='Alert Count')

#         st.write("### 🚨 Number of Alerts per Region")

#         if graph_type == "Bar Chart":
#             fig = px.bar(region_alert_count, x='Region', y='Alert Count', text='Alert Count',
#                          title="Number of Alerts per Region",
#                          labels={'Region': 'Region', 'Alert Count': 'Number of Alerts'},
#                          color='Alert Count', color_continuous_scale='Reds', height=900, width=1600)
#         else:
#             fig = px.line(region_alert_count, x='Region', y='Alert Count', text='Alert Count',
#                           title="Number of Alerts per Region",
#                           labels={'Region': 'Region', 'Alert Count': 'Number of Alerts'},
#                           markers=True, height=900, width=1600)

#         fig = format_graph(fig)  # Apply font size formatting
#         fig.update_layout(xaxis_tickangle=-65)
#         st.plotly_chart(fig, use_container_width=True)

#     # --- Analysis 3: Total Alerts with Date Wise ---
#     elif analysis_type == "Total Alerts with Date Wise":
#         df_alert['Time'] = df_alert['Time'].astype(str).str.strip()
#         df_alert = df_alert.dropna(subset=['Date', 'Time'])
#         df_alert['DateTime'] = pd.to_datetime(df_alert['Date'].dt.date.astype(str) + ' ' + df_alert['Time'], errors='coerce')
#         df_alert = df_alert.dropna(subset=['DateTime'])

#         df_alert = df_alert.sort_values(by=['Date', 'Time'])
#         df_grouped = df_alert.groupby(['Date', 'Time']).size()
#         alert_counts = df_grouped.groupby('Date').size().reset_index(name='Alert Count')

#         st.write("### 📅 Total Alerts Per Date")

#         if graph_type == "Bar Chart":
#             fig = px.bar(alert_counts, x='Date', y='Alert Count', text='Alert Count',
#                          title='Total Alerts with Date Wise',
#                          labels={'Date': 'Date', 'Alert Count': 'Number of Alerts'},
#                          color='Alert Count', color_continuous_scale='Purples', height=900, width=1600)
#         else:
#             fig = px.line(alert_counts, x='Date', y='Alert Count', text='Alert Count',
#                           title='Total Alerts with Date Wise',
#                           labels={'Date': 'Date', 'Alert Count': 'Number of Alerts'},
#                           markers=True, height=900, width=1600)

#         fig = format_graph(fig)  # Apply font size formatting
#         fig.update_layout(xaxis_tickangle=-65)
#         st.plotly_chart(fig, use_container_width=True)







import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(page_title="Alert Data Dashboard", layout="wide")

# Function to clean the data
def clean(df):
    df = df.dropna(how='all')  # Drop rows with all NaN values
    header_row = ['Date', 'Time', 'Region', 'Signal', 'Loss Score', 'Discord Score']
    df_clean = df[~df['Date'].isin(header_row)]  # Remove rows with unwanted headers
    return df_clean

# Streamlit UI
st.title("📊 Alert Data Analysis Dashboard")

# File Upload
uploaded_file = st.sidebar.file_uploader("📂 Upload an Excel file", type=["xlsx"])

# Sidebar navigation
st.sidebar.header("🔍 Select Analysis Type")
analysis_type = st.sidebar.radio("Choose an analysis:", [
    "Analyze Most Occurring Signals in Region",
    "Analyze Number of Alerts in Region",
    "Total Alerts with Date Wise"
])

# Stop execution if no file is uploaded
if not uploaded_file:
    st.warning('⚠ Please upload an Excel file to proceed.')
    st.stop()

# Load and clean data
df_alert = pd.read_excel(uploaded_file)
df_alert = clean(df_alert)
df_alert['Date'] = pd.to_datetime(df_alert['Date'], format='%d-%m-%Y', errors='coerce')

# Select Graph Type
graph_type = st.sidebar.selectbox("�� Select Graph Type", ["Bar Chart", "Line Plot"])

def format_graph(fig):
    """Function to update the graph's layout and increase text size."""
    fig.update_layout(
        xaxis_title_font_size=20,
        yaxis_title_font_size=20,
        xaxis_tickfont_size=16,  # Increase X-axis number size
        yaxis_tickfont_size=16,  # Increase Y-axis number size
        title_font_size=22  # Increase Title Font Size
    )
    fig.update_traces(textfont_size=18)  # Increase Number Size Inside Graph
    return fig

# --- Analysis 1: Most Occurring Signals ---
if analysis_type == "Analyze Most Occurring Signals in Region":
    df_alert_filtered = df_alert[df_alert['Signal'].str.contains(":", na=False)]
    signal_counts = df_alert_filtered.groupby(['Region', 'Signal']).size().reset_index(name='Count')

    regions = df_alert_filtered['Region'].unique()
    selected_region = st.selectbox("🌍 Select a Region", regions)

    if selected_region:
        region_data = signal_counts[signal_counts['Region'] == selected_region].sort_values(by='Count', ascending=False)
        st.write(f"### 📈 Most Occurring Signals in {selected_region}")

        if graph_type == "Bar Chart":
            fig = px.bar(region_data, x='Signal', y='Count', text='Count',
                         title=f'Most Occurring Signals in {selected_region}',
                         labels={'Signal': 'Signal', 'Count': 'Occurrences'},
                         color='Count', color_continuous_scale='Blues', height=900, width=1600)
        else:
            fig = px.line(region_data, x='Signal', y='Count', text='Count',
                          title=f'Most Occurring Signals in {selected_region}',
                          labels={'Signal': 'Signal', 'Count': 'Occurrences'},
                          markers=True, height=900, width=1600)

        fig = format_graph(fig)  # Apply font size formatting
        fig.update_layout(xaxis_tickangle=-65)
        st.plotly_chart(fig, use_container_width=True)

# --- Analysis 2: Number of Alerts per Region ---
elif analysis_type == "Analyze Number of Alerts in Region":
    df_alert['Time'] = df_alert['Time'].astype(str).str.strip()
    df_alert = df_alert.dropna(subset=['Date', 'Time'])
    df_alert['Timestamp'] = pd.to_datetime(df_alert['Date'].dt.date.astype(str) + ' ' + df_alert['Time'], errors='coerce')
    df_alert = df_alert.dropna(subset=['Timestamp'])

    region_alert_count = df_alert[['Timestamp', 'Region']].drop_duplicates().groupby('Region').size().reset_index(name='Alert Count')

    st.write("### 🚨 Number of Alerts per Region")

    if graph_type == "Bar Chart":
        fig = px.bar(region_alert_count, x='Region', y='Alert Count', text='Alert Count',
                     title="Number of Alerts per Region",
                     labels={'Region': 'Region', 'Alert Count': 'Number of Alerts'},
                     color='Alert Count', color_continuous_scale='Reds', height=900, width=1600)
    else:
        fig = px.line(region_alert_count, x='Region', y='Alert Count', text='Alert Count',
                      title="Number of Alerts per Region",
                      labels={'Region': 'Region', 'Alert Count': 'Number of Alerts'},
                      markers=True, height=900, width=1600)

    fig = format_graph(fig)  # Apply font size formatting
    fig.update_layout(xaxis_tickangle=-65)
    st.plotly_chart(fig, use_container_width=True)

# --- Analysis 3: Total Alerts with Date Wise ---
elif analysis_type == "Total Alerts with Date Wise":
    df_alert['Time'] = df_alert['Time'].astype(str).str.strip()
    df_alert = df_alert.dropna(subset=['Date', 'Time'])
    
    # Ensure Date column is properly formatted
    df_alert['DateTime'] = pd.to_datetime(df_alert['Date'].dt.date.astype(str) + ' ' + df_alert['Time'], errors='coerce')
    df_alert = df_alert.dropna(subset=['DateTime'])

    df_alert = df_alert.sort_values(by=['Date', 'Time'])

    # Count alerts per date
    df_grouped = df_alert.groupby(['Date', 'Time']).size()
    alert_counts = df_grouped.groupby('Date').size().reset_index(name='Alert Count')

    st.write("### 📅 Total Alerts Per Date")

    if graph_type == "Bar Chart":
        fig = px.bar(alert_counts, x='Date', y='Alert Count', text='Alert Count',
                     title='Total Alerts with Date Wise',
                     labels={'Date': 'Date', 'Alert Count': 'Number of Alerts'},
                     color='Alert Count', color_continuous_scale='Purples', height=900, width=1600)
    else:
        fig = px.line(alert_counts, x='Date', y='Alert Count', text='Alert Count',
                      title='Total Alerts with Date Wise',
                      labels={'Date': 'Date', 'Alert Count': 'Number of Alerts'},
                      markers=True, height=900, width=1600)

    # Fix x-axis date formatting and rotation
    fig.update_layout(
        xaxis=dict(
            tickformat="%d-%m-%Y",  # Ensures date format is correct
            tickangle=-45  # Rotates date labels to prevent overlap
        )
    )

    fig = format_graph(fig)  # Apply font size formatting
    st.plotly_chart(fig, use_container_width=True)




