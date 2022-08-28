#!/usr/bin/env python3

from msilib import sequence


def detect_ranges(L):
    L2 = sorted(L)
    print(L2)
    start_sequence = 0
    end_sequence = 0


    result_list = []
    for i in range(len(L2)-1):
        if L2[i] + 1 == L2[i + 1]:
            end_sequence = i + 1

        else:
            if start_sequence == end_sequence:
                result_list.append(L2[i])
            else:
                result_list.append((L2[start_sequence],L2[end_sequence]+1))


            start_sequence = i+1
            end_sequence = i+1
    if start_sequence != end_sequence:
        result_list.append((L2[start_sequence],L2[end_sequence]+1))
    else:
        result_list.append(L2[end_sequence])
    return result_list

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
