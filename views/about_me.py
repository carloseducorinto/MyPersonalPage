import streamlit as st
import base64
from streamlit_player import st_player
#from forms.contact import contact_form



st.set_page_config(layout='centered')

# -- Profile Section

def contact_form():
    with st.form('contact_form'):
        name = st.text_input('Name')
        email = st.text_input('Email Address')
        message= st.text_area('Your Message')
        submit_button = st.form_submit_button('Submit')
        
        if submit_button:
            st.success('Message successfully sent!')

@st.experimental_dialog('Contact Me')
def show_contact_form():
    contact_form()

col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
with col1:
    st.image("../assets/cadu_profile_v1.png", width=230)
with col2:
    st.title('Carlos Eduardo Gabriel Santos', anchor=False)
    st.write(
        'Global Senior Data Architect, supporting a financial organization in data-driven decision-making. Also an AI Researcher, conducting various experiments in the field of Generative AI.'
    )    
    
    #if st.button(":email: Contact Me"):
    #    show_contact_form()

# -- Experience & Qualifications ---
st.write('\n')
st.subheader('About', anchor=False)
st.write(""" 
- Over 20 years of experience in the banking and technology consulting industries, holding roles such as IT project manager, system developer, programmer, and business analyst at companies like 7Comm, TQI and Stefanini IT Solutions. Currently he serves as the Global Data Architect at Citi.
- Proficient in Java and Python for Data Science, as well as database management systems like SQL Server and Oracle, with deep knowledge in Credit Risk, Trade Finance, and Services.
- Passionate about innovation and digital transformation, with a track record of managing and delivering complex projects, leading cross-functional teams, and ensuring adherence to financial and technical standards.
- Committed to accountability, adaptability, and resilience, with a hands-on approach to providing practical and effective solutions to complex problems.
         """)

st.write('\n')  
#st.subheader('Discover more Details', anchor=False) 
st.sidebar.markdown(
    """<a href="https://www.linkedin.com/in/carlos-eduardo-gabriel-santos/">
    <img src="data:image/png;base64,{}" width="400">
    </a>""".format(
        base64.b64encode(open("../assets/linkedin_cadu.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)


st.write('\n')  
st.subheader('Publications and Interviews', anchor=False) 
st_player('https://www.youtube.com/watch?v=ccCDMFC1YXU')
st.caption('<div style="text-align: center">Life at Citi</div>', unsafe_allow_html=True)
st.write('\n')
st.write('\n')  
st_player('https://www.youtube.com/watch?v=CMK8ibTagYc')
st.caption('<div style="text-align: center">TV Cultura - Programa Estação Livre</div>', unsafe_allow_html=True)
st.write('\n')
st.write('\n')  
st_player('https://www.youtube.com/watch?v=m219wlZeP5s')
st.caption('<div style="text-align: center">Duca - The Virtual Assistant in Action</div>', unsafe_allow_html=True)
st.write('\n')
st.write('\n')  
#st.subheader('Other', anchor=False) 
# Define the path to the image
#image_path = '../assets/oglobo.png'
#from PIL import Image
#width = st.slider('What is the width in pixels?', 0, 700, 350)
#put your own image here
#image = Image.open(image_path) 
#st.image(image, caption='Entrevista Jornal O Globo', width=350)
print('sucesso') 
st.write('\n')
st.write('\n')  
st.markdown('[Entrevista a respeito de Inteligência Artificial para o Portal Próximo Nivel - Embratel](https://proximonivel.embratel.com.br/citi-avanca-no-uso-de-inteligencia-artificial/)')
st.write('\n')
st.write('\n')  
st.markdown('[Entrevista Jornal o Dia - Rio de Janeiro](https://odia.ig.com.br/rio-de-janeiro/2020/07/5948202-carlos-eduardo-santos--gerente-de-projetos-de-tecnologia-do-citi.html)')
st.write('\n')
st.write('\n')  
st.markdown('[Entrevista Jornal O Globo](https://oglobo.globo.com/economia/celina/noticia/2020/08/sob-pressao-empresas-encaram-diversidade-mudam-estruturas-para-contratar-mais-negros-mulheres-lgbts-24562645.ghtml)')

