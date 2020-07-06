from requests_html import HTMLSession

session = HTMLSession()
url = 'https://sigob.aeronautica.gob.pa/snra/subtipo/2'

r = session.get(url)
r.html.render(sleep=0, keep_page=True, scrolldown=1)
