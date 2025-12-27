# InternshipTasks-Month2
# Project-1 Supermarket Sales Analysis

## Project Overview
This project analyzes supermarket sales data to identify revenue trends, product performance, and customer purchasing behavior. The goal is to extract actionable business insights that support data-driven decision-making in retail operations.

## Business Objectives
- Analyze daily sales patterns
- Identify best-performing product categories
- Study customer spending behavior
- Detect peak sales hours

## Dataset
The dataset contains transactional sales records including product details, customer information, sales amounts, and timestamps.

## Tools & Technologies
- Python
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- Jupyter Notebook

## Key Analysis Performed
- Data cleaning and preprocessing
- Feature engineering (date and time extraction)
- Exploratory Data Analysis (EDA)
- Statistical summary and correlation analysis
- Data visualization

## Key Business Insights
- Sales fluctuate daily, indicating varying customer demand.
- A small number of product lines contribute most of the revenue.
- Member customers have higher average spending than non-members.
- Sales peak during specific hours of the day.

## Recommendations
- Focus promotions on high-performing product categories.
- Strengthen customer loyalty programs.
- Optimize staffing during peak sales hours.
- Introduce time-based offers during off-peak hours.

## Project Structure
Project-01-Supermarket-Sales/
├── data/
├── notebooks/
├── reports/
├── visuals/
├── README.md
└── requirements.txt


# Project-2 Student Performance Analysis
This project focuses on analyzing student academic performance using Exploratory Data Analysis (EDA). The objective is to identify key demographic, socio-economic, and academic factors that influence students’ exam scores and to derive meaningful insights that can support educational decision-making.
This project was completed as Project-2 for Month-2 of a Data Analysis Internship.

## Objectives
* Analyze subject-wise student performance (Math, Reading, Writing)
* Understand the impact of demographic factors such as gender and race/ethnicity
* Evaluate the influence of socio-economic indicators like lunch type and parental education
* Assess the effect of test preparation courses on academic performance
* Generate actionable insights using data visualization and statistical analysis

## Dataset Information
**Source:** Kaggle – *Students Performance in Exams*
**Records:** 1000 students
**Features Include:**
  * Gender
  * Race/Ethnicity
  * Parental Level of Education
  * Lunch Type
  * Test Preparation Course
  * Math Score
  * Reading Score
  * Writing Score
A new feature, **average_score**, was engineered to represent overall student performance.

## Tools & Technologies
* Python
* Jupyter Notebook
* NumPy
* Pandas
* Matplotlib
* Seaborn

## Project Workflow
1. Data Loading & Understanding
2. Data Cleaning & Validation
3. Feature Engineering
4. Univariate Analysis
5. Bivariate Analysis
6. Multivariate Analysis & Correlation
7. Insight Generation
8. Conclusion & Future Scope

## Key Insights
* Students generally perform better in reading and writing than in mathematics.
* Test preparation courses significantly improve student performance across all subjects.
* Female students tend to outperform male students in reading and writing, while males slightly lead in mathematics.
* Students receiving standard lunch perform better than those with free/reduced lunch.
* Higher parental education levels correlate with better student performance.
* Strong positive correlation exists between reading and writing scores.
  
## Conclusion

The analysis reveals that student performance is influenced by a combination of academic preparation, socio-economic background, and parental education. Among all factors, **test preparation emerges as the most impactful controllable variable**, suggesting that targeted academic interventions can substantially improve outcomes and reduce performance gaps.

## Future Scope

* Build predictive machine learning models to forecast student performance
* Incorporate additional features such as attendance and study hours
* Perform clustering to identify learning behavior patterns
* Develop personalized academic recommendation systems

## How to Run the Project
1. Clone the repository

   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory
3. Install required libraries

   ```bash
   pip install -r requirements.txt
   ```
4. Open the Jupyter Notebook and run all cells sequentially


# Project-3 Weather Analysis
## Project Overview
This project focuses on analyzing daily climate time-series data to understand long-term temperature trends, seasonal weather patterns, rainfall (humidity) distribution, and extreme weather events. Using statistical and time-series techniques, the goal is to extract meaningful insights that can support climate monitoring, forecasting, and decision-making for weather-sensitive domains such as agriculture, disaster management, and urban planning.
The project applies exploratory data analysis, trend smoothing, seasonal decomposition, correlation analysis, and anomaly detection to convert raw weather data into actionable climate intelligence.

## Dataset
Source: Kaggle – Daily Climate Time Series Dataset
File Used: DailyDelhiClimateTrain.csv
### Note: The train dataset was selected because it provides long, continuous historical records required for time-series trend analysis, seasonal decomposition, and anomaly detection. The test dataset is intended only for forecasting validation and was not suitable for exploratory analysis.

## Objectives
The primary goals of this project are:
-To analyze long-term temperature trends
-To identify seasonal weather patterns
-To study rainfall and humidity distribution
-To detect extreme weather events using statistical methods
-To generate insights useful for real-world climate applications

## Techniques Applied

The following analytical techniques were used:
-Exploratory Data Analysis (EDA)
-Time-series trend visualization
-30-day rolling mean smoothing
-Seasonal decomposition (Trend, Seasonal, Residual)
-Correlation and bivariate analysis
-Probability distribution analysis
-Z-score based extreme weather detection

## Key Analysis Performed
1. Temperature Trend Analysis-
Daily temperature values were plotted to observe overall trends and long-term variation in climate behavior.
2. Rolling Mean Analysis-
A 30-day rolling average was applied to remove short-term noise and highlight underlying temperature patterns.
3. Seasonal Decomposition-
The temperature series was decomposed into trend, seasonal, and residual components to understand periodic behavior and anomalies.
4. Bivariate & Correlation Analysis-
Relationships between temperature, humidity, wind speed, and pressure were analyzed to identify dependencies and interactions.
5. Rainfall (Humidity) Distribution-
The probability distribution of humidity was examined to understand typical and extreme moisture conditions.
6. Extreme Weather Detection-
Z-score statistical method was used to identify unusually high or low temperature values representing extreme climate events.

## Tools & Technologies
-Python
-Pandas
-NumPy
-Matplotlib
-Seaborn
-Statsmodels
-SciPy

## Conclusion
This project demonstrates how time-series analysis and statistical techniques can be applied to climate data to uncover seasonal patterns, long-term trends, and extreme weather events. The insights generated are useful for climate monitoring, agricultural planning, disaster preparedness, and environmental analytics.


# Project-4: COVID-19 Healthcare Trends
## Project Overview

The COVID-19 pandemic created unprecedented challenges for global healthcare systems.
This project analyzes global COVID-19 time-series data to understand infection trends, mortality patterns, healthcare burden, and growth dynamics.
The objective is to transform raw pandemic data into policy-relevant, actionable insights using data analytics and visualization techniques.

## Objectives

-Analyze long-term trends in COVID-19 cases and deaths
-Study daily infection and mortality behavior
-Identify pandemic waves using rolling averages
-Evaluate healthcare system burden using active cases
-Perform growth rate analysis to measure spread intensity
-Detect peak periods of maximum healthcare stress

## Dataset Description

Source: Global COVID-19 Dataset (Public Health Repository / Kaggle)
Type: Time-series healthcare data
Granularity: Daily records by country
Coverage: Global

## Data Preprocessing

The following preprocessing steps were applied:
-Converted the date column to datetime format
-Sorted data chronologically
-Aggregated country-level data to global trends
-Verified missing values and numeric consistency
-This ensured accurate and reliable time-series analysis

## Analysis Performed
1️⃣ Time-Series Trend Analysis
Cumulative cases and deaths were plotted to understand the overall progression of the pandemic.
2️⃣ Daily Case & Mortality Trends
Daily new cases and deaths were analyzed to observe short-term transmission and severity patterns.
3️⃣ Growth Rate Analysis
Daily growth rates were computed to identify periods of uncontrolled spread and effective containment.
4️⃣ Rolling Average & Wave Detection
A 7-day rolling average was applied to smooth daily fluctuations and reveal pandemic waves.
5️⃣ Healthcare Burden Analysis
Active cases were used to estimate healthcare system load, reflecting hospital and ICU pressure.
6️⃣ Peak & Extreme Event Detection
The date with the highest daily new cases was identified to determine peak healthcare stress.
7️⃣ Pre-Peak vs Post-Peak Comparison
Daily case trends before and after the peak were compared to study pandemic dynamics.

## Conclusion

This project demonstrates strong capability in:
-Time-series healthcare data analysis
-Growth and trend modeling
-Identifying pandemic waves and peak periods
-Deriving policy-relevant public health insights
-The analysis reflects real-world healthcare analytics skills using critical global health data.


# Project-5: Social Media Analytics

## Project Overview

This project focuses on analyzing social media engagement, user behavior, sentiment, and content trends using a real-world social media marketing dataset.
The goal is to transform raw digital interaction data into actionable business and marketing insights.
Unlike traditional business datasets, social media data is unstructured and behavioral in nature. This project demonstrates the ability to analyze modern digital platforms, which is critical for data-driven marketing, brand management, and audience growth.

## Objectives

-Analyze user engagement metrics (likes, shares, comments, impressions)
-Compare performance across social media platforms
-Identify time-based engagement trends
-Study the impact of sentiment on engagement
-Extract content and hashtag trends
-Generate business and marketing recommendations

## Dataset Description

Kaggle Dataset Name:
“Social Media Engagement Dataset”

The dataset contains social media posts with the following information:
-Post metadata (ID, time, platform)
-Engagement metrics (likes, shares, comments, impressions)
-Text content and hashtags
-Sentiment score and sentiment label
-Campaign information
It represents real-world social media marketing data, suitable for digital and behavioral analytics.

## Data Preparation

From the original 28 columns, only analytically relevant columns were selected:

-post_id
-timestamp, day_of_week
-platform
-text_content
-hashtags
-likes_count, shares_count, comments_count
-impressions
-sentiment_score, sentiment_label
-campaign_name, campaign_phase

Additional features engineered:

-Total Engagement = likes + shares + comments
-Engagement Rate = total engagement / impressions
-Time features (date, hour)

This converted raw data into a clean analytical dataset.


## Analysis Performed
1. Univariate Analysis-
Distribution of likes, shares, comments, impressions, and engagement rate
Identification of skewness and viral behavior

2. Platform-wise Analysis-
Comparison of engagement across platforms
Identification of high-performing platforms

3. Time-Series Analysis-
Daily engagement trends
Hour-wise engagement to find optimal posting times

4. Sentiment Analysis-
Comparison of engagement across positive, neutral, and negative posts

5. Campaign Performance-
Evaluation of campaign-wise engagement

6. Hashtag Trend Analysis-
Identification of trending topics and keywords

## Key Insights

-Engagement is highly skewed — a small number of posts generate very high interaction
-Certain platforms consistently outperform others
-Positive sentiment posts receive higher engagement
-Audience activity peaks during specific hours
-Campaign-driven content performs better than organic content
-Trending hashtags significantly boost reach

## Conclusion

This project demonstrates the ability to analyze modern digital data sources and convert raw social media activity into strategic marketing intelligence.
It highlights skills essential for roles in data analytics, digital marketing, and business intelligence.

