import threading
import time

def func0(list_var):
    for x in list_var:
        print(x)
        time.sleep(0.5)

def func1(list_var):
    for x in list_var:
        print(x)
        time.sleep(1)

if __name__=="__main__":
    #####Thread 미사용#####
    # func0([1,2,3,4,5])
    # func1(["A","B","C","D"])

    #####Thread 사용######
    # thread 선언
    x1 =[1,2,3,4,5]
    x2 =["A","B","C","D"]
    t1 = threading.Thread(target=func0,args=(x1,))
    t2 = threading.Thread(target=func1,args=(x2,))

    # thread 시작
    t1.start()
    t2.start()

    # thread 종료
    t1.join()
    t2.join()