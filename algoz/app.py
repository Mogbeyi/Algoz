import argparse


def main():
    parser = argparse.ArgumentParser(description="Search for word in file")

    # word
    parser.add_argument("-w", "--word", required=True, help="Word to be searched for")

    # file
    parser.add_argument(
        "-f", "--file", required=True, help="Path to file that is to be searched"
    )

    # algorithm
    parser.add_argument(
        "-sa",
        "--search-algorithm",
        choices=["binary-search", "depth-first-search", "breadth-first-search"],
        required=True,
        help="Algorithm to be used to search the file",
    )

    parser.add_argument(
        "-o",
        "--order",
        choices=["pre-order", "post-order", "level-order"],
        required=True,
        help="The order in which to traverse the tree",
    )

    args = parser.parse_args()

    if args.search_algorithm == "depth-first-search":
        depth_first.search(args)
        return

    if args.search_algorithm == "breadth-first-search":
        breadth_first.search(args)
        return

    if args.search_algorithm == "binary-search":
        binary.search(args)
        return


if __name__ == "__main__":
    main()
