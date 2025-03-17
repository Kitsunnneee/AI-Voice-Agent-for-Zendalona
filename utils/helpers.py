import os
import time

def create_directory_if_not_exists(directory_path):

    if not os.path.exists(directory_path):
        os.makedirs(directory_path, exist_ok=True)
        print(f"Created directory: {directory_path}")

def measure_execution_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.2f} seconds")
        return result
    return wrapper

def clean_text(text):

    text = ' '.join(text.split())
    

    text = text.strip()
    
    return text
