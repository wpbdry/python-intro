
# Create function to extract and return all urls contained in a webpage (pass in a url as string)
def get_urls (origin):

    # extract basic url
    first_dot = origin.find('.') # find the first dot
    slash = origin.find('/', first_dot) # find the first / after the first dot (end of base url)
    base_url = origin[: slash]
    print (base_url)

    # extract html document as string

    # the following 5 lines copied from https://stackoverflow.com/questions/24153519/how-to-read-html-from-a-url-in-python-3
    import urllib.request
    fp = urllib.request.urlopen(origin)
    page_bytes = fp.read()
    page_string = page_bytes.decode("utf8")
    fp.close()

    # start looking for urls

    start_pos = 0
    output = []

    while True:

        start_a = page_string.find('<a', start_pos)             # get position of next link tag
        start_href = page_string.find('href', start_a)          # get position of href
        start_url_d = page_string.find('"', start_href)         # get next url that starts with double quote
        start_url_s = page_string.find("'", start_href)         # get next url that starts with double quote


        # if neither double quote nor single quote are found
        if start_url_d == -1 and start_url_s == -1:
            break

        # if single quote IS found and double quote is not found or is found after single quote
        elif start_url_s != -1 and (start_url_d == -1 or start_url_d > start_url_s):
            start_url = start_url_s                     # use single quote mark
            end_url = page_string.find("'", start_url + 1)         # find end of url

        # if double quote IS found and single quote is not found or is found after double quote
        elif start_url_d != -1 and (start_url_s == -1 or start_url_s > start_url_d):
            start_url = start_url_d                     # use double quote
            end_url = page_string.find('"', start_url + 1)         # find end of url


        url = page_string[start_url + 1 : end_url]             # get the url
        start_pos = end_url                                     # set the starting point for the next iteration of the loop

        # ignore id links
        if url[0] == '#':
            continue

        #check for internal links (add base url to the beginning
        if url[0] == '/':
            url = base_url + url
            output.append(url)

        #add url to output
        output.append(url)

    return output



urls = get_urls("https://en.wikipedia.org/wiki/Software_engineering")

# print urls in an easy to read way
i = 0
while i < len(urls):
    print (urls[i])
    i = i + 1
