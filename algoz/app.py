import argparse


def main():
    parser = argparse.ArgumentParser(description="Search for word infile")

    parser.add_argument("-w", "--word", required=True, help="Word to be searched for")

    parser.add_argument(
        "-f", "--file", required=True, help="Path to file that is to be searched"
    )

    parser.add_argument(
        "-sa",
        "--search-algorithm",
        choices=["binary-search", "depth-first-search", "breadth-first-search"],
        required=True,
        help="The algorithm to be used to search the file",
    )

    parser.add_argument(
        "-o",
        "--order",
        choices=["pre-order", "post-order", "level-order"],
        required=True,
        help="The order in which to traverse the tree",
    )

    args = parser.parse_args()

    is_depth_first_search = lambda: args.search_algorithm == 'depth-first-search'
    is_breadth_first_search = lambda: args.search_algorithm == 'breadth-first-search'
    is_binary_search = lambda: args.search_algorithm == 'binary-search'

    if is_depth_first_search():
        depth_first.search(args)
        return 


    if is_breadth_first_search():
        depth_first.search(args)
        return 


    if binary_search():
        depth_first.search(args)
        return 

if __name__== "__main__":
    main()
