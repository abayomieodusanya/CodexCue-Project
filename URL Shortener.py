import pyshorteners

def shorten_url(long_url):
    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(long_url)
        return short_url
    except Exception as e:
        print("An error occurred:", e)
        return None

long_url = input("Enter the URL you want to shorten: ")

short_url = shorten_url(long_url)
if short_url:
    print("Shortened URL:", short_url)
else:
    print("Failed to shorten the URL.")
