from scipy.stats import norm
import matplotlib.pyplot as plt

class SignalDetection:
    def SignalDetection(hits, misses, false_alarms, correct_rejections):
        #check for non-numeric values. this should also inherently check 
        #for unwanted characters. 
        attributes = [hits, misses, false_alarms, correct_rejections]
        if not all(isinstance(x, (int, float)) for x in attributes):
            raise ValueError("all inputs must be numeric")

        #check for negative values 
        if hits < 0 or misses < 0 or false_alarms < 0 or correct_rejections < 0:
            raise ValueError("values cannot be negative")     
    
    def hit_rate(self):
        #returning floats in [0,1] when defined. handle edge cases where denominators are zero.
        #TO DO: define add class and use it 
        H = self.hits / (self.hits + self.misses)

        #TO DO: avoid dividing by zero if both are zero
    
        return H 

    def false_alarm_rate(self):
        #TO DO: avoid dividing by zero if both are zero
        FA = self.false_alarms / (self.false_alarms + self.correct_rejections)

        return FA 
    
    def d_prime(self):
        norm.ppf(self.H) - norm.ppf(self.FA)

    def criterion(self):
        C = -0.5 * (norm.ppf(self.H) + norm.ppf(self.FA))

    def __add__(self, other):
        return SignalDetection(self.hits + other.hits, self.misses + other.misses, self.false_alarms + other.false_alarms,
                               self.correct_rejections + other.correct_rejections)
    
    def __sub__(self, other):
        return SignalDetection(self.hits - other.hits, self.misses - other.misses, self.false_alarms - other.false_alarms,
                               self.correct_rejections - other.correct_rejections)
    
    def __mul__(self, factor):
        return SignalDetection(self.hits * factor, self.misses * factor, self.false_alarms * factor, self.correct_rejections * factor)

    @staticmethod
    def plot_sdt(self):
        #TO DO
        '''overlapping signal and noise normal distributions (same variance, 
        sensible x-range),
          a vertical line for the criterion, and a visual indication of (d') 
          (e.g. horizontal arrow or segment between distribution means). 
        Label axes and include a title or legend so the figure is interpretable.'''

        return
    
    @staticmethod
    def plot_roc(sdt_list):
        fig, ax = plt.subplots()
        ax.plot(hit_rate, false_alarm, color = 'g')
        ax.set_xlim([0,1])
        ax.set_ylim([0,1])
        ax.set_xlabel('Hit Rate')
        ax.set_ylabel('False Alarm Rate')
        ax.set_title('ROC Curve')
        
        
        return fig, ax