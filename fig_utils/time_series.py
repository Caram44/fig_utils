import matplotlib.pyplot as plt
import numpy as np
# change values here to affect defaults


class Time_series_fig:

    def __init__(self, figsize=(12, 6), ylabel='', xlabel='',
                 xticks=True, yticks=True,
                 xticklabels=True, yticklabels=True,
                 xlim=None, ylim=None, title='', name='',
                 style='seaborn-colorblind', fontsize=16):

        self.figsize = figsize
        plt.rcParams.update({'font.size': fontsize})
        fig, ax = plt.subplots(1, figsize=self.figsize)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_title(title)
        ax.grid(axis='y')
        if xticks is None:
            xticks = []
        if xticks is True:
            xticks = ax.get_xticks()
        if yticks is True:
            yticks = ax.get_yticks()
        if yticks is None:
            yticks = []
        if xticklabels is None:
            xticklabels = [''] + ['']*len(xticks)
        if yticklabels is None:
            yticklabels = [''] + ['']*len(yticks)
        if xticklabels is True:
            xticklabels = [''] + list(xticks[1:])
        if yticklabels is True:
            yticklabels = [''] + list(yticks[1:])
        if xlim is None:
            xlim = ax.get_xlim()
        else:
            xlim = (xticks[0], xticks[-1])
        if ylim is None:
            ylim = ax.get_ylim()
        else:
            ylim = (yticks[0], yticks[-1])
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_xticks(xticks)
        ax.set_yticks(yticks)
        ax.set_xticklabels(xticklabels)
        ax.set_yticklabels(yticklabels)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        self.fig = fig
        self.ax = ax
