

number_of_input = int(input("How many people's names and score do you want to input?"))

dict = {}

for x in range(number_of_input):
    key, *valu = input("write name and score : ").split()
    mark = list(map(float, valu))
    dict[key] = mark


call = (dict[input("Whose average score do you want to see? ")])
avaraje = (call[0] + call[1] + call[2]) / len(call)
print(f"Average score is : {avaraje:.2f}")
