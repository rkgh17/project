import streamlit as st
from streamlit_option_menu import option_menu
from all_user_graph import all_graph1
from all_user_graph import all_graph2

mdbr = '''
    
---
    
'''

def run_seoul_bike_app():
    tab1, tab2 = st.tabs(["전체 이용자","신규 가입자"])

    with tab1:
        st.header('공공자전거 이용자 수 추이')
        st.image('data/공공자전거 이용정보(월별)/따릉이 이용자 수 추이.png')
        # fig1 = all_graph1()
        # st.pyplot(fig1)
        graph_inter1 = '''

        ### (그래프 해석) 전체 이용자 수

        - 2017이후 따릉이 이용자 수 꾸준히 상승추세
        - 날씨의 영향으로 여름과 겨울에는 이용자 수가 감소

        '''
        st.markdown(graph_inter1, unsafe_allow_html=True)

        st.markdown(mdbr, unsafe_allow_html=True)
        st.header('공공자전거 이용자 수 추이(연도별)')
        st.image('data/공공자전거 이용정보(월별)/따릉이 이용자 수 추이(연도별).png')
        # fig2 = all_graph2()
        # st.pyplot(fig2)
        graph_inter2 = '''

        ### (그래프 해석) 월별 이용자 수

        - 날씨가 좋은 봄과 가을에 이용자 수 상승
        - 전체 이용자 수 증가에 따라 여름에는 이용자 수가 증가하였으나, 상대적으로 겨울에는 크게 증가하지 못함

        '''
        st.markdown(graph_inter2, unsafe_allow_html=True)

    with tab2:
        st.header('공공자전거 신규가입(누적)')
        st.image('data/신규가입자 정보(월별)/따릉이 신규가입 누적.png')
        graph_inter1 = '''

        ### (그래프 해석) 신규 가입 건수

        - 신규 가입자 꾸준히 상승
        - 코로나 영향으로 인해 2020년 성장세가 이전보다 가파름

        '''
        st.markdown(graph_inter1, unsafe_allow_html=True)

        st.markdown(mdbr, unsafe_allow_html=True)
        st.header('공공자전거 신규가입 추이')
        st.image('data/신규가입자 정보(월별)\따릉이 신규가입 추이.png')
        graph_inter2 = '''

        ### (그래프 해석) 신규 가입 건수

        - 날씨가 좋은 봄과 가을에 가입자 수 상승

        '''
        st.markdown(graph_inter2, unsafe_allow_html=True)

        st.markdown(mdbr, unsafe_allow_html=True)
        st.header('공공자전거 연령대별 신규가입(누적)')        
        st.image('data/신규가입자 정보(월별)\따릉이 연령대별 누적 가입자.png')
        graph_inter3 = '''

        ### (그래프 해석) 연령대별 누적 가입자

        - 20대 > 30대 > 40대 > 10대 > 50대 > 60대 > 70대 순 유지

        '''
        st.markdown(graph_inter3, unsafe_allow_html=True) 