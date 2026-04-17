from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

class SignalDetection:
    def __init__(self, hits, misses, false_alarms, correct_rejections):
        self.hits = hits
        self.misses = misses
        self.false_alarms = false_alarms
        self.correct_rejections = correct_rejections
        #check for non-numeric values. this should also inherently check 
        #for unwanted characters. 
        attributes = [hits, misses, false_alarms, correct_rejections]
        if not all(isinstance(x, (int, float)) for x in attributes):
            raise ValueError("all inputs must be numeric")

        #check for negative values 
        if hits < 0 or misses < 0 or false_alarms < 0 or correct_rejections < 0:
            raise ValueError("values cannot be negative")   

        #avoid dividing by zero, and taking ppf(0). just make it 1e-9 so almost 0 but not exactly.
        if self.hits == 0:
            self.hits = 1e-9
        if self.misses == 0:
            self.misses = 1e-9
        if self.false_alarms == 0:
            self.false_alarms = 1e-9
        if self.correct_rejections == 0:
            self.correct_rejections = 1e-9
        
        return 

    
    def hit_rate(self):
        return self.hits / (self.hits + self.misses)

    def false_alarm_rate(self):
        return self.false_alarms / (self.false_alarms + self.correct_rejections)
    
    def d_prime(self):
        return norm.ppf(self.hit_rate()) - norm.ppf(self.false_alarm_rate())

    def criterion(self):
        return -0.5 * (norm.ppf(self.hit_rate()) + norm.ppf(self.false_alarm_rate()))

    def __add__(self, other):
        return SignalDetection(self.hits + other.hits, self.misses + other.misses, self.false_alarms + other.false_alarms,
                               self.correct_rejections + other.correct_rejections)
    
    def __sub__(self, other):
        return SignalDetection(self.hits - other.hits, self.misses - other.misses, self.false_alarms - other.false_alarms,
                               self.correct_rejections - other.correct_rejections)
    
    def __mul__(self, factor):
        return SignalDetection(self.hits * factor, self.misses * factor, self.false_alarms * factor, self.correct_rejections * factor)

    def plot_sdt(self):
        fig, ax = plt.subplots()
        mu_signal = 0.8
        mu_noise = 0
        sigma = 1 #same variance
        x = np.linspace(mu_noise - 4, mu_signal + 4, 1000)
        peak = norm.pdf(0, 0, sigma)
        plt.plot(x, norm.pdf(x, mu_signal, sigma), label = 'Signal', color = 'blue')
        plt.plot(x, norm.pdf(x, mu_noise, sigma), label = 'Signal + Noise', color = 'red')
        ax.set_title('Signal to Noise')
        ax.annotate("d'", xy=(mu_noise, peak), xytext=(mu_signal, peak), 
                    arrowprops=dict(arrowstyle='<->', color='black', linewidth=2))

        ax.axvline(x=self.criterion(), color='black', linestyle='--', linewidth=2, label = "criteron")
        ax.legend(loc = 'best')

        return fig, ax

    @staticmethod
    def plot_roc(sdt_list):
        if not all(isinstance(attribute, SignalDetection) for attribute in sdt_list):
            raise TypeError("all inputs must be of SignalDetection class")
        false_alarms = [0]
        hit_rates = [0]
        for sdt_instance in sdt_list:
            false_alarms.append(sdt_instance.false_alarm_rate())
            hit_rates.append(sdt_instance.hit_rate())

        false_alarms.append(1)
        hit_rates.append(1)

        fig, ax = plt.subplots()
        ax.plot(false_alarms, hit_rates, color = 'purple')
        ax.set_xlim([0,1])
        ax.set_ylim([0,1])
        ax.set_xlabel('False Alarm Rate')
        ax.set_ylabel('Hit Rate')
        ax.set_title('ROC Curve')
        
        
        return fig, ax
    

if __name__ == "__main__":
    # test = SignalDetection(-9, 3, 4,5)
    # test = SignalDetection(0, 0, 0,0)
    # test = SignalDetection(0, 3, 'ttr', '5%')

    sdt1 = SignalDetection(133, 431, 7, 23)
    print("hit rate:", sdt1.hit_rate())
    print("false alarm rate:", sdt1.false_alarm_rate())
    print("d':", sdt1.d_prime())
    print("criterion:", sdt1.criterion())
    fig1, ax1 = sdt1.plot_sdt()
    fig1.savefig('sdt_plot.png')

    sdt2 = SignalDetection(3, 10, 6, 14)
    sdt3 = SignalDetection(4, 6, 31, 8)
    fig2, ax2 = SignalDetection.plot_roc([sdt1, sdt2, sdt3])
    fig2.savefig('roc_plot.png')

