import random

class MathProblemPublisher:
    def generate_problem(self):
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        num3 = random.randint(1, 1000)
        operators = ['+', '-', '*', '/', '%']
        opr1 = random.choice(operators)
        opr2 = random.choice(operators)
        
        problem = f"{num1} {opr1} {num2} {opr2} {num3}"
        return problem

# Contoh penggunaan publisher
publisher = MathProblemPublisher()
problem = publisher.generate_problem()
print(f"Contoh permasalahan: {problem}")

