#By Ansh Bhavesh Nikhil
#https://drive.google.com/drive/u/0/folders/1zLdC-oq33tLV1Um4nOMuB3HkiB7IBcRo     Video Presentation
import speech_recognition as sr
import webbrowser as wb
import smtplib
import time
from googletrans import Translator
def amazon(get):
    url="https://www.amazon.in/s?k="
    return url+get+'&ref=nb_sb_noss_1'
def google(get):
    url='https://www.youtube.com/results?search_query='
    return url+get
def search(get):
    url="https://www.google.com/search?q="
    return url+get
def map(get):
    url='https://www.google.com/maps/place/'
    return url+get

r=sr.Recognizer()

with sr.Microphone ()as source:
    print("speak now")
    audio=r.listen(source)
try:
    if 'hello there'in r.recognize_google(audio):
        i=0
        while(1):
            i=i+1
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('Give a Command')
                audio=r.listen(source)
            if ('Amazon'in r.recognize_google(audio)):
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print('what to be searched')
                    audio = r.listen(source)
                try:
                    get=r.recognize_google(audio)
                    print(get)
                    url=amazon(get)
                    wb.get().open_new_tab(url)
                except sr.UnknownValueError:
                    print('Could not request results')
                except sr.RequestError as e:
                    print('failed'.format(e))
            elif ('You'in r.recognize_google(audio)):
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print('what to be searched')
                    audio = r.listen(source)
                try:
                    get=r.recognize_google(audio)
                    print(get)
                    url=google(get)
                    wb.get().open_new_tab(url)
                except sr.UnknownValueError:
                    print('Could not request results')
                except sr.RequestError as e:
                    print('failed'.format(e))
            elif ('search'in r.recognize_google(audio)):
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print('To be searched in hindi or english?')
                    audio = r.listen(source)
                try:
                    get = r.recognize_google(audio)
                    print(get)
                    if("Hindi" in get):
                        trans=Translator()
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print(trans.translate('what to be searched',dest='hi').text)
                            audio = r.listen(source)
                        try:
                            get=r.recognize_google(audio)
                            #print(get)
                            trans=Translator()
                            get_result=trans.translate(get,dest='hi')
                            #print(type(get_result))
                            get2=get_result.text
                            #print(type(get2))
                            print(get2)
                            url=search(get2)
                            wb.get().open_new_tab(url)
                        except sr.UnknownValueError:
                            print('Could not request results')
                        except sr.RequestError as e:
                            print('failed'.format(e))
                    else:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print('what to be searched')
                            audio = r.listen(source)
                        try:
                            get = r.recognize_google(audio)
                            print(get)
                            url = search(get)
                            wb.get().open_new_tab(url)
                        except sr.UnknownValueError:
                            print('Could not request results')
                        except sr.RequestError as e:
                            print('failed'.format(e))
                except sr.UnknownValueError:
                    print('Could not request results')
                except sr.RequestError as e:
                    print('failed'.format(e))
            elif ('map'in r.recognize_google(audio)):
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print('what to be searched')
                    audio = r.listen(source)
                try:
                    get=r.recognize_google(audio)
                    print(get)
                    url=map(get)
                    wb.get().open_new_tab(url)
                except sr.UnknownValueError:
                    print('Could not request results')
                except sr.RequestError as e:
                    print('failed'.format(e))
            elif ('text'in r.recognize_google(audio)):
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("what is reciever's email address?\t")
                    audio = r.listen(source)
                try:
                            email = r.recognize_google(audio)
                            print(email.replace(" ","").lower())
                            #get = r.recognize_google(audio)
                            #print(get)
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print('what to be mailed')
                                audio = r.listen(source)
                            try:
                                get = r.recognize_google(audio)
                                #print(get)
                                trans = Translator()
                                get_result = trans.translate(get, dest='en')
                                get2 = get_result.text
                                if(get!=get2):
                                    print(trans.translate(get,dest='hi').text)
                                else:
                                    print(get)
                                #print(get2)
                                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                                server.login("pythonproject321@gmail.com", "pythonproject1234")
                                server.sendmail("pythonproject321@gmail.com", email.replace(" ",""),get2)
                                server.quit()
                                print('email has been sent')
                            except sr.UnknownValueError:
                                print('Could not request results')
                            except sr.RequestError as e:
                                print('failed'.format(e))
                except sr.UnknownValueError:
                    print('Could not request results')
                except sr.RequestError as e:
                    print('failed'.format(e))
            elif ('news' in r.recognize_google(audio)):
                wb.get().open_new_tab('https://news.google.com/')
            elif ('cal' in r.recognize_google(audio)):
                wb.get().open_new_tab('https://calendar.google.com/')
            else:
                print('i am still learning this command!')
            if(i>8):
                print("exiting")
                break
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    time.sleep(3)
                    print("want to ask something more ?")
                    audio = r.listen(source)
                if('no'in r.recognize_google(audio)):
                    print('bye')
                    break
            except sr.UnknownValueError:
                print('bye')
                break
            except sr.RequestError as e:
                print('failed'.format(e))
    else :
        print("you were not audible")
except sr.UnknownValueError:
    print('Could not request results')
except sr.RequestError as e:
    print('failed'.format(e))