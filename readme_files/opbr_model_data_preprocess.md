## Documentation for `opbr_color_module.py`

### Overview

This Python script, named `opbr_color_module.py`, provides a set of classes for processing and managing image and label text data for machine learning and computer vision applications. It includes two classes, `DataProcessor` and `ImageProcessor`, each designed to perform specific data-related tasks.

### `DataProcessor` Class

#### `__init__(self, source_folder, train_folder, test_folder, valid_folder)`

This class is responsible for processing and splitting data into training, testing, and validation sets. It is initialized with the paths to the source data folder and destination folders for training, testing, and validation data.

- **Parameters**:
    - `source_folder` (str): Path to the folder containing the source data.
    - `train_folder` (str): Path to the folder where training data will be copied.
    - `test_folder` (str): Path to the folder where testing data will be copied.
    - `valid_folder` (str): Path to the folder where validation data will be copied.

#### `split_data(self, train_ratio=0.8, test_ratio=0.1, valid_ratio=0.1)`

This method splits the data into training, testing, and validation sets based on the provided ratios and copies the files to their respective folders.

- **Parameters**:
    - `train_ratio` (float, optional): Ratio of data to be allocated for training. Default is 0.8.
    - `test_ratio` (float, optional): Ratio of data to be allocated for testing. Default is 0.1.
    - `valid_ratio` (float, optional): Ratio of data to be allocated for validation. Default is 0.1.

#### `verify_and_cleanup(self)`

This method verifies the integrity of image and label text file pairs and removes any missing or mismatched files. It also provides a report on missing files.

#### `move_files_to_class_folder(self, source_path, dest_path, class_id)`

This method moves image and text files from the source path to the destination path based on a specified class ID.

### `ImageProcessor` Class

#### `__init__(self, folder_path)`

This class is designed for processing images and label text files. It is initialized with the path to the folder containing image and label text files.

- **Parameters**:
    - `folder_path` (str): Path to the folder containing image and label text files.

#### `check_image_resolution(self)`

This method checks the resolution of images and removes those with a width less than 1020 pixels. It also provides a report on the removed files.

#### `create_modify_text_files(self, content)`

This method creates or modifies label text files for images with the provided content. It writes the specified content to the label text files.

- **Parameters**:
    - `content` (str): The content to be written to the label text files.

#### `change_class_id_in_text_files(self, cid)`

This method changes the class ID in label text files to the provided class ID. It modifies the label text files for a specific class.

- **Parameters**:
    - `cid` (str): The new class ID.

### Example Usage

The script includes an example of how to use the `DataProcessor` and `ImageProcessor` classes in a real-world scenario for managing and processing image and label data. The example covers tasks such as data splitting, verification, resolution checking, content modification, and class ID changes.

### Environment Variables

The script uses the `dotenv` library to load environment variables, which can be defined in a `.env` file or using other methods suited to environment.

