import matplotlib.pyplot as plt, matplotlib.animation as animation
import numpy as np, scipy.ndimage as ndi
from scipy.io import wavfile
import os, sys, utility


class AudioData:

    source = ''
    title = ''
    data = {}

    def __init__(self, path_to_file):
        try:
            self.title = path_to_file.split('/')[1]
            print self.title
        except IndexError:
            print "Path to file looks wrong..."
            print path_to_file
            exit(0)
        self.source = path_to_file
        self.data = self.load_audio_data()
        fft_space, fft_space_2 = self.pre_process_audio()
        print str(len(fft_space)) + " Frames"
        print str(len(fft_space_2)) + " Frames"
        self.visualize(fft_space, 300, True)

    @staticmethod
    def visualize(frames, frame_rate, color):
        f = plt.figure()
        film = []
        for frame in frames:
            if color:
                film.append([plt.imshow(np.array(frame))])
            else:
                film.append([plt.imshow(frame, 'gray_r')])
        a = animation.ArtistAnimation(f, film, interval=frame_rate,blit=True,repeat_delay=900)
        plt.show()

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

    def pre_process_audio(self):
        frames = []
        animated = []
        # Create a sliding buffer of 1s windows
        buff = 89600
        audio = self.data['data']
        N = np.array(audio[:,0]).shape[0]/buff
        for i in range(N):
            s1 = np.array(audio[0+i*buff:buff/2+i*buff,0])
            s2 = np.array(audio[0+i*buff:buff/2+i*buff,1])
            frame = np.zeros((len(s1),2))
            frame[:,0] = np.log10(np.abs(np.fft.fft(s1)))
            frame[:,1] = np.log10(np.abs(np.fft.fft(s2)))
            frames.append(np.array(frame).reshape(280,320))
            for image in self.automatize(np.array(frame).reshape(280,320),5):
                animated.append(image)
        return animated, frames

    def automatize(self,fft_space, depth):
        f0 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]]
        f1 = [[0,0,0,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0]]
        b0 = [[2,2,2,2,2],[2,1,1,1,2],[2,1,0,1,2],[2,1,1,1,2],[2,2,2,2,2]]

        '''
        frame = fft_space.pop()
        test = ndi.convolve(frame, b0)
        f, ax = plt.subplots(1, 2, sharex=True, sharey=True)
        ax[0].imshow(frame)
        ax[0].set_title('original clip')
        ax[1].imshow(test)
        ax[1].set_title('filtered clip')
        plt.show()
        '''

        modified_reel = []
        for i in range(depth):
            dims = np.array(fft_space).shape
            space = ndi.convolve(np.array(fft_space), f0)
            modified_reel.append(space)
            try:
                ii = 0
                for cell in space.flatten():
                    if cell > 100:
                        space[ii] -= 10
                    if 200 < cell < 100:
                        space[ii] == 10
                    ii += 1
            except IndexError:
                continue

        return modified_reel


def main():
    song_name = '/beastly.wav'
    song_name2 = '/wait.wav'
    if '-demo' in sys.argv:
        # Determine initial Memory Overhead
        mem_0 = utility.check_mem_usage()/1000
        print "[Initial RAM Consumption:"+str(mem_0)+"Kb]"
        ad = AudioData(song_name)

        # Check on RAM consumption
        print "** " + str((utility.check_mem_usage()-mem_0)/1000)+\
              "Kb of Additional RAM Being Used**"

        # Play it and clean up
        # ad.play_audio()
        # ad.destroy()
    else:
        # Determine initial Memory Overhead
        target = sys.argv[1]
        mem_0 = utility.check_mem_usage() / 1000
        print "[Initial RAM Consumption:" + str(mem_0) + "Kb]"
        ad = AudioData(target)
        ad.convert_and_move()
        # Play it and clean up
        ad.display_audio_info()
        ad.destroy()


if __name__ == '__main__':
    main()