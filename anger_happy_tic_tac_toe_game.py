import random   # Importing the random module for generating random positions


score = 0   # Keeps track of total score
print("HAPPY AND ANGRY FACE TIC-TAC-TOE GAME")
boss_boxes = ["🎁"] * 9   # Initialize the board with 9 gift box symbols 🎁


# Print the initial board in a 3x3 format
for index, boss_box in enumerate(range(0, len(boss_boxes),3)):
    print('|'.join(boss_boxes[boss_box:boss_box+3]))


# Main game loop (runs until players quit)
while True:
    print()
    user1 = input("Player1 enter 'X'.['q' to quit.]: ").capitalize()
    print()

    # If Player1 chooses X, randomly place 😁 on the board
    if user1 == 'X':
        randomly = random.randint(0, 8)   # Pick random index
        boss_boxes[randomly] = "😁"       # Place Happy Face
        # Print the updated board
        for index, boss_box in enumerate(range(0, len(boss_boxes), 3)):
            print('|'.join(boss_boxes[boss_box:boss_box + 3]))

    # If Player1 wants to quit
    elif user1 == 'Q':
        exit_query = input("Are you sure you want to quit? Enter either 'yes' or 'no': ").lower()
        if exit_query == 'yes':
            print("\nAww BYE! Let's play again later, okay👋.\n")
            break   # Exit game
        else:
            print("\nWow COOL! Let's play then🤗.\n")
            continue   # Continue game loop

    # Invalid input handling
    else:
        if user1 != 'X' or 'Q':
            print("Incorrect value. Enter 'X' or 'Y'")

    print()
    user2 = input("Player2 enter 'Y'.['q' to quit.]: ").capitalize()
    print()

    # If Player2 chooses Y, randomly place 😡 on the board
    if user2 == 'Y':
        randomly = random.randint(0, 8)   # Pick random index
        boss_boxes[randomly] = "😡"       # Place Angry Face
        # Print the updated board
        for index, boss_box in enumerate(range(0, len(boss_boxes), 3)):
            print('|'.join(boss_boxes[boss_box:boss_box + 3]))

    # If Player2 wants to quit
    elif user2 == 'Q':
        exit_query = input("Are you sure you want to quit? Enter either 'yes' or 'no': ").lower()
        if exit_query == 'yes':
            print("\nAww BYE! Let's play again later, okay👋.\n")
            break   # Exit game
        else:
            print("\nWow COOL! Let's play then🤗.\n")
            continue   # Continue game loop

    # Invalid input handling
    else:
        if user1 != 'X' or 'Q':
            print("Incorrect value. Enter 'X' or 'Y'")


    # --- Check all winning conditions for Player1 😁 ---
    if ((boss_boxes[0] == "😁" ) and
            (boss_boxes[1] == "😁") and
            (boss_boxes[2] == "😁")):   # Top row
        score += 3
        print("Happy Face X 😁 WINS 🎉!!")
        print(f"The trail is this: ___")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9   # Reset board
        continue

    elif ((boss_boxes[3] == "😁") and
          (boss_boxes[4] == "😁") and
          (boss_boxes[5] == "😁")):   # Middle row
        score += 3
        print("Happy Face X 😁 WINS 🎉!!")
        print(f"The trail is this:  ___'")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[6] == "😁") and
          (boss_boxes[7] == "😁") and
          (boss_boxes[8] == "😁")):   # Bottom row
        score += 3
        print("Happy Face X 😁 WINS 🎉!!")
        print(f"The trail is this:  ___")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[0] == "😁") and
          (boss_boxes[3] == "😁") and
          (boss_boxes[6] == "😁")):   # Left column
        score += 3
        print("Happy Face X 😁 WINS 🎉!!")
        print(f"The trail is this: |")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[1] == "😁") and
          (boss_boxes[4] == "😁") and
          (boss_boxes[7] == "😁")):   # Middle column
        score += 3
        print("Happy Face X 😁 WINS 🎉!!")
        print(f"The trail is this: |")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[2] == "😁") and
          (boss_boxes[5] == "😁") and
          (boss_boxes[8] == "😁")):   # Right column
        score += 3
        print("Happy Face X 😁 WINS 🎉!!")
        print(f"The trail is this: |")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[2] == "😁") and
          (boss_boxes[4] == "😁") and
          (boss_boxes[6] == "😁")):   # Diagonal /
        score += 3
        print("Happy Face X 😁 WINS 🎉!!")
        print(f"The trail is this: /")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[0] == "😁") and
          (boss_boxes[4] == "😁") and
          (boss_boxes[8] == "😁")):   # Diagonal \
        score += 3
        print("Happy Face X 😁 WINS 🎉!!")
        print(f"The trail is this: \\")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue



    # --- Check all winning conditions for Player2 😡 ---
    if ((boss_boxes[0] == "😡") and
            (boss_boxes[1] == "😡") and
            (boss_boxes[2] == "😡")):   # Top row
        score += 3
        print("Angry Face Y 😡 WINS 🎉!!")
        print(f"The trail is  this: ___")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[3] == "😡") and
          (boss_boxes[4] == "😡") and
          (boss_boxes[5] == "😡")):   # Middle row
        score += 3
        print("Angry Face Y 😡 WINS 🎉!!")
        print(f"The trail is this: ___")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[6] == "😡") and
          (boss_boxes[7] == "😡") and
          (boss_boxes[8] == "😡")):   # Bottom row
        score += 3
        print("Angry Face Y 😡 WINS 🎉!!")
        print(f"The trail is this: ___")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[0] == "😡") and
          (boss_boxes[3] == "😡") and
          (boss_boxes[6] == "😡")):   # Left column
        score += 3
        print("Angry Face Y 😡 WINS 🎉!!")
        print(f"The trail is this: |")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[1] == "😡") and
          (boss_boxes[4] == "😡") and
          (boss_boxes[7] == "😡")):   # Middle column
        score += 3
        print("Angry Face Y 😡 WINS 🎉!!")
        print(f"The trail is this: |")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[2] == "😡") and
          (boss_boxes[5] == "😡") and
          (boss_boxes[8] == "😡")):   # Right column
        score += 3
        print("Angry Face Y 😡 WINS 🎉!!")
        print(f"The trail is  this: |")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[2] == "😡") and
          (boss_boxes[4] == "😡") and
          (boss_boxes[6] == "😡")):   # Diagonal /
        score += 3
        print("Angry Face Y 😡 WINS 🎉!!")
        print(f"The trail is this: /")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue

    elif ((boss_boxes[0] == "😡") and
          (boss_boxes[4] == "😡") and
          (boss_boxes[8] == "😡")):   # Diagonal \
        score += 3
        print("Angry Face Y 😡 WINS 🎉!!")
        print(f"The trail is this: \\")
        print(f"Score: {score}")
        boss_boxes = ["🎁"] * 9
        continue
