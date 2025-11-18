import os
import logging

logging.basicConfig(
    filename= 'file_checker.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_large_files(directory, max_size_mb):
    large_files = []
    try:
        for file in os.listdir(directory):
            path = os.path.join(directory, file)
            if os.path.isfile(path):
                size_mb = os.path.getsize(path) / (1024 * 1024)
                if size_mb > max_size_mb:
                    large_files.append((file, round(size_mb, 2)))
                    logging.warning(f"{file} is too large: {size_mb:.2f} MB")
                else:
                    logging.info(f"{file} is okay: {size_mb:.2f} MB")
    except Exception as e:
        logging.error(f"Failed to scan directory: {e}")
    return large_files


get_large_files("C:/Users/AbdulAhad/Desktop/Python-Learn", 10)
