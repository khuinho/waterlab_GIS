import streamlit as st 
import pandas as pd
import folium
from streamlit_folium import st_folium


APP_TITLE = '수계방 GIS 시스템'
APP_SUB_TITLE = 'Source: KHU water lab'

#def display_map(df_water, year, quarter):
#    df_water = df_water[(df_water['Year'] == year) & (df_water['Quarter']== quarter)]
#    st.write(df_water.shape)
#    st.write(df_water.head())

def display_map():

    map = folium.Map(location=[37.19286918883309,127.01259613037111], zoom_start = 12, scrollWHEELZoom = False, 
                     tiles='Stamen Terrain')
    
    marker = folium.Marker([37.23101, 127.02922], popup='WC_1', icon=folium.Icon(color='blue'))
    marker.add_to(map)

    marker = folium.Marker([37.23104, 127.0286], popup='WC_2', icon=folium.Icon(color='blue'))
    marker.add_to(map)

    marker = folium.Marker([37.22671, 127.02342], popup='WC_3', icon=folium.Icon(color='blue'))
    marker.add_to(map)

    marker = folium.Marker([37.22008, 127.02076], popup='WC_4', icon=folium.Icon(color='blue'))
    marker.add_to(map)

    marker = folium.Marker([37.2094, 127.02046], popup='WC_5', icon=folium.Icon(color='blue'))
    marker.add_to(map)

    marker = folium.Marker([37.16725, 126.99763], popup='WC_6', icon=folium.Icon(color='blue'))
    marker.add_to(map)

    marker = folium.Marker([37.12476, 127.00043], popup='WC_7', icon=folium.Icon(color='blue'))
    marker.add_to(map)

    st_map = st_folium(map, width=700, height=450)
    
        
    return st_map['last_object_clicked']
    
def main():
    
    st.set_page_config(APP_TITLE, layout= 'centered')
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)
            
    st.subheader('test')
    

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('S')
    with col2:
        st.write('S')
    with col3:
        st.write('S')

    #LOAD DATA
    
    df_water = pd.read_csv('data//수질.csv')
    st.write(df_water.shape)
    
    side_bar_spot = st.sidebar.selectbox('지점',df_water['name'].unique())
    side_bar_cartegori = st.sidebar.selectbox('수질_항목', df_water.columns.drop(['name', 'time']))
    
    lat_lng_dict = {
    '37.23101, 127.02922':'WC-1.' ,
    '37.23104, 127.0286':'WC-2.' ,
    '37.22671, 127.02342':'WC-3.' ,
    '37.22008, 127.02076':'WC-4.' ,
    '37.2094, 127.02046':'WC-5.' ,
    '37.16725, 126.99763':'WC-6.' ,
    '37.12476, 127.00043':'WC-7.' 
    }

    
    #DISPLAY FILTERS AND MAP

    last_click = display_map()

    lat, lng = -1, -1
    if type(last_click) == dict:
        lat , lng = last_click['lat'], last_click['lng']    
    
    st.write(lat, lng)
    df_sidebar = df_water[(df_water['name'] == side_bar_spot)]
    st.write(df_sidebar)    
    #st.bar_chart(df_sidebar)
    df_sidebar_SS = df_sidebar[['time', side_bar_cartegori]].set_index('time')
    st.bar_chart(df_sidebar[['time', side_bar_cartegori]].set_index('time'))
    
    
    #DISPLAY METRICS
if __name__ == '__main__':
    main()