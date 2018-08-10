
# Create function to extract and return all urls in a string
def get_urls (page):

    start_pos = 0
    output = []

    while True:

        start_a = page.find('<a', start_pos)            # get position of next link tag
        start_href = page.find('href', start_a)         # get position of href
        start_url_d = page.find('"', start_href)        # get next url that starts with double quote
        start_url_s = page.find("'", start_href)        # get next url that starts with double quote


        # if neither double quote nor single quote are found
        if start_url_d == -1 and start_url_s == -1:
            break

        # if single quote IS found and double quote is not found or is found after single quote
        elif start_url_s != -1 and (start_url_d == -1 or start_url_d > start_url_s):
            start_url = start_url_s                     # use single quote mark
            end_url = page.find("'", start_url + 1)         # find end of url

        # if double quote IS found and single quote is not found or is found after double quote
        elif start_url_d != -1 and (start_url_s == -1 or start_url_s > start_url_d):
            start_url = start_url_d                     # use double quote
            end_url = page.find('"', start_url + 1)         # find end of url


        url = page[start_url + 1 : end_url]             # get the url
        output.append(url)                              # append the url to the output array
        start_pos = end_url                             # set the starting point for the next iteration of the loop

    return output

# the following 5 lines copied from https://stackoverflow.com/questions/24153519/how-to-read-html-from-a-url-in-python-3
import urllib.request
fp = urllib.request.urlopen("https://en.wikipedia.org/wiki/Software_engineering")
seedpage_bytes = fp.read()
seedpage_string = seedpage_bytes.decode("utf8")
fp.close()

urls = get_urls(seedpage_string)

# print urls in an easy to read way
i = 0
while i < len(urls):
    print (urls[i])
    i = i + 1
