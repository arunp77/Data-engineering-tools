import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Load Data
df = pd.read_excel('supermarkt_sales.xlsx', skiprows=3)
df = df.drop(df.columns[0], axis=1)

# Preprocess Data
df_encoded = pd.get_dummies(df, columns=['Branch', 'City', 'Customer_type', 'Gender', 'Product line', 'Payment'], drop_first=True)

X = df_encoded[['Quantity', 'Unit price', 'gross income']]
y = df_encoded['Total']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# ====================== Streamlit app ========================
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
st.title(":bar_chart: _Sales Dashboard_ created by :blue[Arun] :sunglasses:")

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Select Analysis", ('Data Overview', 'Actual vs Predicted', 'Residual Plot', 'Residuals Distribution', 'Model Performance', 'Learning Curve'))

# Filters
city = st.sidebar.multiselect("Select the City:", options=df["City"].unique(), default=df["City"].unique())
customer_type = st.sidebar.multiselect("Select the Customer Type:", options=df["Customer_type"].unique(), default=df["Customer_type"].unique())
gender = st.sidebar.multiselect("Select the Gender:", options=df["Gender"].unique(), default=df["Gender"].unique())
card_type = st.sidebar.multiselect("Select payment method:", options=df['Payment'].unique(), default=df["Payment"].unique())

# Correct the query by using 'Payment' in the filter
df_selection = df.query("City == @city & Customer_type == @customer_type & Gender == @gender & Payment == @card_type")

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()

# ---- MAIN PAGE ----
st.markdown("##")


# 1. Data Overview
if option == 'Data Overview':
    st.header('Data Overview')
    st.write(df_selection.head())
    st.write(df_selection.describe())

    # Gender Distribution Plot
    st.subheader('Gender Distribution')
    gender_dist = px.histogram(df_selection, x="Gender", title="Gender Distribution", width=600, height=400)
    st.plotly_chart(gender_dist)

    # Sales by City
    st.subheader('Sales by City')
    city_sales = df_selection.groupby('City')['Total'].sum().reset_index()
    city_sales_plot = px.bar(city_sales, x='City', y='Total', title="Total Sales by City", width=600, height=400)
    st.plotly_chart(city_sales_plot)
    
    # Sales by Product Line
    st.subheader('Sales by Product Line')
    product_sales = df_selection.groupby('Product line')['Total'].sum().sort_values(ascending=False)
    product_sales_plot = px.bar(x=product_sales.index, y=product_sales.values, title="Understand which product lines generate the most revenue", width=600, height=400)
    st.plotly_chart(product_sales_plot)

    # ---- Customer Type and Payment Method Crosstab ----
    st.subheader('Customer Type and Payment Method')
    # Create a crosstab using pandas
    customer_payment_crosstab = pd.crosstab(df_selection['Customer_type'], df_selection['Payment']) # "Analyze which customer type uses which payment method"
    # Plot the crosstab as a stacked bar chart using Plotly
    fig = go.Figure()
    for payment_method in customer_payment_crosstab.columns:
        fig.add_trace(
            go.Bar(
                x=customer_payment_crosstab.index,
                y=customer_payment_crosstab[payment_method],
                name=payment_method
            )
        )

    # Customize the layout
    fig.update_layout(
        barmode='stack',
        title="Customer Type vs Payment Method",
        xaxis_title="Customer Type",
        yaxis_title="Count",
        legend_title="Payment Method"
    )

    # Display the plot
    st.plotly_chart(fig)
    
    #------------------------------------------------------------
    # Sales Over Time: If you want to analyze sales trends over time
    st.subheader('Sales Over Time: Analyzing sales trends over time')

    # Ensure the 'Date' column is in datetime format
    df_encoded['Date'] = pd.to_datetime(df_encoded['Date'])

    # Group by Date to get daily sales
    daily_sales = df_encoded.groupby('Date')['Total'].sum().reset_index()

    # Plot using plotly
    fig = px.line(daily_sales, x='Date', y='Total', title='Sales Over Time')

    # Display the plot
    st.plotly_chart(fig)
    
    # Correlation Heatmap
    st.subheader('Correlation Heatmap')

    # Calculate the correlation matrix
    correlation = df[['Unit price', 'Quantity', 'Total', 'gross income', 'Rating']].corr()

    # Plot heatmap using Plotly
    fig = px.imshow(correlation, 
                    text_auto=True, 
                    color_continuous_scale='RdBu_r', 
                    title='Correlation Heatmap')

    st.plotly_chart(fig)
    
    # Customer Segmentation
    st.subheader('Customer Segmentation by Spending')

    #----------------------------------
    # Function to categorize customers based on total spending
    def categorize_customer(total):
        if total < 200:
            return 'Low Spender'
        elif 200 <= total < 500:
            return 'Medium Spender'
        else:
            return 'High Spender'
        
    # Apply customer category
    df['Customer Category'] = df['Total'].apply(categorize_customer)

    #----------------------------------
    # Customer Segmentation
    st.subheader('Customer Segmentation by Spending')

    # Function to categorize customers based on total spending
    def categorize_customer(total):
        if total < 200:
            return 'Low Spender'
        elif 200 <= total < 500:
            return 'Medium Spender'
        else:
            return 'High Spender'

    # Apply customer category
    df['Customer Category'] = df['Total'].apply(categorize_customer)

    # Count the occurrences of each customer category
    customer_segments = df['Customer Category'].value_counts().reset_index()

    # Rename columns to make them more descriptive
    customer_segments.columns = ['Customer Category', 'count']

    # Plot customer segments using Plotly
    fig = px.bar(customer_segments, x='Customer Category', y='count', 
                title='Customer Segments by Spending', 
                labels={'count': 'Number of Customers'})
    st.plotly_chart(fig)

    
    #----------------------------------
    # Sales by Time of Day
    st.subheader('Sales by Time of Day')
    # Group sales by time
    time_sales = df.groupby('Time')['Total'].sum().reset_index()
    # Plot using Plotly
    fig = px.line(time_sales, x='Time', y='Total', title='Sales by Hour of the Day', labels={'Total': 'Total Sales'})
    st.plotly_chart(fig)
    
    #----------------------------------
    # Gross Income by Branch
    st.subheader('Gross Income by Branch')
    # Group by branch
    branch_income = df.groupby('Branch')['gross income'].sum().reset_index()
    # Plot using Plotly
    fig = px.bar(branch_income, x='Branch', y='gross income', title='Gross Income by Branch', labels={'gross income': 'Gross Income'})
    st.plotly_chart(fig)
    
    #----------------------------------
    # Rating Distribution
    st.subheader('Distribution of Customer Ratings')
    # Plot histogram using Plotly
    fig = px.histogram(df, x='Rating', nbins=20, title='Distribution of Customer Ratings', marginal='box', 
                    labels={'Rating': 'Rating'}, color_discrete_sequence=['blue'])
    st.plotly_chart(fig)
    
    #----------------------------------
    # Rating based on Product Line
    st.subheader('Customer Ratings by Product Line')
    # Boxplot using Plotly
    fig = px.box(df, x='Product line', y='Rating', title='Customer Ratings by Product Line', labels={'Rating': 'Rating'})
    fig.update_xaxes(tickangle=45)
    st.plotly_chart(fig)





    

# 2. Actual vs Predicted Plot
if option == 'Actual vs Predicted':
    st.header('Actual vs Predicted Sales')
    scatter_plot = px.scatter(x=y_test, y=y_pred, labels={'x': 'Actual Sales', 'y': 'Predicted Sales'}, title="Actual vs Predicted Sales")
    st.plotly_chart(scatter_plot)

# 3. Residual Plot
if option == 'Residual Plot':
    st.header('Residual Plot')
    residuals = y_test - y_pred
    residual_plot = px.scatter(x=y_pred, y=residuals, labels={'x': 'Predicted Sales', 'y': 'Residuals'}, title="Residual Plot")
    residual_plot.add_hline(y=0, line_dash="dash", line_color="red")
    st.plotly_chart(residual_plot)

# 4. Residual Distribution
if option == 'Residuals Distribution':
    st.header('Distribution of Residuals')
    residuals = y_test - y_pred
    residual_dist = px.histogram(residuals, nbins=50, marginal='violin', title="Distribution of Residuals")
    st.plotly_chart(residual_dist)

# 5. Model Performance
if option == 'Model Performance':
    st.header('Model Performance Metrics')
    r_squared = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    st.write(f"**R-squared:** {r_squared:.3f}")
    st.write(f"**Mean Squared Error (MSE):** {mse:.3f}")

    # Bar plot for R-squared and MSE
    performance_fig = go.Figure(go.Bar(x=['R-squared', 'MSE'], y=[r_squared, mse], marker_color=['blue', 'green']))
    performance_fig.update_layout(title_text="Model Performance Metrics", yaxis_title="Score")
    st.plotly_chart(performance_fig)

# 6. Learning Curve (if you've implemented it)
if option == 'Learning Curve':
    from sklearn.model_selection import learning_curve

    st.header('Learning Curve')
    train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=5, scoring='r2', n_jobs=-1)
    train_scores_mean = train_scores.mean(axis=1)
    test_scores_mean = test_scores.mean(axis=1)

    # Plot learning curve
    learning_curve_fig = go.Figure()
    learning_curve_fig.add_trace(go.Scatter(x=train_sizes, y=train_scores_mean, mode='lines', name='Training Score'))
    learning_curve_fig.add_trace(go.Scatter(x=train_sizes, y=test_scores_mean, mode='lines', name='Validation Score'))
    learning_curve_fig.update_layout(title='Learning Curve', xaxis_title='Training Size', yaxis_title='R-squared Score')
    st.plotly_chart(learning_curve_fig)
