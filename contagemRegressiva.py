import time 


def countDown(t):
    while t:
        mins, secs =divmod(t, 60)
        timer ='{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('tempo completo')

t = input('Tempo que deseja contar ')

countDown(int(t))