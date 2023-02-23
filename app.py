import streamlit as st
import pandas as pd
import numpy as np
import folium
import os
from streamlit_folium import st_folium


# define map

def display_map(location, marker_list, map_type = 'Stamen Terrain'):

    map = folium.Map(location=location, zoom_start = 12, scrollWHEELZoom = False, 
                     tiles='Stamen Terrain')
    
    for idx, m in enumerate(marker_list):
        marker = folium.Marker(m, popup='WC_{}'.format(idx+1), icon=folium.Icon(color='blue'))
        marker.add_to(map)


    st_map = st_folium(map, width=700, height=450)
    
    if type(st_map['last_object_clicked']) == dict:
        return [st_map['last_object_clicked']['lat'],st_map['last_object_clicked']['lng']]
    
    else:
        return [37.23101, 127.02922]

def main():
    
    APP_TITLE = '수계방 GIS 시스템'
    APP_SUB_TITLE = 'Source: KHU water lab'
    
    st.set_page_config(APP_TITLE, layout= 'centered')
    #st.title(APP_TITLE)
    st.markdown("<h1 style='text-align: center; color: black;'>Waterlab GIS System</h1>", unsafe_allow_html=True)
    st.caption(APP_SUB_TITLE)
    
    # load data
    data_list = os.listdir('data')
    data_list2 = []
    for data in data_list:
        data_list2.append(data.split('.')[0])
    
    dataframes = {}
    for data in data_list:
        dataframes[data.split('.')[0]] = pd.read_csv('data//'+data)
    
    df_water = pd.read_csv('data//수질.csv')
    df_soil = pd.read_csv('data//토양.csv')
    
    
    
    
    
    # sidebar
    # side_bar_spot = st.sidebar.selectbox('지점',df_water['name'].unique())
    side_bar_datalist = st.sidebar.multiselect('열람 데이터', data_list2)
    
    side_bar_cartegori_dict = {}
    for data in side_bar_datalist:
        side_bar_cartegori_dict[data] = st.sidebar.multiselect(data, pd.read_csv('data//'+data+'.csv').columns.drop(['name', 'time']))
    
    
    # map
    location = [37.19286918883309,127.01259613037111]
    marker_list = [[37.23101, 127.02922],[37.23104, 127.0286],[37.22671, 127.02342],[37.22008, 127.02076],[37.2094, 127.02046],[37.16725, 126.99763],[37.12476, 127.00043]]
    
    map_info = display_map(location, marker_list)

        
    st.markdown("<h2 style='text-align: center; color: black;'>{}</h1>".format('WC_'+str(marker_list.index(map_info)+1)), unsafe_allow_html=True)
    for data in side_bar_datalist:
        st.markdown("<h4 style=' color: black;'>{}</h1>".format('WC_'+str(marker_list.index(map_info)+1)+' {}'.format(data)), unsafe_allow_html=True)
        for cartegori in side_bar_cartegori_dict[data]:
            st.markdown("<h5 style=' color: black;'>{}</h1>".format('WC_'+str(marker_list.index(map_info)+1)+' {}차트'.format(cartegori)), unsafe_allow_html=True)
            st.bar_chart(dataframes[data][['time', cartegori]].set_index('time'))
    







if __name__ == '__main__':
    main()