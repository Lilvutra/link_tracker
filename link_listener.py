# Listen to link events and update the database accordingly.

import pyperclip, time
from linksdbfunc import init_db, add_link, remove_link

def main():
    init_db()
    last_clipboard = ""
    print("listening to clipboard for job links...")
    
    while True:
        text = pyperclip.paste()
        if text != last_clipboard and text.startwith("http"):
            add_link(text)
            last_clipboard = text
        time.sleep(1)
        
if __name__ == "__main__":
    main()
            

































