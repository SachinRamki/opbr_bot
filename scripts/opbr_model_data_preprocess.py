import os
import random
import shutil
from PIL import Image
from dotenv import load_dotenv
import os

class DataProcessor:
    """
    A class for processing and splitting data into training, testing, and validation sets.
    """

    def __init__(self, source_folder, train_folder, test_folder, valid_folder):
        """
        Initializes the DataProcessor.

        Args:
            source_folder (str): Path to the folder containing the source data.
            train_folder (str): Path to the folder where training data will be copied.
            test_folder (str): Path to the folder where testing data will be copied.
            valid_folder (str): Path to the folder where validation data will be copied.
        """
        self.source_folder = source_folder
        self.train_folder = train_folder
        self.test_folder = test_folder
        self.valid_folder = valid_folder

    def split_data(self, train_ratio=0.8, test_ratio=0.1, valid_ratio=0.1):
        """
        Splits the data into training, testing, and validation sets and copies the files to their respective folders.

        Args:
            train_ratio (float, optional): Ratio of data to be allocated for training. Default is 0.8.
            test_ratio (float, optional): Ratio of data to be allocated for testing. Default is 0.1.
            valid_ratio (float, optional): Ratio of data to be allocated for validation. Default is 0.1.
        """
        # Create destination folders if they don't exist
        os.makedirs(self.train_folder, exist_ok=True)
        os.makedirs(self.test_folder, exist_ok=True)
        os.makedirs(self.valid_folder, exist_ok=True)

        # List all files in the data folder (assuming each image has a corresponding label text file)
        all_image_files = [file for file in os.listdir(self.source_folder) if file.endswith('.jpeg') or file.endswith('.png')]
        random.shuffle(all_image_files)

        # Calculate the number of files for each split
        total_files = len(all_image_files)
        train_split = int(total_files * train_ratio)
        test_split = int(total_files * test_ratio)
        valid_split = int(total_files * valid_ratio)

        # Split the files into train, test, and validation sets
        train_files = all_image_files[:train_split]
        test_files = all_image_files[train_split:train_split + test_split]
        valid_files = all_image_files[train_split + test_split:]

        # Copy image files and their corresponding label text files to their respective folders
        self._copy_files(train_files, self.train_folder)
        self._copy_files(test_files, self.test_folder)
        self._copy_files(valid_files, self.valid_folder)

        print("Data split complete.")

    def _copy_files(self, file_list, destination_folder):
        """
        Copies a list of files to a destination folder.

        Args:
            file_list (list): List of file names to be copied.
            destination_folder (str): Path to the destination folder.
        """
        for file in file_list:
            image_path = os.path.join(self.source_folder, file)
            label_path = os.path.join(self.source_folder, file.replace('.jpeg', '.txt'))
            destination_image_path = os.path.join(destination_folder, file)
            destination_label_path = os.path.join(destination_folder, file.replace('.jpeg', '.txt'))
            shutil.copy(image_path, destination_image_path)
            shutil.copy(label_path, destination_label_path)

    def verify_and_cleanup(self):
        """
        Verifies the integrity of image and label text file pairs and removes any missing or mismatched files.
        """
        # List all files in the folder
        all_files = os.listdir(self.source_folder)

        # Initialize sets to store the names of .jpeg and .txt files without extensions
        jpeg_names = set()
        txt_names = set()

        # Iterate through the files and separate them into sets based on their extensions
        for file in all_files:
            if file.endswith('.jpeg') or file.endswith('.jpg'):
                base_name = os.path.splitext(file)[0]
                jpeg_names.add(base_name)
            elif file.endswith('.txt'):
                base_name = os.path.splitext(file)[0]
                txt_names.add(base_name)

        missing_jpeg_for_txt = txt_names - jpeg_names
        missing_txt_for_jpeg = jpeg_names - txt_names

        if missing_jpeg_for_txt:
            print("Missing .jpeg files for the following .txt files:")
            for missing_txt in missing_jpeg_for_txt:
                print(f"{missing_txt}.txt")

        if missing_txt_for_jpeg:
            print("Missing .txt files for the following .jpeg files:")
            for missing_jpeg in missing_txt_for_jpeg:
                print(f"{missing_jpeg}.jpeg")

        for missing_file in missing_jpeg_for_txt | missing_txt_for_jpeg:
            missing_jpeg = f"{missing_file}.jpeg"
            missing_txt = f"{missing_file}.txt"

            missing_jpeg_path = os.path.join(self.source_folder, missing_jpeg)
            missing_txt_path = os.path.join(self.source_folder, missing_txt)

            if os.path.exists(missing_jpeg_path):
                os.remove(missing_jpeg_path)
                print(f"Deleted missing .jpeg file: {missing_jpeg}")

            if os.path.exists(missing_txt_path):
                os.remove(missing_txt_path)
                print(f"Deleted missing .txt file: {missing_txt}")

        print("Verification and cleanup complete.")

    def move_files_to_class_folder(self, source_path, dest_path, class_id):
        """
        Move image and text files from source_path to dest_path based on class_id.

        Args:
            source_path (str): Path to the source folder containing image and label text files.
            dest_path (str): Path to the destination folder where files should be moved.
            class_id (int): The class ID to filter files by.

        Returns:
            None
        """
        class_names = ['start_page', 'ok', 'finish', 'next', 'accept', 'battle', 'battle_start', 'change_party',
                       'claim', 'close', 'edit_party', 'event', 'finger_down', 'free', 'home', 'league_battle',
                       'loading', 'login', 'player_name', 'skip', 'tutorial', 'char_upg', 'punch', 'combat',
                       'commend', 'battle_loading', 'password', 'profile', 'share_contact', 'scout', 'video_close',
                       'already_claimed', 'dodge', 'skill_2', 'skill_1', 'homescreen', 'hero_details', 'item_chance',
                       'continue_play', 'menu', 'exchange', 'connection_error']

        all_files = os.listdir(source_path)
        text_files = [files for files in all_files if files.endswith('.txt')]

        data_list = []

        for text_file in text_files:
            text_file_path = os.path.join(source_path, text_file)
            with open(text_file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    data_dict = {}
                    data_dict['file_name'] = text_file_path.split('/')[-1]
                    data_dict['object_count'] = int(round(len(parts) / 5, 0))
                    data_dict['class_index'] = int(parts[0])
                    data_dict['class_name'] = class_names[int(parts[0])]
                    data_dict['x'], data_dict['y'], data_dict['w'], data_dict['h'] = map(float, parts[1:5])
                    data_list.append(data_dict)

        df = pd.DataFrame(data_list)
        df.sort_values(by='class_index', ascending=True, inplace=True)

        filtered_df = df[df['class_index'] == class_id]

        column_list = []

        for value in filtered_df['file_name']:
            column_list.append(value)

        for file in column_list:
            image_file_name = file.split('.txt')[0] + ".jpeg"
            text_file_name = file
            image_path = os.path.join(source_path, image_file_name)
            text_path = os.path.join(source_path, text_file_name)
            shutil.move(image_path, dest_path)
            shutil.move(text_path, dest_path)

        new_all_files = os.listdir(source_path)

        print(f"Old file count {len(all_files)}, New file count {len(new_all_files)}")



class ImageProcessor:
    """
    A class for processing images and label text files.
    """

    def __init__(self, folder_path):
        """
        Initializes the ImageProcessor.

        Args:
            folder_path (str): Path to the folder containing image and label text files.
        """
        self.folder_path = folder_path

    def check_image_resolution(self):
        """
        Checks the resolution of images and removes those with a width less than 1020 pixels.
        """
        # Create a list of dictionaries containing filenames and resolutions
        image_files = [file for file in os.listdir(self.folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        image_info_list = []

        for image_file_name in image_files:
            image_file_path = os.path.join(self.folder_path, image_file_name)
            text_file_path = image_file_path.split(".jpeg")[0] + ".txt"

            if os.path.isfile(image_file_path):
                with Image.open(image_file_path) as img:
                    width, height = img.size
                    if width < 1020:
                        os.remove(image_file_path)
                        os.remove(text_file_path)
                    else:
                        image_info_list.append({'filename': image_file_name, 'resolution': (width, height)})

        # Sort the image_info_list based on resolution
        sorted_images = sorted(image_info_list, key=lambda x: x['resolution'])

        # Print the sorted list
        for image in sorted_images:
            print(f"Filename: {image['filename']}, Resolution: {image['resolution']}")

    def create_modify_text_files(self, content):
        """
        Creates or modifies label text files for images with the provided content.

        Args:
            content (str): The content to be written to the label text files.
        """
        # List all image files in the folder
        image_files = [file for file in os.listdir(self.folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        # Create text files with the same names as image files and write content
        for image_file in image_files:
            text_file_name = os.path.splitext(image_file)[0] + '.txt'
            text_file_path = os.path.join(self.folder_path, text_file_name)

            with open(text_file_path, 'w') as text_file:
                text_file.write(content)

    def change_class_id_in_text_files(self, cid):
        """
        Changes the class ID in label text files to the provided class ID.

        Args:
            cid (str): The new class ID.
        """
        # Iterate through each text file in the folder
        for file_name in os.listdir(self.folder_path):
            if file_name.lower().endswith('.txt'):
                file_path = os.path.join(self.folder_path, file_name)
                lines = []

                # Read and modify each line in the text file
                with open(file_path, 'r') as text_file:
                    for line in text_file:
                        parts = line.strip().split()  # Split line into parts
                        if parts:
                            parts[0] = cid  # Change the first value to '1'
                            modified_line = ' '.join(parts)  # Join parts back to a line
                            lines.append(modified_line)

                # Write the modified lines back to the text file
                with open(file_path, 'w') as text_file:
                    text_file.write('\n'.join(lines))

if __name__ == "__main__":
    load_dotenv()
    data_folder = os.getenv("data_folder")
    train_folder = os.getenv("train_folder")
    test_folder = os.getenv("test_folder")
    valid_folder = os.getenv("valid_folder")

    data_processor = DataProcessor(data_folder, train_folder, test_folder, valid_folder)
    data_processor.split_data()
    data_processor.verify_and_cleanup()

    folder_path = '/home/yami/opbr_bot/opbr_yolo_method/dataset_v1v2_merge/class_41'
    content = """41 0.497807 0.491531 0.607456 0.585602"""  # annotations
    cid = "24"  # class id
    mode = 2

    image_annotations_processor = ImageProcessor(folder_path)
    if mode == 1:
        image_annotations_processor.check_image_resolution()
    elif mode == 2:
        image_annotations_processor.create_modify_text_files(content)
    elif mode == 3:
        image_annotations_processor.change_class_id_in_text_files(cid)

 # Use the new function to move files based on class_id
    class_id_to_move = 39
    source_path_to_move = "/home/yami/opbr_bot/opbr_yolo_method/dataset_v1v2v3_merge/valid/"
    dest_path_to_move = "/home/yami/opbr_bot/opbr_yolo_method/dataset_v1v2v3_merge/class_39/"
    data_processor.move_files_to_class_folder(source_path_to_move, dest_path_to_move, class_id_to_move)