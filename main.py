def main():
    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    N = int(input('Enter the number of sequences: '))
    result.append(a1)
    result.append(a2)
    """
    ########################################
    Code Your Program here
    ########################################
    """
    i = 0
    while i < N:
        a3 = a1 + a2
        result.append(a3)
        a1 = a2
        a2 = a3
        i = i + 1

    ########################################
    # Do not delete the return statement
    ########################################
    return result



if __name__ == '__main__':
    main()
