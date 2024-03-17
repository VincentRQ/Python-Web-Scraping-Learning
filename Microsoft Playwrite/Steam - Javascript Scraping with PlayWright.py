from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

URL = "https://store.steampowered.com/specials"

if __name__ == "__main__":

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)

        page.wait_for_load_state("networkidle")
        page.evaluate("() => window.scroll(0,document.body.scrollHeight)")
        page.wait_for_load_state('domcontentloaded')
        page.wait_for_selector('div[class*="StoreSalePriceWidgetContainer"]')


        # page.screenshot(path="steam2.png", full_page=True)
        html = page.inner_html("body")
        tree = HTMLParser(html)

        # divs = tree.css('div[class*="salepreviewwidgets_StoreSaleWidgetContainer"]') pre-Steam website change
        divs = tree.css('div[class*="StoreSalePriceWidgetContainer"]')



        print(len(divs))

        for d in divs:
            # title = d.css_first('div[class*="StoreSaleWidgetTitle"]').text()
            # print(title)

            title = d.css_first('div[class*="StoreSaleWidgetTitle"]')
            if title is not None:
                title = title.text()
                print(title)
            else:
                print("Title not found")
            # thumbnail = d.css_first('img[class*="CapsuleImage"]').attributes.get("src")
            tags = [a.text() for a in d.css("div[class*='_3OSJsO_BdhSFujrHvCGLqV'] > a")[:5]]

            attrs = {
                "title": title,
                "tags": tags,
                # "thumbnail": thumbnail
            }

            print(attrs)





