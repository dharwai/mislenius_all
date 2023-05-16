import time
import webbrowser
with open("updated.txt") as f:
    for url in f:
        webbrowser.register('opera', None, webbrowser.BackgroundBrowser("C:/Users/Rajesh Kumar/AppData/Local/Programs/Opera/opera.exe"))
        webbrowser.get("opera").open_new_tab(url)
        time.sleep(6)
        