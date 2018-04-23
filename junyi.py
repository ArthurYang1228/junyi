

# Q1

def reverse_word(word):

    return word[::-1]


def reverse_sentence(sentence):


    re_sentence = ''
    for word in sentence.split(" "):
        re_sentence += reverse_word(word)+' '
    return re_sentence

#Q2
def find_num(num):
    stm = []
    for n in range(num):
        n +=1
        if (n%3==0 or n%5==0) and not n%15==0:

            pass
        else:
            stm.append(n)

    return len(stm)

#Q3
'''
查看名為混和的袋子，因為標籤一定是錯誤的，故可以推論出標籤為混和袋子內只有一支筆，
而當我們確認是哪種筆時，此時在另一個標籤為另一種筆的袋中就能確認是混和的筆，也可
進一步推論出第三個袋子中的筆是沒出現過的筆，例如當我們自標為混和的袋中拿出原子筆，
那麼標為鉛筆的袋子中不可能是鉛筆(與標示相符)，也不可能是原子筆(已出現了)，因此可以推論出
裡面是混和的筆，而此時也就確認標為原子筆中裝的是鉛筆，反之亦然

'''

#Q4
'''
在這個問題中的概念被錯誤的抽換，因為270*3指的是三人總共所付出的金錢，然而服務生私吞的60元卻不是指
三人實際付出的錢，因此把兩者相加後得到的數字870是沒有意義的
'''




