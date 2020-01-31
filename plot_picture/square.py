# 練習raise的技巧
def plot_square(symb, width, height):
    if len(symb) != 1:
        raise Exception('without symbolic')
    if width <= 2:
        raise Exception('width must >= 2')
    if height <= 2:
        raise Exception('height must >= 2')

    # plot
    print(symb * width)
    for _ in range(height - 2):
        print(symb + ' '*(width-2) + symb)
    print(symb * width)

if __name__ == '__main__':
    for s, w, h in (('*', 5, 5), ('z', 2, 2), ('a', 10, 13)):
        try:
            plot_square(s, w, h)
        except Exception as err:
            print('Exception: '+ str(err))