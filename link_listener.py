# Listen to link events and update the database accordingly.

import pyperclip, time
from linksdbfunc import init_db, add_link, remove_link
from page_check import is_job_page

def main():
    init_db()
    last_clipboard = ""
    print("listening to clipboard for job links...")
    
    while True:
        text = pyperclip.paste()
        if text != last_clipboard and text.startwith("http"):
            print("checking new link:", text)
            if is_job_page(text):
                print("✅ Job link detected, adding to database.")
                add_link(text)
            else:
                print("not a job link it seems hmm...")
            last_clipboard = text
        time.sleep(1)
        
if __name__ == "__main__":
    main()
            

































