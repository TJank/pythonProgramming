
import urllib.request
import io

u = urllib.request.urlopen("https://www.amazon.com/gp/registry/wishlist/381TS2Z7KI7LE/ref=nav_wishlist_lists_1", data=None)
f = io.TextIOWrapper(u, encoding='utf-8')

text = f.read()

