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

# # Stop execution if no file is uploaded
# if not uploaded_file:
#     st.warning('⚠ Please upload an Excel file to proceed.')
#     st.stop()

# # Load and clean data
# df_alert = pd.read_excel(uploaded_file)
# df_alert = clean(df_alert)
# df_alert['Date'] = pd.to_datetime(df_alert['Date'], format='%d-%m-%Y', errors='coerce')

# # Select Graph Type
# graph_type = st.sidebar.selectbox("�� Select Graph Type", ["Bar Chart", "Line Plot"])

# def format_graph(fig):
#     """Function to update the graph's layout and increase text size."""
#     fig.update_layout(
#         xaxis_title_font_size=20,
#         yaxis_title_font_size=20,
#         xaxis_tickfont_size=16,  # Increase X-axis number size
#         yaxis_tickfont_size=16,  # Increase Y-axis number size
#         title_font_size=22  # Increase Title Font Size
#     )
#     fig.update_traces(textfont_size=18)  # Increase Number Size Inside Graph
#     return fig

# # --- Analysis 1: Most Occurring Signals ---
# if analysis_type == "Analyze Most Occurring Signals in Region":
#     df_alert_filtered = df_alert[df_alert['Signal'].str.contains(":", na=False)]
#     signal_counts = df_alert_filtered.groupby(['Region', 'Signal']).size().reset_index(name='Count')

#     regions = df_alert_filtered['Region'].unique()
#     selected_region = st.selectbox("🌍 Select a Region", regions)

#     if selected_region:
#         region_data = signal_counts[signal_counts['Region'] == selected_region].sort_values(by='Count', ascending=False)
#         st.write(f"### 📈 Most Occurring Signals in {selected_region}")

#         if graph_type == "Bar Chart":
#             fig = px.bar(region_data, x='Signal', y='Count', text='Count',
#                          title=f'Most Occurring Signals in {selected_region}',
#                          labels={'Signal': 'Signal', 'Count': 'Occurrences'},
#                          color='Count', color_continuous_scale='Blues', height=900, width=1600)
#         else:
#             fig = px.line(region_data, x='Signal', y='Count', text='Count',
#                           title=f'Most Occurring Signals in {selected_region}',
#                           labels={'Signal': 'Signal', 'Count': 'Occurrences'},
#                           markers=True, height=900, width=1600)

#         fig = format_graph(fig)  # Apply font size formatting
#         fig.update_layout(xaxis_tickangle=-65)
#         st.plotly_chart(fig, use_container_width=True)

# # --- Analysis 2: Number of Alerts per Region ---
# elif analysis_type == "Analyze Number of Alerts in Region":
#     df_alert['Time'] = df_alert['Time'].astype(str).str.strip()
#     df_alert = df_alert.dropna(subset=['Date', 'Time'])
#     df_alert['Timestamp'] = pd.to_datetime(df_alert['Date'].dt.date.astype(str) + ' ' + df_alert['Time'], errors='coerce')
#     df_alert = df_alert.dropna(subset=['Timestamp'])

#     region_alert_count = df_alert[['Timestamp', 'Region']].drop_duplicates().groupby('Region').size().reset_index(name='Alert Count')

#     st.write("### 🚨 Number of Alerts per Region")

#     if graph_type == "Bar Chart":
#         fig = px.bar(region_alert_count, x='Region', y='Alert Count', text='Alert Count',
#                      title="Number of Alerts per Region",
#                      labels={'Region': 'Region', 'Alert Count': 'Number of Alerts'},
#                      color='Alert Count', color_continuous_scale='Reds', height=900, width=1600)
#     else:
#         fig = px.line(region_alert_count, x='Region', y='Alert Count', text='Alert Count',
#                       title="Number of Alerts per Region",
#                       labels={'Region': 'Region', 'Alert Count': 'Number of Alerts'},
#                       markers=True, height=900, width=1600)

#     fig = format_graph(fig)  # Apply font size formatting
#     fig.update_layout(xaxis_tickangle=-65)
#     st.plotly_chart(fig, use_container_width=True)

# # --- Analysis 3: Total Alerts with Date Wise ---
# elif analysis_type == "Total Alerts with Date Wise":
#     df_alert['Time'] = df_alert['Time'].astype(str).str.strip()
#     df_alert = df_alert.dropna(subset=['Date', 'Time'])
    
#     # Ensure Date column is properly formatted
#     df_alert['DateTime'] = pd.to_datetime(df_alert['Date'].dt.date.astype(str) + ' ' + df_alert['Time'], errors='coerce')
#     df_alert = df_alert.dropna(subset=['DateTime'])

#     df_alert = df_alert.sort_values(by=['Date', 'Time'])

#     # Count alerts per date
#     df_grouped = df_alert.groupby(['Date', 'Time']).size()
#     alert_counts = df_grouped.groupby('Date').size().reset_index(name='Alert Count')

#     st.write("### 📅 Total Alerts Per Date")

#     if graph_type == "Bar Chart":
#         fig = px.bar(alert_counts, x='Date', y='Alert Count', text='Alert Count',
#                      title='Total Alerts with Date Wise',
#                      labels={'Date': 'Date', 'Alert Count': 'Number of Alerts'},
#                      color='Alert Count', color_continuous_scale='Purples', height=900, width=1600)
#     else:
#         fig = px.line(alert_counts, x='Date', y='Alert Count', text='Alert Count',
#                       title='Total Alerts with Date Wise',
#                       labels={'Date': 'Date', 'Alert Count': 'Number of Alerts'},
#                       markers=True, height=900, width=1600)

#     # Fix x-axis date formatting and rotation
#     fig.update_layout(
#         xaxis=dict(
#             tickformat="%d-%m-%Y",  # Ensures date format is correct
#             tickangle=-45  # Rotates date labels to prevent overlap
#         )
#     )

#     fig = format_graph(fig)  # Apply font size formatting
#     st.plotly_chart(fig, use_container_width=True)






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

# # Stop execution if no file is uploaded
# if not uploaded_file:
#     st.warning('⚠ Please upload an Excel file to proceed.')
#     st.stop()

# # Load and clean data
# df_alert = pd.read_excel(uploaded_file)
# df_alert = clean(df_alert)
# df_alert.columns = df_alert.columns.str.strip()  # Strip whitespace from column names
# df_alert['Date'] = pd.to_datetime(df_alert['Date'], format='%d-%m-%Y', errors='coerce')
# df_alert = df_alert.dropna(subset=['Date'])  # Ensure 'Date' is not NaT

# # Sidebar Date Range Filter
# st.sidebar.subheader("🗓️ Select Date Range")
# min_date = df_alert['Date'].min()
# max_date = df_alert['Date'].max()

# start_date, end_date = st.sidebar.date_input(
#     "Filter by Date Range",
#     value=(min_date, max_date),
#     min_value=min_date,
#     max_value=max_date
# )

# # Filter data based on selected date range
# df_alert = df_alert[(df_alert['Date'] >= pd.to_datetime(start_date)) & (df_alert['Date'] <= pd.to_datetime(end_date))]

# # Select Graph Type
# graph_type = st.sidebar.selectbox("📊 Select Graph Type", ["Bar Chart", "Line Plot"])

# def format_graph(fig):
#     """Function to update the graph's layout and increase text size."""
#     fig.update_layout(
#         xaxis_title_font_size=20,
#         yaxis_title_font_size=20,
#         xaxis_tickfont_size=16,
#         yaxis_tickfont_size=16,
#         title_font_size=22
#     )
#     fig.update_traces(textfont_size=18)
#     return fig

# # --- Analysis 1: Most Occurring Signals ---
# if analysis_type == "Analyze Most Occurring Signals in Region":
#     df_alert_filtered = df_alert[df_alert['Signal'].str.contains(":", na=False)]
#     signal_counts = df_alert_filtered.groupby(['Region', 'Signal']).size().reset_index(name='Count')

#     regions = df_alert_filtered['Region'].unique()
#     selected_region = st.selectbox("🌍 Select a Region", regions)

#     if selected_region:
#         region_data = signal_counts[signal_counts['Region'] == selected_region].sort_values(by='Count', ascending=False)
#         st.write(f"### 📈 Most Occurring Signals in {selected_region}")

#         if graph_type == "Bar Chart":
#             fig = px.bar(region_data, x='Signal', y='Count', text='Count',
#                          title=f'Most Occurring Signals in {selected_region}',
#                          labels={'Signal': 'Signal', 'Count': 'Occurrences'},
#                          color='Count', color_continuous_scale='Blues', height=900, width=1600)
#         else:
#             fig = px.line(region_data, x='Signal', y='Count', text='Count',
#                           title=f'Most Occurring Signals in {selected_region}',
#                           labels={'Signal': 'Signal', 'Count': 'Occurrences'},
#                           markers=True, height=900, width=1600)

#         fig = format_graph(fig)
#         fig.update_layout(xaxis_tickangle=-65)
#         st.plotly_chart(fig, use_container_width=True)

# # --- Analysis 2: Number of Alerts per Region ---
# elif analysis_type == "Analyze Number of Alerts in Region":
#     df_alert['Time'] = df_alert['Time'].astype(str).str.strip()
#     df_alert = df_alert.dropna(subset=['Date', 'Time'])
#     df_alert['Timestamp'] = pd.to_datetime(df_alert['Date'].dt.date.astype(str) + ' ' + df_alert['Time'], errors='coerce')
#     df_alert = df_alert.dropna(subset=['Timestamp'])

#     region_alert_count = df_alert[['Timestamp', 'Region']].drop_duplicates().groupby('Region').size().reset_index(name='Alert Count')

#     st.write("### 🚨 Number of Alerts per Region")

#     if graph_type == "Bar Chart":
#         fig = px.bar(region_alert_count, x='Region', y='Alert Count', text='Alert Count',
#                      title="Number of Alerts per Region",
#                      labels={'Region': 'Region', 'Alert Count': 'Number of Alerts'},
#                      color='Alert Count', color_continuous_scale='Reds', height=900, width=1600)
#     else:
#         fig = px.line(region_alert_count, x='Region', y='Alert Count', text='Alert Count',
#                       title="Number of Alerts per Region",
#                       labels={'Region': 'Region', 'Alert Count': 'Number of Alerts'},
#                       markers=True, height=900, width=1600)

#     fig = format_graph(fig)
#     fig.update_layout(xaxis_tickangle=-65)
#     st.plotly_chart(fig, use_container_width=True)

# # --- Analysis 3: Total Alerts with Date Wise ---
# elif analysis_type == "Total Alerts with Date Wise":
#     df_alert['Time'] = df_alert['Time'].astype(str).str.strip()
#     df_alert = df_alert.dropna(subset=['Date', 'Time'])

#     df_alert['DateTime'] = pd.to_datetime(
#         df_alert['Date'].dt.strftime('%Y-%m-%d') + ' ' + df_alert['Time'],
#         errors='coerce'
#     )

#     df_alert = df_alert.dropna(subset=['DateTime'])
#     df_alert = df_alert.sort_values(by=['Date', 'Time'])

#     df_grouped = df_alert.groupby(['Date', 'Time']).size()
#     alert_counts = df_grouped.groupby('Date').size().reset_index(name='Alert Count')

#     st.write("### 📅 Total Alerts Per Date")

#     if graph_type == "Bar Chart":
#         fig = px.bar(
#             alert_counts,
#             x='Date',
#             y='Alert Count',
#             text='Alert Count',
#             title='Total Alerts with Date Wise',
#             labels={'Date': 'Date', 'Alert Count': 'Number of Alerts'},
#             color='Alert Count',
#             color_continuous_scale='Purples',
#             height=900,
#             width=1600
#         )
#     else:
#         fig = px.line(
#             alert_counts,
#             x='Date',
#             y='Alert Count',
#             text='Alert Count',
#             title='Total Alerts with Date Wise',
#             labels={'Date': 'Date', 'Alert Count': 'Number of Alerts'},
#             markers=True,
#             height=900,
#             width=1600
#         )

#     fig.update_layout(
#         xaxis=dict(
#             tickformat="%d-%m-%Y",
#             tickangle=-45,
#             tickmode='linear',
#             dtick="D1"
#         )
#     )

#     if len(alert_counts) <= 31:
#         fig.update_layout(
#             xaxis=dict(
#                 tickmode='array',
#                 tickvals=alert_counts['Date'],
#                 ticktext=alert_counts['Date'].dt.strftime('%d-%m-%Y')
#             )
#         )

#     fig = format_graph(fig)
#     st.plotly_chart(fig, use_container_width=True)






import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(page_title="Alert Data Dashboard", layout="wide")

# Function to clean the data
def clean(df):
    df = df.dropna(how='all')
    header_row = ['Date', 'Time', 'Region', 'Signal', 'Loss Score', 'Discord Score']
    df_clean = df[~df['Date'].isin(header_row)]
    return df_clean

# --- UI ---
st.title("📊 Alert Data Analysis Dashboard")

# File Upload
uploaded_file = st.sidebar.file_uploader("📂 Upload an Excel file", type=["xlsx"])

# Sidebar navigation
st.sidebar.header("🔍 Select Analysis Type")
analysis_type = st.sidebar.radio("Choose an analysis:", [
    "Analyze Most Occurring Signals in Region",
    "Analyze Number of Alerts in Region",
    "Total Alerts with Date Wise",
    "Alerts per Hour for Selected Date",
     "Alerts per Hour by Region"
])

if not uploaded_file:
    st.warning('⚠ Please upload an Excel file to proceed.')
    st.stop()

# --- Load Data ---
df_alert = pd.read_excel(uploaded_file)
df_alert = clean(df_alert)
df_alert.columns = df_alert.columns.str.strip()
df_alert['Date'] = pd.to_datetime(df_alert['Date'], format='%d-%m-%Y', errors='coerce')
df_alert['Time'] = df_alert['Time'].astype(str).str.strip()
df_alert = df_alert.dropna(subset=['Date', 'Time'])

# Combine date and time
df_alert['DateTime'] = pd.to_datetime(df_alert['Date'].dt.strftime('%Y-%m-%d') + ' ' + df_alert['Time'], errors='coerce')
df_alert = df_alert.dropna(subset=['DateTime'])

# --- Sidebar Filters ---
st.sidebar.subheader("🗓️ Select Date Range")
min_date = df_alert['Date'].min()
max_date = df_alert['Date'].max()

start_date, end_date = st.sidebar.date_input(
    "Date Range", value=(min_date, max_date), min_value=min_date, max_value=max_date
)

st.sidebar.subheader("⏰ Select Hour Range")
hour_start, hour_end = st.sidebar.slider(
    "Hour Range (24h)", 0, 23, (0, 23)
)

# --- Apply Filters ---
df_alert = df_alert[
    (df_alert['Date'] >= pd.to_datetime(start_date)) &
    (df_alert['Date'] <= pd.to_datetime(end_date)) &
    (df_alert['DateTime'].dt.hour >= hour_start) &
    (df_alert['DateTime'].dt.hour <= hour_end)
]

# --- Graph Style ---
graph_type = st.sidebar.selectbox("📊 Select Graph Type", ["Bar Chart", "Line Plot"])

def format_graph(fig):
    fig.update_layout(
        xaxis_title_font_size=20,
        yaxis_title_font_size=20,
        xaxis_tickfont_size=16,
        yaxis_tickfont_size=16,
        title_font_size=22
    )
    fig.update_traces(textfont_size=18)
    return fig

# --- Analysis 1: Most Occurring Signals in Region ---
if analysis_type == "Analyze Most Occurring Signals in Region":
    df_filtered = df_alert[df_alert['Signal'].str.contains(":", na=False)]
    signal_counts = df_filtered.groupby(['Region', 'Signal']).size().reset_index(name='Count')

    regions = df_filtered['Region'].unique()
    selected_region = st.selectbox("🌍 Select a Region", regions)

    if selected_region:
        region_data = signal_counts[signal_counts['Region'] == selected_region].sort_values(by='Count', ascending=False)
        st.write(f"### 📈 Most Occurring Signals in {selected_region} ({hour_start}:00 to {hour_end}:00)")

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

        fig = format_graph(fig)
        fig.update_layout(xaxis_tickangle=-65)
        st.plotly_chart(fig, use_container_width=True)

# --- Analysis 2: Number of Alerts per Region ---
elif analysis_type == "Analyze Number of Alerts in Region":
    region_alert_count = df_alert[['DateTime', 'Region']].drop_duplicates().groupby('Region').size().reset_index(name='Alert Count')

    st.write(f"### 🚨 Number of Alerts per Region ({hour_start}:00 to {hour_end}:00)")

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

    fig = format_graph(fig)
    fig.update_layout(xaxis_tickangle=-65)
    st.plotly_chart(fig, use_container_width=True)

# --- Analysis 3: Total Alerts with Date Wise ---
elif analysis_type == "Total Alerts with Date Wise":
    df_grouped = df_alert.groupby(['Date', 'Time']).size()
    alert_counts = df_grouped.groupby('Date').size().reset_index(name='Alert Count')

    st.write(f"### 📅 Total Alerts Per Date ({hour_start}:00 to {hour_end}:00)")

    if graph_type == "Bar Chart":
        fig = px.bar(
            alert_counts,
            x='Date',
            y='Alert Count',
            text='Alert Count',
            title='Total Alerts with Date Wise',
            labels={'Date': 'Date', 'Alert Count': 'Number of Alerts'},
            color='Alert Count',
            color_continuous_scale='Purples',
            height=900,
            width=1600
        )
    else:
        fig = px.line(
            alert_counts,
            x='Date',
            y='Alert Count',
            text='Alert Count',
            title='Total Alerts with Date Wise',
            labels={'Date': 'Date', 'Alert Count': 'Number of Alerts'},
            markers=True,
            height=900,
            width=1600
        )

    fig.update_layout(
        xaxis=dict(
            tickformat="%d-%m-%Y",
            tickangle=-45,
            tickmode='linear',
            dtick="D1"
        )
    )

    if len(alert_counts) <= 31:
        fig.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=alert_counts['Date'],
                ticktext=alert_counts['Date'].dt.strftime('%d-%m-%Y')
            )
        )

    fig = format_graph(fig)
    st.plotly_chart(fig, use_container_width=True)

# --- Analysis 4: Alerts per Hour for Selected Date ---
elif analysis_type == "Alerts per Hour for Selected Date":
    available_dates = df_alert['Date'].dropna().dt.date.unique()
    selected_date = st.selectbox("📆 Select a date", sorted(available_dates))

    df_selected = df_alert[df_alert['Date'].dt.date == selected_date]

    df_selected['Hour'] = df_selected['DateTime'].dt.hour
    hourly_alerts = df_selected.groupby('Hour').size().reset_index(name='Alert Count')

    st.write(f"### ⏱️ Hourly Alert Distribution for {selected_date.strftime('%d-%m-%Y')}")

    fig = px.bar(hourly_alerts, x='Hour', y='Alert Count', text='Alert Count',
                 title=f'Alerts per Hour on {selected_date.strftime("%d-%m-%Y")}',
                 labels={'Hour': 'Hour of Day', 'Alert Count': 'Number of Alerts'},
                 color='Alert Count', color_continuous_scale='Tealgrn', height=700, width=1400)

    fig = format_graph(fig)
    st.plotly_chart(fig, use_container_width=True)

    

# elif analysis_type == "Alerts per Hour by Region":
#     # Extract the hour from the DateTime
#     df_alert['Hour'] = df_alert['DateTime'].dt.hour

#     # Count unique alert events (distinct DateTime + Region)
#     unique_alerts = df_alert[['DateTime', 'Region']]
#     unique_alerts = unique_alerts.drop_duplicates()
#     unique_alerts['Hour'] = unique_alerts['DateTime'].dt.hour

#     # Group by Region and Hour
#     region_hour_alert_count = (
#         unique_alerts.groupby(['Region', 'Hour'])
#         .size()
#         .reset_index(name='Alert Count')
#     )

#     st.write(f"### ⏰ Number of Unique Alert Events per Hour by Region ({hour_start}:00 to {hour_end}:00)")

#     if graph_type == "Bar Chart":
#         fig = px.bar(region_hour_alert_count, x='Hour', y='Alert Count', color='Region',
#                      barmode='group', text='Alert Count',
#                      title="Alerts per Hour by Region (Distinct Events)",
#                      labels={'Hour': 'Hour of Day', 'Alert Count': 'Number of Alerts'},
#                      height=900, width=1600)
#     else:
#         fig = px.line(region_hour_alert_count, x='Hour', y='Alert Count', color='Region',
#                       markers=True, text='Alert Count',
#                       title="Alerts per Hour by Region (Distinct Events)",
#                       labels={'Hour': 'Hour of Day', 'Alert Count': 'Number of Alerts'},
#                       height=900, width=1600)

#     fig = format_graph(fig)
#     fig.update_layout(xaxis_tickmode='linear', xaxis_tick0=0, xaxis_dtick=1)
#     st.plotly_chart(fig, use_container_width=True)

elif analysis_type == "Alerts per Hour by Region":
    # Extract the hour from the DateTime
    df_alert['Hour'] = df_alert['DateTime'].dt.hour

    # Drop duplicates to count unique alert events
    unique_alerts = df_alert[['DateTime', 'Region']].drop_duplicates()
    unique_alerts['Hour'] = unique_alerts['DateTime'].dt.hour

    # Group by Region and Hour
    region_hour_alert_count = (
        unique_alerts.groupby(['Region', 'Hour'])
        .size()
        .reset_index(name='Alert Count')
    )

    # Create hour range label: "08:00 - 08:59"
    region_hour_alert_count['Hour Label'] = region_hour_alert_count['Hour'].apply(
        lambda h: f"{h:02d}:00 - {h:02d}:59"
    )

    st.write(f"### ⏰ Number of Unique Alert Events per Hour by Region ({hour_start}:00 to {hour_end}:00)")

    if graph_type == "Bar Chart":
        fig = px.bar(region_hour_alert_count, x='Hour Label', y='Alert Count', color='Region',
                     barmode='group', text='Alert Count',
                     title="Alerts per Hour by Region (Distinct Events)",
                     labels={'Hour Label': 'Hour Range', 'Alert Count': 'Number of Alerts'},
                     height=900, width=1600)
    else:
        fig = px.line(region_hour_alert_count, x='Hour Label', y='Alert Count', color='Region',
                      markers=True, text='Alert Count',
                      title="Alerts per Hour by Region (Distinct Events)",
                      labels={'Hour Label': 'Hour Range', 'Alert Count': 'Number of Alerts'},
                      height=900, width=1600)

    fig = format_graph(fig)
    fig.update_layout(xaxis_tickangle=-90)
    st.plotly_chart(fig, use_container_width=True)
