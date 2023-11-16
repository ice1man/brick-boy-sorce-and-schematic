def snake(display, snake_speed=2):
    display_text.clear()
    # Define snake and food positions
    snake_x = 30
    snake_y = 30
    food_x = 60
    food_y = 60

    # Define snake body
    snake_body = [(snake_x, snake_y)]

    # Define game variables
    game_over = False

    # Draw snake and food on display
    display_dot.fill(0)
    display_dot.draw_rectangle(snake_body[0], (10, 10))
    display_dot.draw_rectangle((food_x, food_y), (10, 10))
    display_dot.show()

    # Start game loop
    while not game_over:

        # Check for key presses
        keys = machine.button_read()
        if keys & machine.BUTTON_LEFT:
            snake_x -= snake_speed
        elif keys & machine.BUTTON_RIGHT:
            snake_x += snake_speed
        elif keys & machine.BUTTON_UP:
            snake_y -= snake_speed
        elif keys & machine.BUTTON_DOWN:
            snake_y += snake_speed

        # Check if snake has hit the wall
        if snake_x < 0 or snake_x >= 72:
            game_over = True
        elif snake_y < 0 or snake_y >= 50:
            game_over = True

        # Check if snake has hit itself
        for body_part in snake_body[1:]:
            if snake_x == body_part[0] and snake_y == body_part[1]:
                game_over = True

        # Move snake body
        snake_body.insert(0, (snake_x, snake_y))
        snake_body.pop()

        # Check if snake has eaten the food
        if snake_x == food_x and snake_y == food_y:
            food_x = random.randint(0, 71)
            food_y = random.randint(0, 49)
            snake_body.append((snake_x, snake_y))

        # Draw snake and food on display
        display_dot.fill(0)
        for body_part in snake_body:
            display_dot.draw_rectangle(body_part, (10, 10), color=0xFF0000)
        display_dot.draw_rectangle((food_x, food_y), (10, 10), color=0x00FF00)
        display_dot.show()

        # Wait for a short period of time
        time.sleep(0.1)

