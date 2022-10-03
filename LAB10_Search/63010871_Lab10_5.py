def min_box(lst, number_of_boxes):
    left = max(lst)
    right = sum(lst)
    while left <= right:
        box_size = (left+right)//2 ## MIDDLE
        box_count = 0
        i = 0
        while i < len(lst):
            weight = 0
            while i < len(lst) and weight + lst[i] <= box_size: #add item to box
                weight += lst[i]
                i += 1
            box_count += 1  # increase number of boxes

        if box_count <= number_of_boxes: right = box_size - 1  # a lot of items in box
        else: left = box_size + 1

    return left


if __name__ == '__main__':
    lst, boxes = input("Enter Input : ").split('/')
    boxes = int(boxes)
    lst = list(map(int, lst.split()))
    print(f"Minimum weigth for {boxes} box(es) = {min_box(lst, boxes)}")