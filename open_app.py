import assistant_speaks as ass
import os

def open_application(input): 
  
    if "chrome" in input: 
        ass.assistant_speaks("Google Chrome") 
        os.system(r'/usr/bin/google-chrome')
        return
  
    elif "firefox" in input or "mozilla" in input: 
        ass.assistant_speaks("Opening Mozilla Firefox") 
        os.system(r'/usr/bin/firefox')
        return
  
    elif "code" in input: 
        ass.assistant_speaks("Opening Microsoft visual Code") 
        os.system(r'C:\Users\ashut\AppData\Local\Programs\Microsoft VS Code\Code.exe')
        return
  
    elif "hatch" in input: 
        ass.assistant_speaks("Opening Hatch File") 
        os.system(r'H:')
        return
  
    else: 
  
        ass.assistant_speaks("Application not available") 
        return
