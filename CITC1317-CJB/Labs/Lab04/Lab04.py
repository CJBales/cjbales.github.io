#C.J. Bales
#CITC1317
#Lab04
#9/18/24
def reverse_words(str):
    words = str.split(' ')
    reversetxt = [word[::-1] for word in words]
    return ' '.join(reversetxt)

def add_weirdness(str1):
    weirdstr = str.maketrans("aeiouAEIOU","ɓɐʍs$&*@#X")
    return str1.translate(weirdstr)

def translate_to_winlim(str1):
    reversestr = reverse_words(str1)
    weirdstr = add_weirdness(reversestr)
    return weirdstr

print(translate_to_winlim("ITS GAME OVER MAN"))
#Alien
print(translate_to_winlim("I see your Schwartz is as big as mine!"))
#SpaceBalls
print(translate_to_winlim("She doesn't look Druish!"))
#SpaceBall
print(translate_to_winlim("Merchandising!"))
#SpaceBalls
print(translate_to_winlim("I want to believe."))
#X-Files
