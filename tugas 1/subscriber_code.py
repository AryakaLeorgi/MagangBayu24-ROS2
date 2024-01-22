class MathProblemSubscriber:
    @staticmethod
    def solve_problem(problem):
        try:
            result = eval(problem)
            return result
        except Exception as e:
            return f"Error: {e}"

# Contoh penggunaan subscriber
subscriber = MathProblemSubscriber()
hasil = subscriber.solve_problem("593 * 1293 - 20")
print(f"Hasil kalkulasi: {hasil}")

