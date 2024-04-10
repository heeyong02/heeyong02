#개념 확인과제
def rep_char(c, n):
    print(c * n)
def draw_line_string():
    msg1 = f'Hello {name},'
    msg2 = 'Welcome to Seoul.'
    #nstr = max(len(msg1), len(msg2))
    nstr = len(msg1) if(len(msg1)>len(msg2))else len(msg2)

    rep_char('-', nstr + 2)  #영어 한 글자 당 - 1개, 앞뒤공백1칸
    print(f' {msg1} \n {msg2} ')
    rep_char('-', nstr + 2)
name = input('Input his/her name: ')
msg_t = draw_line_string()
