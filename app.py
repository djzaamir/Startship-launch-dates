import requests
from bs4 import BeautifulSoup 


site_url = "https://everydayastronaut.com/sn9-10-km-flight-live-updates/"


def main():
    print("\n Fetching Starship launch details from Everyday-Astronaut Website...")
    site_text = requests.get(site_url).content
    soup = BeautifulSoup(site_text, "lxml")

    # Getting closer to our area of interest
    roi_td = soup.find("td", "has-text-align-left")
    # After investigating the markup, we can see that the next area is our area of interest
    # and contains the actual updated launch date from everyday astronaut website
    launch_date = roi_td.find_next_sibling()
    
    print(f"\n Current Expected Launch Date ->  {launch_date.em.text}\n")
    

if __name__ == "__main__":
    main()