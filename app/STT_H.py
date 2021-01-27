# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 

@author: Harsh
"""

#!/usr/bin/env python
from __future__ import absolute_import, division, print_function

import argparse
import numpy as np
import shlex
import subprocess
import sys
import wave
#import json

import pyaudio
import wave
    

from deepspeech import Model, version
from timeit import default_timer as timer


try:
    from shhlex import quote
except ImportError:
    from pipes import quote




def record():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024
    RECORD_SECONDS = 7
    WAVE_OUTPUT_FILENAME = "test1.wav"
 
    p = pyaudio.PyAudio()
    p.get_default_input_device_info()
    # start Recording
    stream = p.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    print ("Listening....")
    frames = []
  
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print ("finished recording")
 
 
    # stop Recording
    stream.stop_stream()
    stream.close()
    p.terminate()
 
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(p.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
	

    """from scipy.io.wavfile import write

    fs = 16000  # Sample rate
    seconds = 5  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    print("Listening..")
    sd.wait()  # Wait until recording is finished
    print("Done, running deepspeech..")
    write('output.wav', fs, myrecording)  # Save as WAV file """

def convert_samplerate(audio_path, desired_sample_rate):
    sox_cmd = 'sox {} --type raw --bits 16 --channels 1 --rate {} --encoding signed-integer --endian little --compression 0.0 --no-dither - '.format(quote(audio_path), desired_sample_rate)
    try:
        output = subprocess.check_output(shlex.split(sox_cmd), stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        raise RuntimeError('SoX returned non-zero status: {}'.format(e.stderr))
    except OSError as e:
        raise OSError(e.errno, 'SoX not found, use {}hz files or install it: {}'.format(desired_sample_rate, e.strerror))

    return desired_sample_rate, np.frombuffer(output, np.int16)


def metadata_to_string(metadata):
    return ''.join(token.text for token in metadata.tokens)


def words_from_candidate_transcript(metadata):
    word = ""
    word_list = []
    word_start_time = 0
    # Loop through each character
    for i, token in enumerate(metadata.tokens):
        # Append character to word if it's not a space
        if token.text != " ":
            if len(word) == 0:
                # Log the start time of the new word
                word_start_time = token.start_time

            word = word + token.text
        # Word boundary is either a space or the last character in the array
        if token.text == " " or i == len(metadata.tokens) - 1:
            word_duration = token.start_time - word_start_time

            if word_duration < 0:
                word_duration = 0

            each_word = dict()
            each_word["word"] = word
            each_word["start_time"] = round(word_start_time, 4)
            each_word["duration"] = round(word_duration, 4)

            word_list.append(each_word)
            # Reset
            word = ""
            word_start_time = 0

    return word_list


def metadata_json_output(metadata):
    json_result = dict()
    json_result["transcripts"] = [{
        "confidence": transcript.confidence,
        "words": words_from_candidate_transcript(transcript),
    } for transcript in metadata.transcripts]
    return json.dumps(json_result, indent=2)



class VersionAction(argparse.Action):
    def __init__(self, *args, **kwargs):
        super(VersionAction, self).__init__(nargs=0, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print('DeepSpeech ', version())
        exit(0)

def predict_text(filepath):
    model_load_start = timer()
    # sphinx-doc: python_ref_model_start
    ds = Model('deepspeech-0.8.2-models.pbmm')
    # sphinx-doc: python_ref_model_stop
    model_load_end = timer() - model_load_start
    print('Loaded model in {:.3}s.'.format(model_load_end), file=sys.stderr)

    desired_sample_rate = ds.sampleRate()
    
    #print('Loading scorer from files {}'.format(args.scorer), file=sys.stderr)
    scorer_load_start = timer()
    ds.enableExternalScorer('kenlm1.scorer')
    scorer_load_end = timer() - scorer_load_start
    print('Loaded language model in {:.3}s.'.format(scorer_load_end), file=sys.stderr)


    fin = wave.open(filepath, 'rb')
    fs_orig = fin.getframerate()
    if fs_orig != desired_sample_rate:
        print('Warning: original sample rate ({}) is different than {}hz. Resampling might produce erratic speech recognition.'.format(fs_orig, desired_sample_rate), file=sys.stderr)
        fs_new, audio = convert_samplerate('test1.wav', desired_sample_rate)
    else:
        audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

    audio_length = fin.getnframes() * (1/fs_orig)
    fin.close()

    print('Running inference.', file=sys.stderr)
    inference_start = timer()
    # sphinx-doc: python_ref_inference_start
    text = ds.stt(audio)
    # sphinx-doc: python_ref_inference_stop
    inference_end = timer() - inference_start
    print('Inference took %0.3fs for %0.3fs audio file.' % (inference_end, audio_length), file=sys.stderr)
    return text

