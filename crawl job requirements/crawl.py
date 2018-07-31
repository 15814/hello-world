
# -*- coding: utf-8 -*-




def main():
    import requests

    r = requests.get("http://game.campus.163.com/2018/zhiwei/zaixian/jsl/2018/06/25/29329_760515.html#jobList")

    print(r.status_code)
    print('r.headers: ',r.headers)
    r.encoding = 'utf-8'

    writefilename = 'crawl.html'
    path = './'
    with open(path+writefilename,'w', encoding = 'utf-8') as wf:
        wf.write(r.text)







if __name__ == '__main__':
    main()
