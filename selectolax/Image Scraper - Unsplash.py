from httpx import get
from selectolax.parser import HTMLParser

def get_img_tags_for(term=None):
    if not term:
        raise Exception("No search term provided")

    url=f"https://unsplash.com/s/photos/{term}"
    resp = get(url)

    if resp.status_code != 200:
        raise Exception("Error getting response")


    tree = HTMLParser(resp.text)
    imgs = tree.css("figure a img + div img")
    return imgs

def img_filter_out(url: str, keywords: list) -> bool:
    return not any(x in url for x in keywords)

# img_filter(src, ['premium', 'profile']) -> true/false

def get_high_reso_img_url(img_node):
    srcset = img_node.attrs["srcset"]
    srcset_list = srcset.split(",")

    url_res = [src.split(" ") for src in srcset_list if img_filter_out(src, ['plus', 'profile', 'premium' ])]

    if not url_res:
        return None

    return url_res[0][0].split("?")[0]






if __name__ == '__main__':
    img_nodes = get_img_tags_for('galaxy')
    all_img_urls = [get_high_reso_img_url(i) for i in img_nodes]
    img_urls = [u for u in all_img_urls if u]

    print(img_urls)
    # [print(get_high_reso_img_url(i)) for i in img_nodes[:4]]

    # img_urls = [i.attrs["src"] for i in img_nodes]
    # relevant_urls = [i for i in img_urls if img_filter_out(i, ['plus','oremium','profile'])]
    #
    # for u in relevant_urls:
    #     print(u)
    #
    #
    # print (len(img_nodes))
    # print(img_nodes)
    #






