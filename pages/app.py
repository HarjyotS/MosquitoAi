import streamlit as st
import torch
from PIL import Image
import numpy as np
import plotly.express as px
import pandas as pd
import math

st.set_page_config(page_title="MosquitoAi App")
# dengue fever
dtext = """
Dengue fever is a viral illness transmitted by the bite of an infected mosquito.
It is caused by one of four closely related dengue viruses (DENV-1, DENV-2, DENV-3, or DENV-4).

Symptoms of dengue fever typically begin 3-14 days after being bitten by an infected mosquito
and may include high fever, severe headache, joint and muscle pain, and a rash. Some people may
also experience nausea, vomiting, and diarrhea. In severe cases, dengue fever can progress to
dengue hemorrhagic fever, a potentially life-threatening condition characterized by bleeding,
low platelet count, and difficulty breathing.

Dengue fever is found in tropical and subtropical regions of the world, including parts of Africa,
the Americas, Southeast Asia, and the Western Pacific. It is most commonly transmitted by the Aedes
mosquito, which bites during the day and is found in urban areas.

There is no specific treatment for dengue fever. Management of the disease typically involves pain relief,
rest, and rehydration. In severe cases, hospitalization may be necessary.

To prevent dengue fever, it is important to protect against mosquito bites by using mosquito nets,
wearing long-sleeved clothing, and using insect repellents. In areas where dengue fever is prevalent,
it is also important to eliminate standing water, where mosquitoes can breed. A vaccine is available
in some countries, but it is not fully effective and is not recommended for everyone.
"""
ytext = """
Yellow fever is a viral illness transmitted by the bite of an infected mosquito.
It is caused by the yellow fever virus, which is a member of the flavivirus family.

Symptoms of yellow fever typically begin 3-6 days after being bitten by an infected
mosquito and may include fever, chills, headache, muscle pain, and nausea. In severe cases
, yellow fever can progress to a more serious phase characterized by high fever, jaundice
(yellowing of the skin and whites of the eyes), abdominal pain, and vomiting. In the most
severe cases, yellow fever can lead to multiple organ failure and death.

Yellow fever is found in tropical and subtropical regions of Africa and South America.
It is most commonly transmitted by the Aedes mosquito, which bites during the day and
is found in urban areas.

There is no specific treatment for yellow fever. Management of the disease typically involves
supportive care, such as pain relief, hydration, and rest. In severe cases, hospitalization
may be necessary.

To prevent yellow fever, it is important to protect against mosquito bites by using mosquito nets,
wearing long-sleeved clothing, and using insect repellents. In areas where yellow fever is prevalent,
it is also important to eliminate standing water, where mosquitoes can breed. A vaccine is available
for yellow fever and is recommended for travelers to areas where the disease is present. The vaccine
is highly effective and provides long-lasting immunity against the disease.
"""
ztext = """
Zika virus is a viral illness transmitted by the bite of an infected mosquito. It is caused by the
Zika virus, which is a member of the flavivirus family.

Symptoms of Zika virus infection are typically mild and may include fever, rash, joint pain,
and conjunctivitis (red eyes). Many people infected with Zika virus do not have any symptoms.
However, Zika virus infection during pregnancy can cause severe birth defects, including 
microcephaly (abnormally small head size) and other brain abnormalities.

Zika virus is found in tropical and subtropical regions of the world, including parts of Africa,
the Americas, Southeast Asia, and the Western Pacific. It is most commonly transmitted by the
Aedes mosquito, which bites during the day and is found in urban areas. Zika virus can also be
transmitted sexually and from mother to child during pregnancy or childbirth.

There is no specific treatment for Zika virus infection. Management of the disease typically 
involves supportive care, such as pain relief, hydration, and rest. In severe cases, hospitalization
may be necessary.

To prevent Zika virus infection, it is important to protect against mosquito bites by using mosquito
nets, wearing long-sleeved clothing, and using insect repellents. In areas where Zika virus is
prevalent, it is also important to eliminate standing water, where mosquitoes can breed. There
is currently no vaccine available for Zika virus.
"""

ctext = """
Chikungunya is a viral illness transmitted by the bite of an infected mosquito.
It is caused by the chikungunya virus, which is a member of the alphavirus family.

Symptoms of chikungunya typically begin 3-7 days after being bitten by an infected
mosquito and may include fever, joint pain, muscle pain, headache, and rash. The
joint pain can be severe and can last for several weeks or even months. Some people
may also experience nausea, vomiting, and fatigue. In rare cases, chikungunya can
lead to more serious complications, including neurological and cardiovascular problems.

Chikungunya is found in tropical and subtropical regions of the world, including parts
of Africa, Asia, the Caribbean, Central and South America, and the Indian subcontinent. 
It is most commonly transmitted by the Aedes mosquito, which bites during the day and
is found in urban areas.

There is no specific treatment for chikungunya. Management of the disease typically
involves supportive care, such as pain relief, hydration, and rest. In severe cases
, hospitalization may be necessary.

To prevent chikungunya, it is important to protect against mosquito bites by using
mosquito nets, wearing long-sleeved clothing, and using insect repellents. In areas
where chikungunya is prevalent, it is also important to eliminate standing water,
where mosquitoes can breed. There is currently no vaccine available for chikungunya.
"""

wntext = """
West Nile virus is a viral illness transmitted by the bite of an infected mosquito.
It is caused by the West Nile virus, which is a member of the flavivirus family.

Symptoms of West Nile virus infection range from mild to severe and may include fever,
headache, body aches, joint pain, vomiting, diarrhea, and rash. In severe cases, West
Nile virus infection can lead to West Nile encephalitis, an inflammation of the brain,
or West Nile meningitis, an inflammation of the lining of the brain and spinal cord.
These serious complications can lead to seizures, paralysis, and death.

West Nile virus is found in Africa, the Middle East, Europe, and the United States.
It is most commonly transmitted by the Culex mosquito, which bites at night and is
found in urban areas.

There is no specific treatment for West Nile virus infection. Management of the disease
typically involves supportive care, such as pain relief, hydration, and rest. In severe
cases, hospitalization may be necessary.

To prevent West Nile virus infection, it is important to protect against mosquito bites
by using mosquito nets, wearing long-sleeved clothing, and using insect repellents. In 
areas where West Nile virus is prevalent, it is also important to eliminate standing water,
where mosquitoes can breed. There is currently no vaccine available for West Nile virus.
"""
ftext = """
Filariasis, also known as elephantiasis, is a tropical disease caused by parasitic worms called filarial worms.
The worms are transmitted to humans through the bite of infected mosquitoes.

The most common type of filariasis is caused by the worms Wuchereria bancrofti and Brugia malayi.
These worms can cause a range of symptoms, including fever, swelling of the arms, legs, and genitalia,
and lymphatic dysfunction. In severe cases, filariasis can lead to elephantiasis, a condition in which
the limbs or other body parts become severely swollen and disfigured.

Filariasis is found in tropical and subtropical regions of the world, including parts of
Africa, Asia, the Caribbean, and South America. It is most commonly transmitted by the
Aedes mosquito, which bites during the day and is found in urban areas.

There is no specific treatment for filariasis. Management of the disease typically
involves medications to kill the worms and reduce inflammation. In severe cases, 
surgery may be necessary to remove damaged tissue or to improve lymphatic flow.

To prevent filariasis, it is important to protect against mosquito bites by using 
mosquito nets, wearing long-sleeved clothing, and using insect repellents. In areas
where filariasis is prevalent, it is also important to eliminate standing water, where
mosquitoes can breed. There is currently no vaccine available for filariasis.
"""
etext = """
Encephalitis is an inflammation of the brain that can be caused by a variety of factors,
including infections, autoimmune disorders, and toxins.

Symptoms of encephalitis may include fever, headache, confusion, seizures, and changes in
behavior or consciousness. In severe cases, encephalitis can lead to coma, paralysis, or death.

Encephalitis can be caused by a number of different pathogens, including viruses, bacteria,
and parasites. The most common causes of viral encephalitis are herpes simplex virus (HSV),
varicella-zoster virus (VZV), and arboviruses (such as West Nile virus, Japanese encephalitis
virus, and others). Bacterial encephalitis is less common but can be caused by bacteria such
as Haemophilus influenzae, Streptococcus pneumoniae, and Neisseria meningitidis.

Treatment of encephalitis typically involves medications to control the inflammation and to
treat the underlying cause, if known. In severe cases, hospitalization and supportive care,
such as oxygen therapy and fluid management, may be necessary.

To prevent encephalitis, it is important to practice good hygiene, such as washing your hands
frequently and avoiding close contact with people who are sick. It is also important to get
vaccinated against viruses that can cause encephalitis, such as measles, mumps, rubella,
and varicella. In areas where arboviruses are prevalent, it is important to protect against
mosquito bites by using mosquito nets, wearing long-sleeved clothing, and using insect repellents.
"""
st.markdown(
    """
        <style>
            [data-testid="stSidebarNav"] {
                background-repeat: no-repeat;                
            }
            [data-testid="stSidebarNav"]::before {
                content: "MosquitoAi";
                margin-left: 20px;
                margin-top: 20px;

                font-size: 30px;
                text-align: center;
                position: relative;
            }
        </style>
        """,
    unsafe_allow_html=True,
)
st.title("MosquitoAi Application")
st.text(
    "Uplaod an image of a close up of a mosquito and we will tell you what type it is."
)
# read images.zip as a binary file and put it into the button
with open("images.zip", "rb") as fp:
    btn = st.download_button(
        label="Download test images",
        data=fp,
        file_name="images.zip",
        mime="application/zip",
    )
image = st.file_uploader(
    "Upload Image", type=["jpg", "jpeg", "png", "webp"], accept_multiple_files=False
)

if image:
    try:
        image = Image.open(image)
        model = torch.hub.load("WongKinYiu/yolov7", "custom", "trained7mai.pt")
        results = model(image, size=640)
        fig = px.imshow(np.squeeze(results.render()), aspect="equal")

        st.plotly_chart(fig)
        # st.text(results.pandas().xyxy)
        name = results.pandas().xyxy[0]["name"].unique()[0]
        confidence = round(
            (results.pandas().xyxy[0]["confidence"].unique()[0] * 100), 2
        )
        if name:
            st.text(f"Detected {name} with confidence {confidence}")
            if name == "Aedes Aegypti Landing" or name == "Aedes Aegypti Smashed":
                st.write(
                    """
                    Aedes aegypti is a mosquito species that is known to transmit diseases such as dengue fever,
                    yellow fever, and Zika virus. It is commonly found in tropical and subtropical regions,
                    including parts of the Americas, Africa, and Asia. This mosquito is small and dark in color,
                    with distinctive small white marking dots on its legs and thorax. It is primarily a daytime
                    feeder and is attracted to the carbon dioxide and heat emitted by humans. Aedes aegypti is also
                    known to breed in standing water, making it important to eliminate any sources of standing water
                    around the home in order to reduce the risk of mosquito bites.
                    """
                )
                st.image("images/Aedes_aegypti.jpg")
                st.write("Known Carried Diseases")

                tab1, tab2, tab3 = st.tabs(
                    ["Dengue Fever", "Yellow Fever", "Zika Virus"]
                )
                with tab1:
                    st.write(dtext)
                    st.write(
                        "More Info can be found on the [CDC website](https://www.cdc.gov/dengue/index.html)"
                    )
                with tab2:
                    st.write(ytext)
                    st.write(
                        "More Info can be found on the [CDC website](https://www.cdc.gov/yellowfever/index.html)"
                    )
                with tab3:
                    st.write(ztext)
                    st.write(
                        "More Info can be found on the [CDC website](https://www.cdc.gov/zika/index.html)"
                    )
            elif (
                name == "Aedes Albopictus Landing" or name == "Aedes Albopictus Smashed"
            ):
                st.write(
                    """
                    Aedes albopictus, also known as the Asian tiger mosquito, is a small, 
                    aggressive mosquito species that is native to Southeast Asia. It is known
                    for its distinctive black and white striped legs and thorax, and is active during the day.
                    This mosquito is a vector for a number of diseases, including dengue fever, Zika virus, chikungunya
                    , and yellow fever. It has a wide range of habitats and is capable of breeding in small containers of water,
                    making it difficult to control. Aedes albopictus has spread to many countries worldwide 
                    through the transportation of goods and has become a significant public health threat in many areas.
                    """
                )
                st.image("images/Aedes-albopictus.jpg")
                st.write("Known Carried Diseases")
                btab1, btab2, btab3, btab4 = st.tabs(
                    ["Dengue Fever", "Yellow Fever", "Zika Virus", "Chikungunya"]
                )
                with btab1:
                    st.write(dtext)
                    st.write(
                        "More Info can be found on the [CDC website](https://www.cdc.gov/dengue/index.html)"
                    )
                with btab2:
                    st.write(ytext)
                    st.write(
                        "More Info can be found on the [CDC website](https://www.cdc.gov/yellowfever/index.html)"
                    )
                with btab3:
                    st.write(ztext)
                    st.write(
                        "More Info can be found on the [CDC website](https://www.cdc.gov/zika/index.html)"
                    )
                with btab4:
                    st.write(ctext)
                    st.write(
                        "More Info can be found on the [CDC website](https://www.cdc.gov/chikungunya/index.html)"
                    )
            elif name == "Culex Quinq Landing" or name == "Culex Quinq Smashed":
                st.write(
                    """
                    Culex quinquefasciatus, also known as the southern house mosquito,
                    is a species of mosquito that is commonly found in tropical and
                    subtropical regions around the world. It is known to transmit diseases
                    such as West Nile virus, filariasis, and encephalitis. This mosquito
                    is typically grey or brown in color and has distinctive white bands on
                    its legs and thorax. It is a nocturnal feeder and is attracted to the
                    carbon dioxide and heat emitted by humans. Culex quinquefasciatus is known
                    to breed in standing water, such as in areas with high levels of moisture
                    or in areas with poor drainage. To reduce the risk of mosquito bites, it 
                    is important to eliminate any sources of standing water around the home and
                    to use insect repellents when outdoors.
                    """
                )
                st.image("images/Culex_quinq.jpg")
                st.write("Known Carried Diseases")
                ctab1, ctab2, ctab3 = st.tabs(
                    ["West Nile virus", "Filariasis", "Encephalitis"]
                )
                with ctab1:
                    st.write(wntext)
                    st.write(
                        "More Info can be found on the [CDC website](https://www.cdc.gov/westnile/index.html)"
                    )
                with ctab2:
                    st.write(ftext)
                    st.write(
                        "More Info can be found on the [CDC website](https://www.cdc.gov/parasites/lymphaticfilariasis/index.html)"
                    )
                with ctab3:
                    st.write(etext)
                    st.write(
                        "More Info can be found on the [CDC website](https://www.cdc.gov/easternequineencephalitis/index.html)"
                    )

    except:
        st.text("No mosquitos detected.")
