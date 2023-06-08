#Question Three

def dictComp(stop,step):
    square_dict = {f'items-{k}' : [k for k in range(1,(step+1))] for k in range(1,stop)}
    return square_dict

print(dictComp(10,4))
