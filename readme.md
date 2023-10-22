# OPBR Bot

![OPBR Bot Logo](bot_logo.png)

OPBR Bot is an automated bot developed to perform various tasks in the one piece mobile game. The bot combines screen mirroring, computer vision, and automation to interact with the game and execute actions based on detected elements.

## Features

- Screen mirroring with scrcpy.
- Real-time object detection with YOLO.
- Automated mouse clicks and actions.
- Keyboard listener for stopping the bot.

## Modules

The project consists of several modules, click on it to see its documentation:

1. [opbr_window_manager.py](./readme_files/opbr_window_manager.md) - Provides functions to capture screenshots of specific windows.

2. [opbr_keyboard_listener.py](./readme_files/opbr_keyboard_listener.md) - Listens for keyboard events to stop the bot.

3. [opbr_scrcpy_manager.py](./readme_files/opbr_scrcpy_manager.md) - Manages the scrcpy screen mirroring process.

4. [opbr_mouseclicks.py](./readme_files/opbr_mouseclicks.md) - Contains the main bot logic for object detection and mouse click automation.

5. [opbr_colour_module.py](./readme_files/opbr_colour_module.md) - Defines color constants for visualization.

6. [main.py](./readme_files/main.md) - The main script that orchestrates the bot's operations.

7. [opbr_mousetrack.py](./readme_files/opbr_mousetrack.md) - Tracks the mouse locs and captures

8. [opbr_model_data_preprocess.py](./readme_files/opbr_model_data_preprocess.md) - Preprocess the dataset

9. [opbr_model_train.ipynb](./readme_files/opbr_model_train.md) - Training and creation of model

## Getting Started

To run the OPBR Bot, you need to set up the required dependencies, configuration, and models. Follow these steps:

1. Clone this repository:

    ```shell
    git clone https://github.com/yourusername/opbr-bot.git
    ```

2. Set up your environment with the necessary dependencies.

3. Configure the environment variables, including the screen ID, file paths, and model path.

4. Start the bot by running `main.py`.

## Usage

- Press the 'M' key to stop the bot at any time.

- Monitor the bot's actions and output in the terminal.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and test them.

4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgments

- This project was made possible by various open-source libraries and tools, including scrcpy and YOLO.

- Special thanks to the community for support and contributions.

---

