import webbrowser

website = input('search website: ')

if website == 'google':
    search = input('search: ')

    webbrowser.open('https://www.google.com/search?q=' + search)

elif website == 'youtube':
    search = input('search: ')

    webbrowser.open('https://www.youtube.com/results?search_query=' +search)

elif website == 'edge':
    search = input('search: ')

    webbrowser.open('https://www.bing.com/search?pglt=41&q=' +search)
