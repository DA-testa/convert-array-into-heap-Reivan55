def build_heap(data):
    swaps = []

    def sift_down(i):
        min_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < len(data) and data[left_child] < data[min_index]:
            min_index = left_child

        if right_child < len(data) and data[right_child] < data[min_index]:
            min_index = right_child

        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(min_index)

    for i in range(len(data) // 2, -1, -1):
        sift_down(i)

    return swaps


def main():
    
    first_input = input().strip()

    
    if first_input == 'I':
        n = int(input())
        data = list(map(int, input().split()))
    
    elif first_input == 'F':
        n = int(input())
        data = list(map(int, input().split()))
    
    else:
        n = int(first_input)
        data = list(map(int, input().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()






