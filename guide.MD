Press Ctrl+C to copy the link -> link goes to clipboard 
Use pyperclip to peek inside 
check clipboard every second 
if content has changed, and it looks like a link, treat it as an event -> save into database
query saved links

Layers:

1. Clipboard Layer 
- Source of truth for new job links
- Read this using Pyperclip
2. Application Logic Layer 
- Watches clipboard for changes 
- Filter valid links
- Decide when to save something
3. Database Layer 
- Store job links
- Use SQLite(links.db)
- Contain a table(links) with cols: id, link, data_saved
4. User Interaction Layer 
- Simple: just print messages in terminal when a new link is saved.
- Later: could be extended into a CLI menu, a GUI (Tkinter), or even a web app (Flask).