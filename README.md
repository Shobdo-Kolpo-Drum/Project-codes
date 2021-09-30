# Project-codes
All the codes we built for the project.
We are not allowing anyone to copy or use this code for now.But hopefully we will let it be open source for all in near future

# Procedure
Should follow the rules below to finish the training.We are using google collab for training purposes.The instructions here are given accordingly.

# Clone DeepSpeech repository

> !git clone https://github.com/mozilla/DeepSpeech.git

# Connect google drive  with collab

>from google.colab import drive

>drive.mount('/content/drive')

# Update Tensorflow

>!pip install --upgrade tensorflow

# Know What version of GPU is provided by google collab
At change the runtime of google collab from google collab menu to GPU.You can use CPU as runtime but the process will be slower 

>!nvidia-smi

# Change directory & install DeepSpeech Train

>%cd DeepSpeech

>!pip3 install --upgrade -e .

# Python3-dev for additional python feature

>!sudo apt-get install python3-dev

# Install Tensorflow GPU

As we are using GPU as Runtime we need to install tensorflow-gpu

>!pip3 uninstall tensorflow

>!pip3 install 'tensorflow-gpu==1.15.4'

# Generating the scorer
To support the trained file we need to generate a scorer file for more accuracy(not necessary)

# Training
Training our dataset with the framework.To do so we need to set some flags(--) and point the training framework to our dataset with csv files Which we have prepared before.

>!python3 DeepSpeech.py \
--alphabet_config_path path-to-alphabet \
  --train_files Path-to-train-file-csv \
  --dev_files path-to-dev-file-csv \
  --test_files path-to-test-file-csv \
  --checkpoint_dir path-to-checkpoints \
  --export_dir path-to-output-the-model \
  --load_checkpoint_dir path-to-load-the-previous-checkpoint-froom \
  --save_checkpoint_dir path-to-save-the-checkpoint \
  --checkpoint_secs 1800 \
  --max_to_keep 2 \
  --n_hidden 64 \
  --early_stop true \
  --es_epochs 10 \
  --use_allow_growth true \
  
  # Some useful flags
  
  # Install SOX
  For managing the wav files of different types
  
  >!apt -qq install -y sox
  
  # Testing our trained model
  
 > !deepspeech --model path-to-model --audio path-to-audio-you-want-to-convert-to-text
  
  
  


  
  



