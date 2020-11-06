# ASR_Citi
Automatic Speech Recognition specially designed for specific use case words using Deepspeech 

# Steps


# Create and activate a virtualenv
virtualenv -p python3 $HOME/tmp/deepspeech-venv/

source $HOME/tmp/deepspeech-venv/bin/activate

# Install DeepSpeech
pip3 install deepspeech

# Download pre-trained English model files
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.1/deepspeech-0.9.1-models.pbmm

curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.1/deepspeech-0.9.1-models.scorer

This will install acoustic model file and language model file scorer(This model file scorer is a huge language model created by mozilla covering general english words) 

Modify the path and the name of the model and scorer in STT_H.py accordingly. 

# Creating own language model file
# Build Kenlm
wget -O - https://kheafield.com/code/kenlm.tar.gz | tar xz

mkdir kenlm/build

cd kenlm/build

cmake ..

make -j2

After having kenlm built and a kenlm folder which has files in kenlm/build/bin 

# Create vocab.txt
Create vocab.txt file with words/sentences which you want the ASR system to recognise.

# Run Generate_lm_H.py 
Run the Generate_lm_H.py file having the paths to vocab.txt, alphabet.txt and kenlm corrected accordingly. 

This python file will create a kenlm1.scorer file which will now be the language model file for the STT_h.py code.


