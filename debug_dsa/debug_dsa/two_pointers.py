def p(arr, left, right):
    # 1. Print the indices
    indices = " ".join(f"{i:3}" for i in range(len(arr)))
    print(f"Index:   {indices}")

    # 2. Print the array values
    values = " ".join(f"{val:3}" for val in arr)
    print(f"Array:  [{values}]")

    # 3. Create the pointer line
    pointer_line = ["   "] * len(arr)
    if left == right:
        pointer_line[left] = "L&R"
    else:
        pointer_line[left] = " L "
        pointer_line[right] = " R "

    print(f"Pointer:  {' '.join(pointer_line)}")
    print("-" * (len(arr) * 4 + 10))


if __name__ == "__main__":
    # Example usage:
    nums = [10, 20, 30, 40, 50, 60]
    L, R = 1, 4

    print(nums, L, R)
