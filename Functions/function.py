# equation: y = mx + b
# equation: y = 5x + 3
# shaan said: when x = 5, y = 28

def equation(x):
    y = 5 * x + 3

    return y


for i in range(1, 101):
    mrs_long_wants = i
    shaans_answer = equation(mrs_long_wants)
    print(f"Mrs. Long wants: {mrs_long_wants}")
    print(f"Shaan's answer: {shaans_answer}\n")
