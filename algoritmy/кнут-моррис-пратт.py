def pi_function(s:str):
    """Пи-функция для строки. На выходе получаем список i-ый элемент которого показывает длину максимального
       собственного(не равного самой строке) суффикса равного преффиксу для строки s[:i]
    """
    pi_s = [0 for i in range(len(s)+1)]
    for i in range(2, len(s)+1):
        curr_pi = pi_s[i-1]
        while curr_pi > 0 and s[i-1] != s[curr_pi]:
            curr_pi = pi_s[curr_pi]
        if s[i-1] == s[curr_pi]:
            curr_pi += 1
        pi_s[i] = curr_pi
    return pi_s

def kn_mor_pr(s:str, sub:str):
    """Алгоритм Кнута-Морриса-Пратта. Выводит индексы всех вхождений подстроки sub в строку s, если их нет"""
    pi_s = pi_function(sub + '#' + s)
    return [i-(2*len(sub)+1) for i in range(len(pi_s)) if pi_s[i] == len(sub)]

