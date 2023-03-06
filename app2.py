import streamlit as st
import pandas as pd
import numpy as np
import folium
import os
from PIL import Image
from streamlit_folium import st_folium


# define map

def display_map(location, marker_list, map_type = 'Stamen Terrain'):

    map = folium.Map(location=location, zoom_start = 12, scrollWHEELZoom = False, 
                     tiles='Stamen Terrain')
    
    for idx, m in enumerate(marker_list):
        marker = folium.Marker(m, popup='WC_{}'.format(idx+1),tooltip='WC_{}'.format(idx+1), icon=folium.Icon(color='blue'))
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
    image_list = os.listdir('data2')
    data_0 = {}
    for image_name in image_list:
        data_0[image_name.split('_')[0]] = []
    
    for image_name in image_list:
        data_0[image_name.split('_')[0]].append(image_name.split('_')[1].split('.')[0])

    
    
    # sidebar
    # side_bar_spot = st.sidebar.selectbox('지점',df_water['name'].unique())
    side_bar_1 = st.sidebar.multiselect('데이터 대분류', data_0.keys())
    side_bar_final = {}
    
    for side_bar in side_bar_1:
        side_bar_final[side_bar] = st.sidebar.multiselect(side_bar, data_0[side_bar])

    
    #for side_bar in side_bar_1:
    #    st.sidebar.multiselect(side_bar, data_0[side_bar])
        

    

    
    
    # map
    location = [37.19286918883309,127.01259613037111]
    marker_list = [[37.23101, 127.02922],[37.23104, 127.0286],[37.22671, 127.02342],[37.22008, 127.02076],[37.2094, 127.02046],[37.16725, 126.99763],[37.12476, 127.00043]]
    
    map_info = display_map(location, marker_list)
    
    # display checked file
    for big in side_bar_final.keys():
        for small in side_bar_final[big]:
            
            st.markdown("<h3 style='text-align: center; color: black;'>{}</h1>".format(big+'_'+small), unsafe_allow_html=True)

            
            image = Image.open('data2//'+big+'_'+small+'.jpg')
            st.image(image, caption= big+'_'+small, width = 700)
            

        
    #st.markdown("<h2 style='text-align: center; color: black;'>{}</h1>".format('WC_'+str(marker_list.index(map_info)+1)), unsafe_allow_html=True)







if __name__ == '__main__':
    main()