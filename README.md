# Space Invaders Clone

This is a **Space Invaders**-inspired game developed in Python using the `turtle` graphics module and `pygame` for sound playback.  
The project was created as part of the *"100 Days of Code: The Complete Python Pro Bootcamp"* course and serves as a hands-on exercise to reinforce object-oriented programming concepts and animation handling.

## Features

- Classic arcade-style gameplay with:
  - Moving invaders that drop bombs
  - A player-controlled spacecraft that can move and shoot lasers
  - Barriers for temporary protection
  - Lives system and score tracking
- Pixel-art style using custom `.gif` sprites
- Sound effects using `pygame.mixer`:
  - Laser shots
  - Explosions
  - Win/Lose feedback

## Project Structure

```
.
├── board.py         # Scoreboard and lives display
├── invader.py       # Invaders and enemy bomb logic
├── spacecraft.py    # Player, barriers, and laser logic
├── settings.py      # Game configuration and constants
├── sounds.py        # Sound effect setup
├── main.py          # Main game loop and initialization
├── *.gif            # Sprite images (invader1.gif, invader2.gif, spacecraft.gif)
├── *.wav            # Sound files (shoot.wav, explode.wav, win.wav, lose.wav)
```

## Controls

- Left Arrow: Move spacecraft left  
- Right Arrow: Move spacecraft right  
- Spacebar: Shoot laser

## Requirements

Make sure to have Python 3 and the following packages installed:

```
pip install pygame
```

Additionally, ensure the following files are in the same directory:

- invader1.gif, invader2.gif, spacecraft.gif
- shoot.wav, explode.wav, win.wav, lose.wav

## Notes

- This is an educational project and not intended for production or commercial use.
- Sprites and sounds are used purely for learning purposes and are not distributed with copyright intent.
- If the game does not start or sound fails, check that your system supports `pygame.mixer` and all assets are present.
