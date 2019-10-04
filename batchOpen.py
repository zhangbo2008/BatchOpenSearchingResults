'''
想让搜索一个东西,时候自动把当前页所有找到的都打开.



先搞百度
'''

def main(wenzi,canshu=10):

    import requests


    from urllib import parse
    from urllib import request
    from bs4 import BeautifulSoup
    #引入BS库
    address='http://www.baidu.com/s?wd='
    wenzi= parse.quote(wenzi)
    address+=wenzi
    address+='&rn='
    address+=str(canshu)

    '''
    注意地址要进行中文转码,不然打开的网址是不对的!
    '''



    res = requests.get(address)

    html = res.text

    soup = BeautifulSoup(html,'html.parser') #把网页解析为BeautifulSoup对象

    # print(type(soup)) #查看soup的类型  soup的数据类型是 <class 'bs4.BeautifulSoup'>  soup是一个BeautifulSoup对象。
    #
    # print(soup)
    # 打印soup






    quan=soup.find_all('h3',class_='t')




    all_href=[i.find('a')['href'] for i in quan]
    all_href=[i for i in all_href if i[:4]=='http']
    print(all_href)
    print(len(all_href))

    import webbrowser
    for i in all_href:
        webbrowser.open(i)





'''
第一个是kw,第二个是要返回的结果,如果是10,可以不写.最大可以写50.
'''







import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('url',  help='an integer for the accumulator')
parser.add_argument('num', help='an integer for the accumulator')
args = parser.parse_args()
main(args.url,args.num)








