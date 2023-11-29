from src.regulator import Regulator

def main():
    regulator = Regulator()
    command = 'a'
    while command != 'e':
        command = input()
        match command:
            case 'e':
                break
            
            case 'i':
                value = input().strip()
                regulator.insert_use_case(value)

            case 'c':
                value = input()
                regulator.search_use_case(value)

            case 'l':
                value = int(input())
                regulator.list_use_case(value)

            case 'x':
                value = int(input())
                regulator.number_traversal_use_case(value)

            case 'o':
                init = input().strip()
                end = input().strip()
                regulator.alphabetic_traversal_use_case(init, end)

            case 'r':
                value = input()
                regulator.remove_use_case(value)

            case 'p':
                regulator.post_order()

            case _:
                pass


if __name__ == "__main__":
    main()