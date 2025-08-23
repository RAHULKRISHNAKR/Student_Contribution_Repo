# A simple Python script that prints a multiplication table

def multiplication_table(n: int):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

if __name__ == "__main__":
    multiplication_table(5)
