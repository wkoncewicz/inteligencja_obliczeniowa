import matplotlib.pyplot as plt
import random
from aco import AntColony
import time

start = time.time()
plt.style.use("dark_background")

COORDS = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
)


def random_coord():
    r = random.randint(0, len(COORDS))
    return r


def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))


plot_nodes()

colony = AntColony(COORDS, ant_count=300, alpha=0.5, beta=1.2,
                pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,
                iterations=300)

optimal_nodes = colony.get_path()

end = time.time()
duration = end - start
print("time:", duration)

for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )


plt.show()

#default - 240.6556715522927
#czas: 18.04226565361023

#colony = AntColony(COORDS, ant_count=150, alpha=1.0, beta=3.0,
                    # pheromone_evaporation_rate=0.20, pheromone_constant=500.0,
                    # iterations=200)
#231.5510487538921 / 240.65567155229272
#czas: 6.019184112548828

#colony = AntColony(COORDS, ant_count=500, alpha=2.0, beta=2.0,
                    # pheromone_evaporation_rate=0.60, pheromone_constant=1500.0,
                    # iterations=100)
#240.65567155229272 / 231.5510487538921
#czas: 10.097235202789307
