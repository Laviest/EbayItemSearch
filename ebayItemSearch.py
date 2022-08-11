from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


print("What item are you searching for?")
item_search = input(">")
print("New, used or any condition?")
item_condition = input(">")
item_condition = item_condition.strip().lower()
page = 1
item_search = item_search.replace(" ", "+")

options = ChromeOptions()
options.add_argument("headless")
PATH = r"C:/Users/Pero/Downloads/chromedriver_win32/chromedriver.exe"
driver = Chrome(executable_path=PATH, options=options)

if item_condition == "anycondition":
    driver.get(f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={item_search}&_sacat=0&_pgn{page}")
elif item_condition == "new":
    driver.get(f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={item_search}&_sacat=0&rt=nc&LH_ItemCondition=3&_pgn{page}")
else:
    driver.get(f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={item_search}&_sacat=0&rt=nc&LH_ItemCondition=4&_pgn{page}")

for page in range(1, 3):
    if item_condition == "anycondition":
        driver.get(f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={item_search}&_sacat=0&_pgn{page}")
    elif item_condition == "new":
        driver.get(f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={item_search}&_sacat=0&rt=nc&LH_ItemCondition=3&_pgn{page}")
    else:
        driver.get(f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={item_search}&_sacat=0&rt=nc&LH_ItemCondition=4&_pgn{page}")
    html = driver.page_source
    soupTwo = BeautifulSoup(html, "lxml")
    ebay_items = soupTwo.find_all("li", {"class": "s-item s-item__pl-on-bottom s-item--watch-at-corner"})

    for item in ebay_items:

        try:
            item_name = item.find("div", class_="s-item__info clearfix").h3.text
            item_price = item.find("div", class_="s-item__detail s-item__detail--primary").span.text
            item_shipping_cost = item.find("span", {"class": "s-item__shipping s-item__logisticsCost"}).text
            item_link = item.find("a", {"class": "s-item__link"})['href']
            secondary_info = item.find("span", {"class": "SECONDARY_INFO"}).text
            from_where = item.find("span", {"class": "s-item__location s-item__itemLocation"}).text

            print(f"{item_name} shipped {from_where}.")
            print(f"{secondary_info} costs {item_price} with shipping price: {item_shipping_cost}")
            print(item_link)
            print("\n")
        except AttributeError:
            continue

