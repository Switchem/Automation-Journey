import matplotlib.pyplot as plt


def collaztt(number):
    if number % 2 == 0:
        positive = number // 2
        print(positive)
        return positive
    else:
        odd = 3 * number + 1
        print(odd)
        return odd


number = int(input("Enter number: "))

sequence = [number]


while number != 1:
    number = collaztt(number)
    sequence.append(number)

print("Full sequence:", sequence)

plt.plot(sequence)
plt.title("Collatz Sequence")
plt.xlabel("Steps")
plt.ylabel("Value")
plt.show()
