from requests_html import HTMLSession
import datetime


def find(text, element):
    try:
        index = text.index(element)
        return text[index+1]
    except:
        return ''


def scrape(wipono):
    session = HTMLSession()
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"}
    data = {}
    status_url = f'https://patentscope.wipo.int/search/en/detail.jsf?docId={wipono}&_cid=P11-KQ6CCK-39257-2'
    # FETCHING STATUS RELEATED DETAILS
    html = session.get(status_url)
    html = html.html
    data['publicationNumber'] = ''
    data['publicationDate']=''
    data['Title']=''
    data['international_app']=''
    data['International_Filing']=''
    data['Applicants']=''
    data['Inventors']=''
    data['Agents']=''
    data['Priority_Data']=''
    elements = html.find('div.ps-field.ps-biblio-field')

    for element in elements:
         temp = element.text
         if "Publication Number" in temp:
             temp = temp.split()
             temp.reverse()
             data['publicationNumber']  = temp[0]

         if "Publication Date" in temp:
             temp = temp.split()
             temp.reverse()
             data['publicationDate'] = temp[0]

         if "Title" in temp:
             #print("this is title")
             #print(element)
             titleval=element.find('.needTranslation-biblio')
             for c in titleval:
                 data['Title']= c.text

         if "International Application No." in temp:
             temp = temp.split()
             temp.reverse()
             data['international_app'] = temp[0]

         if "International Filing Date" in temp:
             temp = temp.split()
             temp.reverse()
             data['International_Filing'] = temp[0]

         if "Applicants" in temp:
             Applicants = temp
             Applicants=Applicants.replace("Applicants","")
             data['Applicants']=Applicants.strip()

         if "Inventors" in temp:
             Inventors = temp
             Inventors=Inventors.replace("Inventors","")
             data['Inventors']=Inventors.strip()

         if "Agents" in temp:
             #print(temp)
             Agents = temp
             Agents=Agents.replace("Agents","")
             data['Agents']=Agents.strip()

         if "Priority Data" in temp:
             date = element.find('tr',first=True)
             data['Priority_Data']=(date.text)
             #Priority_Data = temp
             #Priority_Data=Priority_Data.replace("Priority Data","")
             #Priority_Data=Priority_Data.strip()
             #Priority_Data=Priority_Data.split(" ")
             #Priority_Data=Priority_Data[0]
   
        
    
    
            

    # print("publication number is")
    # print(publicationNumber)
    # print("publication date is")
    # print(publicationDate)
    # print("title is")
    # print(Title)
    # print("this is internation application no")
    # print(international_app)
    # print("international filing date is")
    # print(International_Filing)
    # print("Applicants name is")
    # print(Applicants)
    # print("this is inventors")
    # print(Inventors)
    # print("Agents name is")
    # print(Agents)
    # print("Prioriy data is")
    # print(Priority_Data)
    return data


if __name__ == '__main__':
    print(scrape('79319876'))
# 76709358

         
