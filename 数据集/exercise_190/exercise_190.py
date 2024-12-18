# A program that groups a list into chunks
def chunks(elements, chunk_size):
    result = []
    for i in range(0, len(elements), chunk_size):
        result.append(elements[i:i + chunk_size])
    return result


# Example run
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

parts = chunks(numbers, 4)

print(parts)