
# Create function to extract and return all urls contained in a list of webpages
# Pass in an array of urls in the following format:

# [['Name', 'url'], ['Name', 'url']]

def get_urls (origin):

    output = []

    i = 0
    while i < len(origin):

        # extract basic url
        first_dot = origin[i][1].find('.') # find the first dot
        slash = origin[i][1].find('/', first_dot) # find the first / after the first dot (end of base url)
        base_url = origin[i][1][: slash]

        # extract html document as string

        # the following 5 lines copied from https://stackoverflow.com/questions/24153519/how-to-read-html-from-a-url-in-python-3
        import urllib.request
        fp = urllib.request.urlopen(origin[i][1])
        page_bytes = fp.read()
        page_string = page_bytes.decode("utf8")
        fp.close()

        # Look for title of this webpage
        head_pos = page_string.find('<head')
        start_title = page_string.find('<title', head_pos)
        end_title = page_string.find('</title>')

        # get the title
        title = page_string[start_title + 7 : end_title]


        # set title to this page
        origin[i][0] = title

        # start looking for urls

        start_pos = 0 # reset start position for the url finding loop



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

            #add url to output
            appendment = ['Title', url]
            output.append(appendment)

        i = i + 1

    myreturn = [origin, output]
    return myreturn



results = get_urls([["Title", "https://en.wikipedia.org/wiki/Software_engineering"], ["Title", "https://en.wikipedia.org/wiki/Software_development_process"]])
new_urls = results[1]
titles = results[0]

print('CURRENT DATA')
print('')
print('Websites passed into function (have titles added now')
j = 0
while j < len(titles):
    print(titles[j])
    j = j + 1

print ('')
print ('New URLs found (no titles yet)')
k = 0
while k < len(new_urls):
    print(new_urls[k])
    k = k + 1




