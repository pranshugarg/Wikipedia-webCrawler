import time
import urllib
from bs4 import BeautifulSoup
import requests
start_url  = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def continue_crawl(search_history, target_url, max_steps=25):
        if search_history[-1] == target_url:
                    print("We've found the target article!")
                            return False
                            elif len(search_history) > max_steps:
                                        print("The search has gone on suspiciously long, aborting search!")
                                                return False
                                                elif search_history[-1] in search_history[:-1]:
                                                            print("We've arrived at an article we've already seen, aborting search!")
                                                                    return False
                                                                    else:
                                                                                return True


                                                                            def find_first_link(url):
                                                                                    # get the HTML from "url", use the requests library
                                                                                        # feed the HTML into Beautiful Soup
                                                                                            # find the first link in the article
                                                                                                # return the first link as a string, or return None if there is no link
                                                                                                    response = requests.get(url)
                                                                                                        html=response.text
                                                                                                            soup = BeautifulSoup(html,"html.parser") 
                                                                                                                content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
                                                                                                                    #Note that we have to use the argument class_ since class is a reserved keyword in Python.
                                                                                                                        #The first line finds the div that contains the article's body. The next line loops over each <p> tag in the div,
                                                                                                                            #if that tag is a child of the div. The documentation tells us that,"If you only want Beautiful Soup to consider 
                                                                                                                                #direct children, you can pass in recursive=False". recursive=False will find the direct(first) children of iterated loop
                                                                                                                                    #(all the direct children paragraphs here).
                                                                                                                                        article_link = None
                                                                                                                                            for element in content_div.find_all("p", recursive=False):  
                                                                                                                                                        if element.find("a", recursive=False):
                                                                                                                                                                       article_link = element.find("a", recursive=False).get('href')
                                                                                                                                                                                  break     
                                                                                                                                                                                  #we have to ensure that our code only finds links to ordinary articles, and not links to footnotes, pronunciation guides, 
                                                                                                                                                                                      #or other strange things.This works because "special links" like footnotes and pronunciation keys 
                                                                                                                                                                                          #all seem to be wrapped in more div tags. Since these special links aren't direct descendants of a paragraph tag, we can 
                                                                                                                                                                                              #skip them using the same technique as before.We use the find method this time rather than find_all because 
                                                                                                                                                                                                  #find returns the first tag it finds rather than a list of matching tags.
                                                                                                                                                                                                      #a.get('href') // href enables to extract articleName without whole article URL.
                                                                                                                                                                                                          if not article_link:
                                                                                                                                                                                                                      return
                                                                                                                                                                                                                      #The links in Wikipedia articles are relative urls(eg:wiki/Templebryan_Stone_Circle)
                                                                                                                                                                                                                          #rather than absolute urls (eg:https://en.wikipedia.org/wiki/Templebryan_Stone_Circle). 
                                                                                                                                                                                                                              #This is how to create an absolute(full) url from a relative url(article_link ,here).
                                                                                                                                                                                                                                  first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
                                                                                                                                                                                                                                      return first_link    
                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                  # download html of last article in article_chain
                                                                                                                                                                                                                                  # find the first link in that html
                                                                                                                                                                                                                                  # add the first link to article_chain
                                                                                                                                                                                                                                  # delay for about two seconds

                                                                                                                                                                                                                                  article_chain = [start_url]

                                                                                                                                                                                                                                  while continue_crawl(article_chain, target_url):
                                                                                                                                                                                                                                          print(article_chain[-1])
                                                                                                                                                                                                                                              first_link = find_first_link(article_chain[-1])
                                                                                                                                                                                                                                                  if not first_link:
                                                                                                                                                                                                                                                              print("We've arrived at an article with no links,abort search!")
                                                                                                                                                                                                                                                                      break 
                                                                                                                                                                                                                                                                      article_chain.append(first_link)
                                                                                                                                                                                                                                                                          time.sleep(2)



