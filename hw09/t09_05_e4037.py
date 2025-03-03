def merge_sort(main, extra):

    if len(main) > 1:
        mid = len(main) // 2
        lefthalf_m = main[:mid]
        lefthalf_e = extra[:mid]
        righthalf_m = main[mid:]
        righthalf_e = extra[mid:]

        merge_sort(lefthalf_m, lefthalf_e)
        merge_sort(righthalf_m, righthalf_e)

        i, j, k = 0, 0, 0

        while i < len(lefthalf_m) and j < len(righthalf_m):
            if lefthalf_m[i] <= righthalf_m[j]:
                main[k] = lefthalf_m[i]
                extra[k] = lefthalf_e[i]
                i += 1

            else:
                main[k] = righthalf_m[j]
                extra[k] = righthalf_e[j]
                j += 1
            k += 1

        while i < len(lefthalf_m):
            main[k] = lefthalf_m[i]
            extra[k] = lefthalf_e[i]
            i += 1
            k += 1

        while j < len(righthalf_m):
            main[k] = righthalf_m[j]
            extra[k] = righthalf_e[j]
            j += 1
            k += 1

if __name__ == "__main__":
    f = open("input.txt")
    n = int(f.readline())
    main = []; extra = []
    for line in f:
        line = line.split()
        main.append(int(line[0]))
        extra.append(int(line[1]))

    merge_sort(main, extra)
    
    for x in range(n):
        print(main[x], extra[x])

    f.close()

