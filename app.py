import os
from datetime import datetime

from utils import save_to

def main(*args):
    
    now = datetime.now().strftime("%d%m%Y_T_%H%M%S")

    if "json" in args:
        output_path = f"{os.getcwd()}\\data\\output-{now}.json"
        print("saving to json initiated, path is: ", output_path)
        save_to.data_json(output_path)
    if "spark-streaming" in args:
        save_to.spark()
    else:
        save_to.console()

if __name__ == "__main__":
    main("json")