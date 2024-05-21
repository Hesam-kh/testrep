import scipy.io
import matplotlib.pyplot as plt
import numpy as np


class data(object):
    def __init__(self):
        self.mat_perfect = scipy.io.loadmat('F:/MS project/code/Channel data/mehran/perfect channel/Perfect_H_40000.mat')
        self.data_perfect = self.mat_perfect ['My_perfect_H']
        
        #self.mat_22db = scipy.io.loadmat('F:/MS project/code/Channel data/mehran/noisy channel 22db/My_noisy_H_22.mat')
        #self.data_22db = self.mat_22db ['My_noisy_H']
        
        #self.mat_12db = scipy.io.loadmat('F:/MS project/code/Channel data/mehran/noisy channel 12db/My_noisy_H_12.mat')
        #self.data_12db = self.mat_12db ['My_noisy_H']
    
    def perfect_channel(self):
        data_perfect_real = self.data_perfect.real
        data_perfect_imag = self.data_perfect.imag
        
        channel_perfect_real = data_perfect_real.reshape((40000,1008))
        channel_perfect_imag = data_perfect_imag.reshape((40000,1008))
        
        #channel_perfect_real_mean = np.mean(channel_perfect_real,0)
        #channel_perfect_imag_mean = np.mean(channel_perfect_imag,0)
        
        #channel_perfect_real_var = np.var(channel_perfect_real,0)
        #channel_perfect_imag_var = np.var(channel_perfect_imag,0)
        
        return channel_perfect_real, channel_perfect_imag
    
    def twenty_two_db_noisy_channel(self):
        
        data_22db_real = self.data_22db.real
        data_22db_imag = self.data_22db.imag
        
        channel_22db_real = data_22db_real.reshape((40000,1008))
        channel_22db_imag = data_22db_imag.reshape((40000,1008))
        
        #channel_22db_real_mean = np.mean(channel_22db_real,0)
        #channel_22db_imag_mean = np.mean(channel_22db_imag,0)
        
        #channel_22db_real_var = np.var(channel_22db_real,0)
        #channel_22db_imag_var = np.var(channel_22db_imag,0)
        
        return channel_22db_real, channel_22db_imag
    
    def twleve_db_noisy_channel(self):
        
        data_12db_real = self.data_12db.real
        data_12db_imag = self.data_12db.imag

        channel_12db_real = data_12db_real.reshape((40000,1008))
        channel_12db_imag = data_12db_imag.reshape((40000,1008))

        #channel_12db_real_mean = np.mean(channel_12db_real,0)
        #channel_12db_imag_mean = np.mean(channel_12db_imag,0)

        #channel_12db_real_var = np.var(channel_12db_real,0)
        #channel_12db_imag_var = np.var(channel_12db_imag,0)
        
        return channel_12db_real, channel_12db_imag

    def desired_SNR(self,SNR_db):
        
        channel_perfect_real, channel_perfect_imag = self.perfect_channel()
        
        scale_SNR_db = 1/(10**(SNR_db/10))
        noise_SNR_db = np.random.normal(0,np.sqrt(scale_SNR_db),(40000,1008)) 
        
        channel_SNR_db_real = channel_perfect_real + noise_SNR_db
        channel_SNR_db_imag = channel_perfect_imag + noise_SNR_db
        
        return channel_SNR_db_real, channel_SNR_db_imag
#%%
A = data()
channel,_ = A.perfect_channel()

print(np.sum(channel[0,:]**2)/1008)       
''' 
SMALL_SIZE = 13
MEDIUM_SIZE = 15
BIGGER_SIZE = 17

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title   

plt.figure('The first row of channel_perfect_real')
plt.plot(channel_perfect_real[0,:],linewidth=1.5)
plt.title('The first row of channel_perfect_real')   

plt.figure('mean of channel_perfect_real')
plt.plot(channel_perfect_real_mean,linewidth=1.5)
plt.title('mean of channel_perfect_real') 

x = np.linspace(0, 1008, 1008)
plt.figure('channel_perfect_real')
plt.plot(x,channel_perfect_real_mean,'g-')
plt.fill_between(x,channel_perfect_real_mean-(2*channel_perfect_real_var),channel_perfect_real_mean+(2*channel_perfect_real_var),alpha=0.5)
plt.title('channel_perfect_real')
plt.grid()  
'''