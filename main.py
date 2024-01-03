import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
import pyttsx3

wikipedia.set_lang('vi')
language = 'vi'


# path = ChromeDriverManager().install()

# chuyển văn bản thành âm thanh
def speak(text):
    print("Bot:  ", text)

    tts = gTTS(text=text, lang="vi", slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")


# chuyển giọng nói thành văn bản
def get_audio():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bot:  Đang nghe ! -- __ -- !")

        # ear_robot.pause_threshold = 4
        audio = ear_robot.record(source , duration= 4)
        # audio = ear_robot.listen(source, phrase_time_limit=5)

        try:
            print(("Bot :  ...  "))
            text = ear_robot.recognize_google(audio, language="vi-VN")
            print("Tôi:  ", text)
            return text
        except Exception as ex:
            print("Bot:  Lỗi Rồi ! ... !")
            return 0


def get_audio_2():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        ear_robot.pause_threshold = 2
        print("Đang nghe ===========================")
        audio = ear_robot.listen(source)
    try:
        text = ear_robot.recognize_google(audio, language="vi-VN")
    except:
        speak("Nhận dạng giọng nói thất bại. Vui lòng nhập lệnh ở dưới")
        text = input("Mời nhập: ")
    return text.lower()


def stop():
    speak("Hẹn gặp lại sau ! ... ")


def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Vui lòng nói lại!")
    time.sleep(3)
    stop()
    return 0


def hello(name):
    day_time = int(strftime('%H'))
    if 0 <= day_time < 11:
        speak(f"Chào bạn {name}. Chúc bạn buổi sáng tốt lành.")
    elif 11 <= day_time < 13:
        speak(f"Chào bạn {name}. Chúc bạn có một buổi trưa thật vui vẻ.")
    elif 13 <= day_time < 18:
        speak(f"Chào bạn {name}. Chúc bạn buổi chiều vui vẻ.")
    elif 18 <= day_time < 22:
        speak(f"Chào bạn {name}. Tối rồi, Bạn đã cơm nước gì chưa ?")
    elif 22 <= day_time <= 23:
        speak(f"Chào Bạn {name}. Muộn rồi bạn nên đi nghủ sớm nha.")
    else:
        speak(f"Thời gian bên tôi chưa đúng hoặc gặp lỗi. Bạn nên xem lại nha.")


def get_time(text):
    now = datetime.datetime.now()
    if 'giờ' in text:
        speak(f"Bây giờ là {now.hour} giờ {now.minute} phút {now.second} giây")
    elif "ngày" in text:
        speak(f"hôm nay là ngày {now.day} tháng {now.month} năm {now.year}")
    else:
        speak("Ý bạn là gì.")


def open_application(text):
    

    if 'notepad' in text:
        npath="C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(npath)
    if "google" in text:
        speak("Mở Google Chrome")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe")
    elif "powerpoint" in text:
        speak("Mở Microsoft Powerpoint")
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe")
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe")
    
    elif "zalo" in text:
        speak("Mở Zalo")
        os.startfile("C:\\Users\\ngoba\\AppData\\Local\\Programs\\Zalo\\Zalo.exe")
    elif "visual code" in text:
        speak("Mở Visual Studio Code")
        os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")
    elif "arduino" in text:
        speak("Mở Arduino IDE")
        os.startfile("C:\\Users\\ngoba\\AppData\\Local\\Programs\\Arduino IDE\\Arduino IDE.exe")
    elif "android studio" in text:
        speak("Mở Android Studio")
        os.startfile("C:\\Program Files\\Android\\Android Studio\bin\\studio64.exe")

    else:
        speak("Ứng dụng chưa cài đặt. Vui Lòng cài đặt cho tui nha !")


def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = "https://www." + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở. ")
        if input("Nếu muốn tiếp tục thì nhấn q: ") == "q":
            pass
        return True
    else:
        return False


def open_google_and_search(text):
    search_for = str(text).split("kiếm", 1)[1]
    url = f"https://www.google.com/search?q={search_for}"
    webbrowser.get().open(url)
    speak("Đây là thông tin bạn cần tìm")


def open_google_and_search2():
    speak("Nói thứ bạn cần tìm kiếm trên google")
    search = str(get_text()).lower()
    url = f"https://www.google.com/search?q={search}"
    webbrowser.get().open(url)
    speak("Đây là thông tin bạn cần tìm")



def play_youtube():
    speak("Nói nội dung bạn muốn tìm trên youtube")
    search = get_text()
    url = f"https://www.youtube.com/search?q={search}"
    webbrowser.get().open(url)
    speak("Đây là thứ mà tôi tìm được bạn xem qua nhé")


def play_youtube_2():
    speak("Nói nội dung bạn muốn tìm trên youtube")
    search = get_text()
    while True:
        result = YoutubeSearch(search, max_results=10).to_dict()
        if result:
            break
    url = f"https://www.youtube.com" + result[0]['url_suffix']
    webbrowser.get().open(url)
    speak("Đây là thứ mà tôi tìm được bạn xem qua nhé")
    print(result)


# url = 'https://api.unsplash.com/photos/random?client_id=' + \
#       api_key
def change_wallpaper():
    api_key = "XFyV6boeltUQBb9ROo5nPsWWvoPPDCPLRSwMaO_IXc4"
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
          api_key  # pic from unspalsh.com
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Location where we download the image to.
    urllib2.urlretrieve(photo, "D:\\Download____CocCoc\\a.png")
    image = os.path.join("D:\\Download____CocCoc\\a.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 3)
    speak("Hình nền máy tính bạn đã được thay đổi. Bạn ra home xem có đẹp không nha ?")



def tell_me_about():
    try:
        speak("Hãy nói cho tôi nghe Bạn muốn tìm gì ạ\\ ?")
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        dem = 0
        for content in contents[1:]:
            if dem < 2:
                speak("Bạn có muốn biết thêm không ???")
                ans = get_text()
                if 'có' not in ans:
                    break
            dem += 1
            speak(content)
        speak("Đây là nội dung tôi vừa tìm được cảm ơn bạn đã lắng nghe")
    except:
        speak(f"{name} không định nghĩa được thuật ngữ của bạn !!!")


def help_me():
    speak(f"""
    {robot_name} có thể giúp bạn thực hiện các việc sau đây:
    1. chào hỏi
    2. Hiển thị giờ
    3. Mở website, ứng dụng desktop
    4. Tìm kiếm với google
    5. Dự báo thời tiết
    6. Tìm kiếm video với youtube
    7. Thay đổi hình nền máy tính
    8. Định nghĩa với từ điển bách khoa toàn thư ( Wikipedia )
    """)

def main_brain():
    speak("Xin chào. Bạn tên là gì ?")
    global robot_name
    robot_name = "BOT"
    global name
    name = get_text()
    if name:
        speak(f'Xin chào bạn {name}.')
        speak(f'Bạn cần Bot giúp gì không ạ ?')
        while True:
            text = get_text()

            if not text:
                break
            elif ('tạm biệt' in text) or ('hẹn gặp lại' in text):
                stop()
                break
            elif "chào Bot" in text:
                hello(name)
            elif "hiện tại" in text:
                get_time(text)

            elif "mở" in text:

                if '.' in text:
                    open_website(text)
                
                else:
                    open_application(text)

            elif "tìm kiếm" in text:
                if str(text).split("kiếm", 1)[1] == "":
                    open_google_and_search2()
                else:
                    open_google_and_search(text)
            elif 'youtube' in text:
                speak("Bạn muốn tìm kiếm đơn giản hay phức tạp")
                yeu_cau = get_text()
                if "đơn giản" in yeu_cau:
                    play_youtube()
                    if input():
                        pass
                elif "phức tạp" in yeu_cau:
                    play_youtube_2()
                    if input("Tiếp tục y/n: ") == "y":
                        pass
            elif "hình nền" in text:
                change_wallpaper()
            elif "định nghĩa" in text:
                tell_me_about()
            elif "có thể làm gì" in text:
                help_me()
            elif "tắt máy" in text:
                os.system(f"shutdown -s -t 30")
            elif "khởi động lại" in text:
                os.system(f"shutdown -r -t 30")
            else:
                speak(f"Chức năng chưa có. Bạn vui lòng chọn lại chức năng đã có trong menu nha ! ")

main_brain()