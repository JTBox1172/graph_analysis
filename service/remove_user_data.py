import threading
import time
import datetime
import os

def cleanUp():
    while True:
        print("cleaning")
        return_data_path = "./user_data/return_data"
        uploaded_data_path = "./user_data/uploaded_data"
        return_files = [f for f in os.listdir(return_data_path) if os.path.isfile(os.path.join(return_data_path, f))]
        uploaded_files = [f for f in os.listdir(uploaded_data_path) if os.path.isfile(os.path.join(uploaded_data_path, f))]
        for file in return_files:
            print(f"removing {file}")
            file_path = os.path.join(return_data_path, file)
            time_stored = (int((datetime.datetime.now()).timestamp())) - (os.path.getctime(file_path))
            if(time_stored > 300):
                os.remove(file_path)
        for file in uploaded_files:
            print(f"removing {file}")
            file_path = os.path.join(uploaded_data_path, file)
            time_stored = (int((datetime.datetime.now()).timestamp())) - (os.path.getctime(file_path))
            if(time_stored > 300):
                os.remove(file_path)
        time.sleep(120)

thread = threading.Thread(target=cleanUp)
thread.daemon = True
thread.start()