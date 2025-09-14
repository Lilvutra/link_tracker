#Synchoronous Execution and Asynchoronous Execution

playwright.sync_api: program will wait for each browser action to complete before proceeding to the next line of code

playwright.async_api: operations are non-blocking and require wait

sync_playwright Context Manager 
The primary entry point for using the synchronous API is the sync_playwright context manager. This ensures that Playwright resources are properly managed (e.g., browsers are launched and closed)

-> In our context, we choose sync 
































