import agentql
from playwright.sync_api import sync_playwright
import time

# Set the URL to the desired website
URL = "https://www.bosch-home.com/us/owner-support/get-support/owner-manuals"

def main():
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:
        page = agentql.wrap(browser.new_page())

        # Navigate to the URL
        page.goto(URL)
        page.wait_for_load_state("networkidle")

        try:
            # Handle Cookie Popup if present
            cookie_button = page.get_by_prompt("the accept all button")
            
            cookie_button.first.click()
            page.wait_for_timeout(1000)  # Wait for 1 second

            # Fill search bar
            search_bar = page.get_by_prompt("the search bar")
            if search_bar:
                search_bar.fill("SHX5AEM4N/01")
                page.wait_for_timeout(1000)  # Wait for 1 second
                
                # Click search button
                search_button = page.get_by_prompt("the next button")
                if search_button:
                    search_button.click()
                    page.wait_for_load_state("networkidle")
                    page.wait_for_timeout(2000)  # Wait for 2 seconds
                    
                    # Click next button
                    next_button = page.get_by_prompt("the next button")
                    if next_button:
                        results_page = next_button.click()
                        page.wait_for_load_state("networkidle")
                        page.wait_for_timeout(2000)  # Wait for new page to load
                        
                        # Create new wrapped page for the results page
                        results_page = agentql.wrap(page)
                        
                        # Click installation instruction button on new page
                        install_button = results_page.get_by_prompt("the installation instruction button")
                        if install_button:
                            install_button.click()
                            results_page.wait_for_load_state("networkidle")

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            
        # Used only for demo purposes
        page.wait_for_timeout(20000)

if __name__ == "__main__":
    main()
