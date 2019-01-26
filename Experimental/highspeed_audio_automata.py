import numpy as np
from scipy.io import wavfile
import os, sys, utility


class AudioData:

    source = ''
    title = ''
    data = {}

    def __init__(self, path_to_file):
        self.source = path_to_file
        self.title = self.convert_and_move()
        self.data = self.load_audio_data()

    def convert_and_move(self):
        song_name = self.source.split('/')[len(self.source.split('/'))-1]
        os.system('cp '+self.source+' $PWD;')
        os.system('ffmpeg -loglevel quiet -i '+song_name+' '+song_name.split('.')[0]+'.wav')
        os.system('rm '+song_name)
        return song_name.split('.')[0]+'.wav'

    def load_audio_data(self):
        sample_rate, raw_data = wavfile.read(self.title)
        audio_data = np.array(raw_data)
        n_samples = audio_data.shape[0]
        song_length = float(n_samples)/sample_rate
        audio_info = {'sample_rate':sample_rate,
                      'n_samples':n_samples,
                      'seconds':song_length,
                      'data': audio_data}
        return audio_info

    def play_audio(self):
        try:
            os.system('paplay ' + self.title)
        except KeyboardInterrupt or IOError:
            print "Destroying Audio Data and Exiting..."

    def destroy(self):
        os.system('rm '+self.title)

    def display_audio_info(self):
        print "Sample Rate: "+str(self.data['sample_rate'])
        print "N_Samples: "+str(self.data['n_samples'])
        print "Runtime: " + str(self.data['seconds'])+'s '
        print "Data Shape: "+str(self.data['data'].shape)


def main():
    if '-demo' in sys.argv:
        # Determine initial Memory Overhead
        mem_0 = utility.check_mem_usage()/1000
        print "[Initial RAM Consumption:"+str(mem_0)+"Kb]"

        ad = AudioData('/media/root/CoopersDB/MUSIC/Disturbed/deify.mp3')

        # Check on RAM consumption
        print "** " + str((utility.check_mem_usage()-mem_0)/1000)+\
              "Kb of Additional RAM Being Used**"
        # Play it and clean up
        ad.play_audio()
        ad.destroy()
    else:
        # Determine initial Memory Overhead
        target = sys.argv[1]
        mem_0 = utility.check_mem_usage() / 1000
        print "[Initial RAM Consumption:" + str(mem_0) + "Kb]"

        ad = AudioData(target)

        # Play it and clean up
        ad.display_audio_info()
        ad.destroy()


if __name__ == '__main__':
    main()