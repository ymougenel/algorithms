def min_tab(tab, i_start):
    mini = tab[i_start]
    i_mini = i_start
    for k in range(i_start + 1, len(tab)):
        if tab[k] < mini:
            mini = tab[k]
            i_mini = k
    return i_mini


def sort(tab):
    for i in range(0, len(tab) - 1):
        i_min = min_tab(tab, i)
        tab[i], tab[i_min] = tab[i_min], tab[i]
    return tab
