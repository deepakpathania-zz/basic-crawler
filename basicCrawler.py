## basic web crawler in python made to extract all the links from the seed page to related pages.
##not complete yet, just testing the waters.


def union(p,q):
    for item in p:
        if item not in q:
            p.append(item)

            
def get_page(url):  ##returns the content of the page whose url is passed in
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def getNextPos(page): ## gets the url and indicates the position for initiating next search
    start_link=page.find("a href")
    if start_link != -1 :
        start_quote=page.find('"',start_link)
        end_quote=page.find('"',start_quote+1)
        url=page[start_quote+1:end_quote]
        return url,end_quote
    else :
        return None,0
def getAllLinks(page): ##extracts the links and stores in a list
    links=[]
    while True:
          url,endpos= getNextPos(page)
          if url :
                 links.append(url)
                 page=page[endpos:]
          else :
                 break
    return links


   
def crawl_web(seed): ##crawls the links present in tocrawl and adds to crawled after crawling
    tocrawl=[seed]
    crawled=[]
    while tocrawl:
        p = tocrawl.pop()
     
        if p not in crawled:
            crawled.append(p)
            tocrawl.append(getAllLinks(get_page(p)))
            
    return crawled

result = crawl_web("https://www.udacity.com/cs101x/index.html")  ##sample test case

for temp in result:  ##printing the links found
    print temp
