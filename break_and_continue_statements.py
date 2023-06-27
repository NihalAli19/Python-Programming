for i in range(12):
    if (i == 5):
        continue        # leave the iteration, jumps to the next iteration
    elif (i == 8):
        break           # leave the loop, breaking out of the loop
    else:
        print("5 x",i,"=", (5 * i))