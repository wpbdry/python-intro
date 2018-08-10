# Create function to extract and return all urls contained in a list of webpages
# Pass in an array of urls in the following format:

# [['Name', 'url'], ['Name', 'url']]
from urllib.error import HTTPError


def get_urls(origin):
    output = []
    l = len(origin)

    i = 0
    c = 0
    while i < len(origin):
        c = c + 1  # keep track of how many completed

        # Check for and skip PDFs to save time
        last_dot = origin[i][1].rfind('.')
        file_type = origin[i][1][last_dot:]
        if file_type == '.pdf' or file_type == '.PDF':
            print('PDF skipped at page %s ' % origin[i][1])
            origin.pop(i)
            continue

        # extract current directory from url
        first_dot = origin[i][1].find('.')  # find the first dot
        slash = origin[i][1].find('/', first_dot)  # find the first / after the first dot (end of base url)
        base_url = origin[i][1][: slash]

        # extract html document as string

        # the following fp code is adapted from
        # https://stackoverflow.com/questions/24153519/how-to-read-html-from-a-url-in-python-3
        import urllib.request
        try:
            fp = urllib.request.urlopen(origin[i][1])
        except HTTPError:
            print("404 at page %s" % origin[i][1])
            origin.pop(i)
            continue
        except urllib.error.URLError:
            print("Could not reach server at %s" % origin[i][1])
            origin.pop(i)
            continue
        page_bytes = fp.read()
        try:
            page_string = page_bytes.decode("utf8")
        except UnicodeDecodeError:
            print("Could not decode page %s" % origin[i][1])
            origin.pop(i)
            continue
        fp.close()

        # Look for title of this webpage
        head_pos = page_string.find('<head>')
        start_title = page_string.find('<title>', head_pos)
        end_title = page_string.find('</title>')

        # get the title
        title = page_string[start_title + 7: end_title]

        # set title to this page
        origin[i][0] = title

        # start looking for urls

        start_pos = 0  # reset start position for the url finding loop

        while True:

            start_a = page_string.find('<a', start_pos)  # get position of next link tag
            start_href = page_string.find('href', start_a)  # get position of href
            start_url_d = page_string.find('"', start_href)  # get next url that starts with double quote
            start_url_s = page_string.find("'", start_href)  # get next url that starts with double quote

            # if neither double quote nor single quote are found
            if start_url_d == -1 and start_url_s == -1:
                break

            # if single quote IS found and double quote is not found or is found after single quote
            elif start_url_s != -1 and (start_url_d == -1 or start_url_d > start_url_s):
                start_url = start_url_s  # use single quote mark
                end_url = page_string.find("'", start_url + 1)  # find end of url

            # if double quote IS found and single quote is not found or is found after double quote
            elif start_url_d != -1 and (start_url_s == -1 or start_url_s > start_url_d):
                start_url = start_url_d  # use double quote
                end_url = page_string.find('"', start_url + 1)  # find end of url

            url = page_string[start_url + 1: end_url]  # get the url
            start_pos = end_url  # set the starting point for the next iteration of the loop

            # ignore blank links
            if len(url) == 0:
                continue

            # ignore id links
            if url[0] == '#':
                continue

            # check for internal links (add base url to the beginning
            if url[0] == '/':
                url = base_url + url

            # add url to output
            appendment = ['Title', url]
            output.append(appendment)

        print('Completed ' + str(c) + ' of ' + str(l) + ' (' + str(int(c / l * 100)) + '%)')
        i = i + 1

    print('Complete. ' + str(len(origin)) + ' valid links found.')
    return [origin, output]


# operation

# Paste any page or set of pages below to change the seed page(s)
# Format: [['', 'Page URL'], ['', 'Page URL']]
seed = [['', "https://www.python.org/"]]

seed_l = len(seed)

print('')
print('Process 1 of 2: Seed links')

result_1 = get_urls(seed)

print('')
print('Process 2 of 2: All links found in seed pages')

result_2 = get_urls(result_1[1])

print('')
print('All valid links found:')
print("['Title', 'URL']")

j = 0
while j < len(result_1[0]):
    print(result_1[0][j])
    j = j + 1

k = 0
while k < len(result_2[0]):
    print(result_2[0][k])
    k = k + 1

print('')
print('End of list. Program has not been written to find links in pages found in seed pages')
