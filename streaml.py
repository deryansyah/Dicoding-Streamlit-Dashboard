import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



path = 'data/bike_sharing_day.csv'
df = pd.read_csv(path, sep=';')

# membuat dictionary season
season = {1: 'spring',
          2: 'summer',
          3: 'fall',
          4: 'winter'}

# map dictionary season ke dalam dataframe
df['season'] = df['season'].map(season)

# membuat dictionary season
weathersit = {1: 'Clear, Few clouds, Partly cloudy, Partly cloudy',
              2: 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
              3: 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
              4: 'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'}

# map dictionary season ke dalam dataframe
df['weathersit'] = df['weathersit'].map(weathersit)

season_data = df.groupby('season')['cnt'].mean()
weather_data = df.groupby('weathersit')['cnt'].mean()
weather_labels = ['Clear', 'Mist', 'Light Rain', 'Heavy Rain']

st.title("Bike Rental Analysis")

st.write(
    """
    Dashboard ini akan menjawab pertanyaan:
    1. Musim apa yang menjadi favorit pengendara sepeda?
    2. Situasi cuaca manakah yang menjadi favorit pengendara sepeda?

    Berikut grafik hasil penelusuran kami:
    """)

# Plotting the bar chart for season
fig1, ax1 = plt.subplots()
season_data.plot(kind='bar', color='skyblue', ax=ax1)
ax1.set_title('Average Count of Rented Bikes by Season')
ax1.set_xlabel('Season')
ax1.set_ylabel('Average Count')

# Plotting the bar chart for weathersit with custom xticks
fig2, ax2 = plt.subplots()
weather_data.plot(kind='bar', color='lightcoral', ax=ax2)
ax2.set_title('Average Count of Rented Bikes by Weather Situation')
ax2.set_xlabel('Weather Situation')
ax2.set_ylabel('Average Count')
ax2.set_xticks(range(len(weather_labels)))
ax2.set_xticklabels(weather_labels, rotation=45)

# Display the charts using Streamlit

st.write(
    """
    ## 1. Musim apa yang menjadi favorit pengendara sepeda?
    Musim gugur (Fall) menjadi musim favorit pengendara sepeda diikuti musim panas.
    Musim dingin (winter) secara mengejutkan menjadi musim favorit ketiga dengan
    """)
st.pyplot(fig1)

st.write(
    """
    ## 2. Situasi cuaca manakah yang menjadi favorit pengendara sepeda?
    Situasi cuaca yang cerah menjadi favorit pengendara sepeda dengan situasi cuaca hujan gerimis menjadi favorit kedua.
    Situasi cuaca berkabut tidak terlalu disukai pengendara sepeda dan hujan deras tak ada satupun yang bersepeda
    """)
st.pyplot(fig2)