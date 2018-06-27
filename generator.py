

def generate():
    numberrow = ''
    sleft =r'{"rows":"'
    sright = r'","person":[],"organization":[],"position":""},'

    with open('./output.txt','w',encoding='utf-8') as wf:
        for i in range(207,324):
            numberrow = str(i)
            wf.write(sleft + numberrow + sright + '\n')




def main():
    generate()

if __name__ == '__main__':
    main()
