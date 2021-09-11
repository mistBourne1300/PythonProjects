def order_freq(ciphertext):
    charlist, countlist = find_freq(ciphertext)
    ordered_list = []
    while len(charlist)>0:
        max_index = countlist.index(max(countlist))
        ordered_list.append(charlist[max_index])
        del charlist[max_index]
        del countlist[max_index]
    return ordered_list


def find_freq(ciphertext):
    char_list = []
    count_list = []
    for c in ciphertext:
        if c in char_list:
            count_list[char_list.index(c)] += 1
        else:
            char_list.append(c)
            count_list.append(1)
    return char_list, count_list


def decript_cipher(ciphertext):
    ordered_freq_list = order_freq(ciphertext)
    english_letters_list = ['e','t','a','i','n','o','s','h','r','d','l','u','c','m','f','w','y','g','p','b','v','k','q','j','x','z']
    decripted_text = []
    for c in ciphertext:
        decripted_text += english_letters_list[ordered_freq_list.index(c)]
    return decripted_text

get_encription = open("Desktop/Python/Crypto/encripted.txt")

text = get_encription.read()
print(find_freq(text))
print(order_freq(text))
plaintext = decript_cipher(text)
plainstring = ''
for c in plaintext:
    plainstring += c

print(plainstring)
