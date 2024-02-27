def load_bar(percent):
    bar = ['.','.','.','.','.','.','.','.','.','.']

    for sector in range((percent // 10)):
        bar[sector] = '%'

    if percent >= 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{percent}% [" + ''.join(bar) + "]")
        print("Still loading...")


percent = int(input())
load_bar(percent)