import random
def nim_game():
    heap_size = 29  # Number of matchsticks in the heap
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
    a=int(heap_size/2)
    b=heap_size-a

    return b
  
def min_heap_move(heap_size):
    a= random.randint(1,heap_size)
    return a

if __name__ == "__main__":
    nim_game()
