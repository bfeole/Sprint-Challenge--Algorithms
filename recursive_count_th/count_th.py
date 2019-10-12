'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    th_string = "th"

    # base case There is an empty string in TEST!
    if (len(word) == 0 or len(word) < len(th_string)):
        return 0
    # if word == "th":
    #     return 1
    # if len(word) < 2:
    #     return 0
    # if not word:
    #     return 0

    # recursive
    if (word[0:len(th_string)] == "th"):
        return 1 + count_th(word[len(th_string) - 1:])

    else:
        return 0 + count_th(word[len(th_string) - 1:])
    # if index == len(word) - 1:
    #     return count
    # if word[index] == 't' and word[index+1] == 'h':
    #     count += 1
        # return 1 + count_th(word[0] + word[1])
    # index += 1
    # else:
    #     return 0 + count_th(word[0] + word[1])
    # return (word[0:1] == "th") + count_th(word[0:1])

    # return count_th(word)
