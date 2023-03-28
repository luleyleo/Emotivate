
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

sns.set_theme(style="darkgrid")

# title
TITLE = 'V-A Space'
plt.title(TITLE, loc='center')

POINT_TRANSPARENCY = 0.66
POINT_SIZE = 66
POINT_INNER_COLOR='red'
POINT_EDGE_COLOR='red'

RING_TRANSPARENCY = 0.33

def plt_va(valence:[float], arousal:[float], img_path:str):
    '''
    save plot of datapoints consisting of valence (x-axis) and arousal (y-axis)
    :param valence: list of valence values
    :param arousal: list of arousal values
    :param img_path: image path
    :return:
    '''
    global POINT_TRANSPARENCY,RING_TRANSPARENCY,POINT_INNER_COLOR,POINT_EDGE_COLOR

    target_label = 'valence\narousal: {1}'.format(valence, arousal)
    ax = sns.scatterplot(
        x=valence,
        y=arousal,
        label=target_label,
        legend=False,
        alpha=POINT_TRANSPARENCY,
        s=POINT_SIZE,
        edgecolor=POINT_EDGE_COLOR,
        color= POINT_INNER_COLOR
    )

    # unit circle
    ax.add_patch(plt.Circle((0, 0), radius=0.25, edgecolor='black', facecolor='None', alpha=RING_TRANSPARENCY, label='r=0.25'))
    ax.add_patch(plt.Circle((0, 0), radius=0.50, edgecolor='black', facecolor='None', alpha=RING_TRANSPARENCY, label='r=0.50'))
    ax.add_patch(plt.Circle((0, 0), radius=0.75, edgecolor='black', facecolor='None', alpha=RING_TRANSPARENCY, label='r=0.75'))
    ax.add_patch(plt.Circle((0, 0), radius=1.00, edgecolor='black', facecolor='None', alpha=RING_TRANSPARENCY, label='r=1.00'))

    # resizing
    plt.rcParams["figure.figsize"] = (10, 10) # (20, 20)
    pos = ax.get_position()
    pos = [pos.x0, pos.y0 - 0.05,  pos.width, pos.height]
    ax.set_position(pos)
    ax.set_aspect('equal')

    plt.annotate('valence', xy=(0.9, 0.02))
    plt.annotate('arousal', xy=(0.02, 1.2))

    # tweak aesthetic
    plt.tick_params(
        axis='both',
        which='major',
        bottom=False,
        top=False,
        labelbottom=False,
        right=False,
        left=False,
        labelleft=False
    )
    ax.grid(False)

    # origin
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    # tweak bounds
    ax.set(xlim=(-1, 1))
    ax.set(ylim=(-1, 1))
    ax.set_xbound(lower=-1.30, upper=1.30)
    ax.set_ybound(lower=-1.30, upper=1.30)

    plt.savefig(img_path, bbox_inches='tight')
   #plt.show()