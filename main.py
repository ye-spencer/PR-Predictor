import requests 
from bs4 import BeautifulSoup 

def main():
    athleteid = 24094886
    athletic_url = "https://www.athletic.net/athlete/" + str(athleteid) + "/track-and-field/all"
    test = getdata("https://www.google.com")
    print(test.prettify())
    
def getdata(url):
    r = requests.get(url) 
    return r.text 

def html_code(url): 
  
    htmldata = getdata(url) 
    soup = BeautifulSoup(htmldata, 'html.parser') 

    return(soup) 

if __name__ == "__main__":
    main()