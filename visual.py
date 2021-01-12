import matplotlib.pyplot as plt
import main
import random as rnd
import matplotlib.animation as animation

def entities_pie(categories):
    """
    Task 24: Display a single subplot that shows a pie chart for categories.

    The function should display a pie chart with the number of planets and the number of non-planets from categories.

    :param categories: A dictionary with planets and non-planets
    :return: Does not return anything
    """

    labels = "Planets", "Non-Planets"
    sizes = [len(categories["Planets"]), len(categories["Non-Planets"])]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%")
    ax1.axis("equal")
    plt.show()


def entities_bar(categories):
    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """
    bar_start = [5, 10, 15]
    width = 0.5
    low_g = len(categories["low gravity"])
    medium_g = len(categories["medium gravity"])
    high_g = len(categories["high gravity"])
    p1 = plt.bar(bar_start, [low_g, medium_g, high_g], width)
    plt.title("Entities of Gravity")
    plt.ylabel("Amount")
    plt.xlabel("Type of Gravity")
    plt.xticks(bar_start, ("Low Gravity", "Medium Gravity", "High Gravity"))
    plt.show()


def orbits(summary):
    """
    Task 26: Display subplots where each subplot shows the "small" and "large" entities that orbit the planet.

    Summary is a nested dictionary of the form:
    summary = {
        "orbited planet": {
            "small": [entity, entity, entity],
            "large": [entity, entity]
        }
    }

    The function should display for each orbited planet in summary. Each subplot should show a bar chart with the
    number of "small" and "large" orbiting entities.

    :param summary: A dictionary containing the "small" and "large" entities for each orbited planet.
    :return: Does not return anything
    """


def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """

