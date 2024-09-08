def main():
    statues = int(input())
    printers = 1
    days = 0

    while printers < statues:
        printers += printers
        days += 1

    print(days+1)

if __name__ == '__main__':
    main()

