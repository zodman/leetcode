import sys


def p(arr, left, right):
    width = 4  # Increased width for 3-digit support

    # 1. Print the indices
    indices = "".join(str(i).center(width) for i in range(len(arr)))
    print(f"Index:   {indices}", file=sys.stderr)

    # 2. Print the array values
    # Fix: We add the brackets outside the joined string to keep alignment perfect
    values = "".join(str(val).center(width) for val in arr)
    print(f"Array:  [{values}]", file=sys.stderr)

    # 3. Create the pointer line
    pointer_line = []
    for i in range(len(arr)):
        if i == left == right:
            label = "L&R"
        elif i == left:
            label = "L"
        elif i == right:
            label = "R"
        else:
            label = ""

        pointer_line.append(label.center(width))

    print(f"Pointer: {''.join(pointer_line)}", file=sys.stderr)
    print("-" * (len(arr) * width + 10), file=sys.stderr)


if __name__ == "__main__":
    # Example with 3-digit numbers
    nums = [100, 250, 300, 450, 500, 999]

    p([20, 20, 20, 20, 20, 20], 0, 5)
    p(nums, 0, 5)
    p([1, 2, 3], 2, 2)
