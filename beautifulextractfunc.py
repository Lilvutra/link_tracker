#Extract header
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright 


def get_page_title(url: str) -> str:
    
    tits = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            #extract page content 
            page.goto(url, timeout=8000) 
            html = page.content()
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string if soup.title else "No Title Found"
            tits.append(title.strip())
        except Exception as e:
            print("Could not fetch title:", e)
            return "Error fetching title" 
        
        try:
            headlines = soup.find_all(['h1', 'h2', 'h3'])
            for headline in headlines:
                print(f"headline found: {headline.string.strip()}")
                if headline.string:
                    tits.append(headline.string.strip())
                    print(f"tits: {tits}")        
            return "No headline found"
        except Exception as e:
            print("Could not extract headline:", e)
            return "Error extracting headline"
        
        try:
            meta_tag = soup.find('meta', attrs={'name': 'title'})
            if meta_tag and 'content' in meta_tag.attrs:
                tits.append(meta_tag['content'].strip())
            return "No meta title found"
        except Exception as e:
            print("Could not extract meta title:", e)
            return "Error extracting meta title"
        
        finally:
            browser.close()
            
    # how many tits we have 
    tits = list(set([t for t in tits if t]))
    print("Titles found:", tits)
    return tits if tits else ["No title found"]








































