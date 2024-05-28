from src.utils import *


def main():
    operations_list = get_operations_list(load_json(OPERATION_PATH))
    sorted_operations_list = sort_executed_operations(operations_list)
    for i in range(OPERATIONS_COUNT):
        print(format_output(sorted_operations_list[i]))


if __name__ == "__main__":
    main()
