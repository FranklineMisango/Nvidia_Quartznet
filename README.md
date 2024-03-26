# Nvidia_Quartznet
An Intermediate Speech-Text Transcriptor with Nvidia Quartznet Model

### Execution Instructions

1. Download the Libri dataset
    - Train - https://www.openslr.org/resources/60/train-clean-360.tar.gz
    - Dev/Val - https://www.openslr.org/resources/60/dev-clean.tar.gz
    - Test - https://www.openslr.org/resources/60/test-clean.tar.gz
    - Download all the tar zip files in a folder named data in the modular code directory

2. Unzip the data
    - Unzip the data by the folder with the commands
      (Run the commands on the same level, in the modular code directory.)
      tar -xf data/train-clean-360.tar.gz
      tar -xf data/dev-clean.tar.gz
      tar -xf data/test-clean.tar.gz
    
    - The folders named train-clean-360, dev-clean and test-clean will be created in the data folder one by one as the tar files unzip. It will take time as the data files are large. 

    - Rename the newly created folders to train, dev, and test respectively.

3. Run the train.py script to initialize the trainer.
    - It will first generate text files for the paths to the audio files in your data in the folder called filelists, named train_data.txt and val_data.txt.
    - You can change the configurations in config.yml to control the number of epochs and batch size.

4. Run the test.py script for testing, it will first generate a test_data.txt file in filelist and then initialize a trainer and then will show WER (Word Error Rate) in the end.

5. You can run the command "tensorboard --logdir logs" to monnitor your experiments.

6. A custom trained model and configurations are saved in a folder called best_model in notebooks which can be used for inference purposes in the file called NVidiaQuartzNet_bestmodel.ipynb.
   - Upload the file in a Google drive folder called Speech_to_Text
   - Upload best model folder in the same directory Speech_to_Text
   - Run the commands in the ipython file to first create a symbolic link and then run the rest of the codes to transcribe a youtube video.
    - You can also use model configurations as in quartznet15x15.yaml and your own trained checkpoints saved in a directory called checkpoints while running train.py for inference.

7. Nvidia Pretrained model is used in the file called NVidiaQuartzNet.ipynb.
   Upload it in the drive and run it using Google Colab as shown in lectures.


Python version - 3.8.10
