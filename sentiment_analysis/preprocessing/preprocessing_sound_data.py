import pathlib
import librosa
from tqdm import tqdm
from PIL import Image
import numpy as np


def save_mfcc_features(audio_files, out_dir, frames_root):
    for file in tqdm(audio_files):

        # only extract features for existing files
        if file.is_file():
            signal, sr = librosa.load(file)
            mel_f = librosa.feature.melspectrogram(signal, sr=sr, hop_length=int(0.010 * sr))

            #save features to a file, whose name equals original file, but in the output dir
            a = file.stem
            output_file = pathlib.Path(out_dir, file.stem + '.npz')
            np.savez_compressed(output_file.as_posix(), {'mel_spectrum': mel_f})


dataset_root = pathlib.Path('data/datasets/emo_db')
preprocessed_root = pathlib.Path('data/preprocessed/emo_db')
audio_root = pathlib.Path(dataset_root, 'wav')

#  get a list of absolute paths for corresponding '.wav'-files
audio_files = audio_root.glob('*')
mfcc_out_dir = pathlib.Path(preprocessed_root, 'mel_spectrum')
mfcc_out_dir.mkdir(parents=True, exist_ok=True)

save_mfcc_features(audio_files, mfcc_out_dir)