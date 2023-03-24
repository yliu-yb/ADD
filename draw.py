import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

# font set
plt.rcParams['font.family'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False
SMALL_SIZE = 9
MEDIUM_SIZE = 10
BIGGER_SIZE = 10
plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)  # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

# cm to inches
cm = 1 / 2.54

def DrawLine(x1, y1, x2, y2):
    nrows, ncols = 2, 1
    figsize = [16 * cm, 15 * cm]
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, dpi=300)

    ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    ax[0].xaxis.set_major_locator(mdates.YearLocator(5))
    ax[0].xaxis.set_minor_locator(mdates.YearLocator(1))
    ax[1].xaxis.set_major_locator(mdates.YearLocator(5))
    ax[1].xaxis.set_minor_locator(mdates.YearLocator(1))

    ax[0].yaxis.set_major_locator(ticker.MultipleLocator(5))
    ax[0].yaxis.set_minor_locator(ticker.MultipleLocator(1))
    ax[1].yaxis.set_major_locator(ticker.MultipleLocator(5))
    ax[1].yaxis.set_minor_locator(ticker.MultipleLocator(1))

    ax[0].set_xlabel("Date(UTC)")
    ax[1].set_xlabel("Date(UTC)")
    ax[0].set_ylabel("$^\circ$C")
    ax[1].set_ylabel("$^\circ$C")
    ax[0].set_title("Area-Averaged Monthly daytime 3min CMG Land-surface Temperature")
    ax[1].set_title("Area-Averaged Monthly nighttime 3min CMG Land-surface Temperature")

    ax[0].plot(x1, y1, color = "black", marker = 'o', markersize = 2)
    ax[1].plot(x2, y2, color = "black", marker = 'o', markersize = 2)

    plt.tight_layout()

    plt.savefig("./LST.png", dpi = 600)