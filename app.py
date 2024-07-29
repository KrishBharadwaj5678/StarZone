import requests
import streamlit as st

st.set_page_config(
    page_title="Star Hub",
    page_icon="icon.png",
    menu_items={
        "About":"Welcome to StarHub, your ultimate destination for celebrity information.Stay informed and entertained with comprehensive insights into the lives and careers of celebrities around the world."
    }
)

st.write("<h2 style='color:#77E4C8;font-size:31px;'>Discover Everything About Your Favorite Celebrities.</h2>",unsafe_allow_html=True)

name=st.text_input("Enter Celebrity Name",placeholder="the rock")

btn=st.button('Search')
if btn:
    api_url = 'https://api.api-ninjas.com/v1/celebrity?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6'})
    if response.status_code == requests.codes.ok:
        data=response.json()
        if(len(data)==0):
            st.info("Celebrity Information Unavailable.")
        else:
            for i in data:
                st.write(f"<h2 style='color:#FFB200;font-size:33px;'>{i['name'].title()}</h2>",unsafe_allow_html=True)

                def checkDataExistence(data,label,extrainfo):
                    if(isinstance(data,list)):
                        occupation=""
                        for j in data:
                            if("_" in j):
                                splitted_words=j.split("_")
                                combinedOccup=" ".join(words.title() for words in splitted_words)
                                occupation+=combinedOccup+", "
                            else:
                                occupation+=j.title()+", "
                                
                        occupation=occupation.rstrip(", ")

                        st.write(f"<li style='font-size:25px;'>{label}: {occupation}</li>",unsafe_allow_html=True)
                        
                    elif(len(str(data))>=1):
                        st.write(f"<li style='font-size:25px;'>{label}: {data}{extrainfo}</li>",unsafe_allow_html=True)
                    
                try:checkDataExistence(i['net_worth'], "Net Worth",'')
                except:pass

                try:checkDataExistence(i['gender'].title(), "Gender",'')
                except:pass

                try:checkDataExistence(i['birthday'], "DOB",'')
                except:pass

                try:checkDataExistence(i['death'], "Death",'')
                except:pass

                try:checkDataExistence(i['nationality'].upper(), "Nationality",'')
                except:pass
                
                try:checkDataExistence(i['age'], "Age",'')
                except:pass

                try:checkDataExistence(i['height'], "Height","m")
                except:pass

                try:
                    is_alive = "Yes" if i['is_alive'] else "No"
                    checkDataExistence(is_alive, "Alive",'')
                except:pass

                try:checkDataExistence(i['occupation'], "Occupation",'')
                except:pass