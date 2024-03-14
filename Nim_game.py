def nim_game():
    heap_size = 50  # Number of matchsticks in the heap
    current_player = "Max"

    while heap_size > 0:
        print(f"\nCurrent heap size: {heap_size}")
        if current_player == "Max":
            move = max_heap_move(heap_size)
        else:
            move = min_heap_move(heap_size)

        print(f"{current_player} takes {move} matchsticks.")
        heap_size -= move

        # Switch players
        current_player = "Min" if current_player == "Max" else "Max"

    print(f"\n{current_player} wins!")

def max_heap_move(heap_size):
    # Max always wins by leaving a heap size that is a multiple of 4
    if heap_size % 4 == 0:
        return 3
    else:
        return heap_size % 4

def min_heap_move(heap_size):
    # Min's move is not relevant in this example as Max always wins
    # You can customize Min's strategy if needed
    return 1

if __name__ == "__main__":
    nim_game()
