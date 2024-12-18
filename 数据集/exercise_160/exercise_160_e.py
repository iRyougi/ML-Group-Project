# An example function that takes any number of keyword arguments
def info(**students):
    print("This year students info:")
    for name, major in students.items():
        print(f"- {name}: {major}")
        print("\n")  # 1


# Example run
info(Alice="Physics", Bob="Maths")

info(
    Alice="Applied Physics",
    Bob="Maths",
    Charlie="Pharmaseutics",
    David="Fluid Mechanics",
)
