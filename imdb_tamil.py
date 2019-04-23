import bs4
import requests

url='https://www.imdb.com/india/top-rated-tamil-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=600ca544-31f5-4bd8-ae38-ea4014c93bab&pf_rd_r=Q2QV1ZJEB8P02E5VV5BZ&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_india_tr_rhs_3'
page=requests.get(url)

page_soup=bs4.BeautifulSoup(page.text, 'html.parser')

list_container=page_soup.find('tbody', {'class':'lister-list'})
list=list_container.find_all('td', {'class':'titleColumn'})
list2=list_container.find_all('td', {'class':'ratingColumn imdbRating'})

print(list2[1].text)

filename='imdb_top_tamil.csv'
headers="No.,Movie Name,Rating \n"
f=open(filename, 'w')
f.write(headers)

i=0

for movie in list:
    name=movie.text.replace('\n' , '').replace('.' , ',').replace(' ' , '').strip()
    rating=list2[i].text.strip()
    #rating=movie.find('td', {'class':'ratingColumn imdbRating'})
    #img_src=movie.img['src']
    print(name + ',' + rating  )
    f.write(name + ',' + rating + '\n')
    i=i+1

f.close();