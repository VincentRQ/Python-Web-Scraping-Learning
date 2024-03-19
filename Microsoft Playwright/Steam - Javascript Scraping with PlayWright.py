from utils.extract import extract_full_body_html
from utils.parse import parse_raw_attributes
from config.tools import get_config
from selectolax.parser import HTMLParser




if __name__ == "__main__":
    config = get_config()
    html = extract_full_body_html(from_URL= config.get('url'), wait_for=config.get('container').get('selector'))
    tree = HTMLParser(html)

    # divs = tree.css('div[class*="salepreviewwidgets_StoreSaleWidgetContainer"]') pre-Steam website change
    # divs = tree.css('div[class*="StoreSalePriceWidgetContainer"]')
    divs = tree.css(config.get('container').get('selector'))
    print(len(divs))

    for d in divs:

            attrs = parse_raw_attributes(d, config.get('item'))

            # title = d.css_first('div[class*="StoreSaleWidgetTitle"]').text()
            # title = d.css_first('div[class*="StoreSaleWidgetTitle"]')
            # if title is not None:
            #     title = title.text()
            #     print(title)
            # else:
            #     print("Title not found")
            # thumbnail = d.css_first('img[class*="CapsuleImage"]').attributes.get("src")
            # tags = [a.text() for a in d.css("div[class*='_3OSJsO_BdhSFujrHvCGLqV'] > a")[:5]]
            # release_date = d.css_first('div[class*="WidgetReleaseDateAndPlatformCtn"] > div[class*="StoreSaleWidgetRelease"]').text()
            # reviewed_score = d.css_first('div[class*="ReviewScoreValue"] > div').text()
            # reviewed_by = d.css_first('div[class*="ReviewScoreCount"]').text()
            #
            # sale_price = d.css_first('div[class*="StoreSalePriceBox"]').text()
            # original_price = d.css_first('div[class*="StoreOriginalPrice"]').text()


            # attrs = {
            #     "title": title,
            #     "sale_price": sale_price,
            #     "original_price": original_price,
            #     "reviewed_score": reviewed_score,
            #     "reviewed_by": reviewed_by,
            #     "release_date": release_date,
            #     "tags": tags,
            #     "thumbnail": thumbnail
            # }

            print(attrs)





