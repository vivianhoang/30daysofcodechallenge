"""Roy wanted to increase his typing speed for programming contests.
So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog"
repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter
of the alphabet at least once.)

After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.
Given a sentence s, tell Roy if it is a pangram or not."""

sentence = raw_input().replace(" ", "")

def isPanagram(str):
    alpha = []

    for letter in str:
        letter = letter.lower()
        if letter not in alpha:
            alpha.append(letter)

    sort_alpha = sorted(alpha)
    final_alpha = "".join(sort_alpha)

    if final_alpha == "abcdefghijklmnopqrstuvwxyz":
        return "pangram"
    else:
        return "not pangram"

print isPanagram(sentence)