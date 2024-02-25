max_diff , problems = map(int, input().split())

difficulties = list(map(int, input().split()))


def can_round(list_probs):
    if 0 not in list_probs:
        for i in range(len(list_probs)):
            list_probs[i] -= 1
        return True
    return False

list_probs = [0] * max_diff

return_char = ''
for problem in difficulties:
    list_probs[problem - 1] += 1
    if can_round(list_probs):
        return_char += '1'
    else:
        return_char += '0'

print(return_char)