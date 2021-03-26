# Speech recognition
Automatic Speech Recognition specially designed for specific use case words using Deepspeech

## Step 1. Create and activate a virtualenv
virtualenv -p python3 $HOME/tmp/deepspeech-venv/

source $HOME/tmp/deepspeech-venv/bin/activate

## Step 2. Install DeepSpeech
pip3 install deepspeech

## Step 3. Download pre-trained English model files
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.1/deepspeech-0.9.1-models.pbmm

curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.1/deepspeech-0.9.1-models.scorer

This will install acoustic model file and language model file scorer(This model file scorer is a huge language model created by mozilla covering general english words) 

We are using deepspeech created acoustic model, and our own language model which we created using the script Generate_lm_H.py

Modify the path and the name of the model and scorer in STT_H.py accordingly. 

## Step 4. Creating own language model file
### Build Kenlm
wget -O - https://kheafield.com/code/kenlm.tar.gz | tar xz

mkdir kenlm/build

cd kenlm/build

cmake ..

make -j2

After having kenlm built and a kenlm folder which has files in kenlm/build/bin 

### Create vocab.txt
Create vocab.txt file with words/sentences which you want the ASR system to recognise.

### Download generate_scorer_package according to your OS
generate_scorer_package file is found in native_client.tar file which you can download from

https://github.com/mozilla/DeepSpeech/releases

according to your OS

### Run Generate_lm_H.py 
Run the Generate_lm_H.py file having the paths to vocab.txt, alphabet.txt,kenlm and generate_scorer_package corrected accordingly. 

This python file will create a kenlm1.scorer file which will now be the language model file for the STT_h.py code.


# Build app

## Step 1. Setup database
If this is the first time setting up the app on your machine and/or the `app.db` file, which is SQLite file for database is not found in the root directory, run the following commands:
1. `flask db init`
2. `flask db upgrade`
3. `flask db migrate`

## Step 2. Run the app
For the first launches, as well as for testing purposes, we recommend running flask in `dev` mode. Thus, run the following commands:
1. `export FLASK_ENV=development` - this command will ensure that development mode is turned on.
2. `export FLASK_APP=aqua.py` - this command will make sure that the app file is found properly.

Now that you are ready with initial setup, you can run the app:

```flask run```

An important note to keep in mind is that if this is the first launch and/or the query database is empty, the system will attempt at creating the queries from data files (if `queries.txt` is in the filesystem, it will copy from there, if not, it will try to rebuild the queries from the `vocab-tagged.xlsx` file).

If this is the case, you should see a message on the console, where flask app is being run with the following text:

```Creating DB from txt file.```

If you see this message, make sure that you do not terminate the app until the process is completed. Otherwise, you will end up with an incomplete database.

### Correcting errors
In case you encounter any errors along the way (such as db error or incomplete database), follow these steps to restart the process:
1. Remove the `migrations` directory
2. Remove the `app.db` file
