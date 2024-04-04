def rearrange_animal(head, body, tail):
    return [head, body, tail]

# Taking input
head = input("Enter the head of the animal: ")
body = input("Enter the body of the animal: ")
tail = input("Enter the tail of the animal: ")

# Rearranging the elements
normal_animal = rearrange_animal(head, body, tail)

print("The normal arrangement of the animal is:", normal_animal)
