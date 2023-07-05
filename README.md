# FOREST_FIRE-USING-CELLULAR-AUTOMATA: Fire spread modeling using probabilistic Cellular Automata
## Introduction
Fire spread modeling is a critical field that holds immense significance in various domains, including wildfire management, urban planning, and disaster response. Understanding and predicting fire behavior allow us to mitigate its destructive potential, safeguard lives, and protect ecosystems. However, this endeavor comes with challenges, including the complex dynamics of fire, the influence of environmental factors, and the need for accurate and efficient modeling techniques. In this project, we delve into fire spread modeling using probabilistic Cellular Automata, aiming to create a framework that captures uncertainties, integrates vital variables, and offers a powerful tool for understanding and mitigating fire spread.

## Challenges Addressed:

Wind Patterns: The speed and direction of wind play a pivotal role in driving and shaping fire behavior. Capturing the complex relationship between wind patterns and fire dynamics is crucial for accurate modeling and prediction.
Probability of Ignition: Factors like the presence of flammable materials, fuel moisture content, and human activities affect the probability of fire occurrence. Incorporating these variables into the modeling process is essential for realistic and effective simulations.
Efficient Modeling Techniques: The scale and complexity of fire dynamics demand computationally efficient algorithms capable of processing vast amounts of data. Balancing accuracy and efficiency ensures that fire spread models can be utilized effectively in real-world scenarios.

## Objective:
By leveraging probabilistic Cellular Automata, our project aims to develop a robust framework that integrates these challenges.
 We strive to capture the uncertainties of fire dynamics, incorporate wind patterns, probability of ignition, and other crucial variables, and provide timely and reliable predictions.
 Through this research, we seek to unlock the secrets of fire spread, mitigate its destructive potential, and pave the way for a safer world for generations to come.

Join us on this captivating journey as we delve into fire spread modeling, unraveling the complexities, and forging a path toward controlling and taming the perils of fire. Together, we can revolutionize wildfire management, enhance urban planning, and strengthen disaster response, ensuring the resilience and well-being of our communities and environment.

## The Modeling Approach
### States:
EMPTY: Represents an empty cell.
TREE: Represents a cell with a tree.
BURNING: This represents a cell on fire.
BURNING_DURATION: This represents a cell that was burning and is now in the burning duration phase.
WATER: Represents a cell containing water.

### Probabilistic Rules:
The spread of fire from a tree to its neighboring cells depends on multiple factors, including burning neighbors and the probability of a lightning strike (p_lightning).
If the number of burning neighbors exceeds a certain threshold (threshold), a tree will catch fire.
The duration of the burning state (BURNING_DURATION) is probabilistic, where a tree has a 20% chance to remain burning and an 80% chance to turn back to an empty state.

### Additional Factors:
Tree growth: The forest is generated using the generate_forest function, where each cell has a probability (p_growth) of being a tree.
Lightning strikes: A random chance (p_lightning) determines if a tree catches fire due to a lightning strike.
Wind direction: The wind direction is represented by a tuple (wind_direction) indicating the movement in rows and columns.
Wind effects: The wind can influence the spread of fire by considering the cells affected by wind direction and speed (wind_speed).
Water bodies: Water bodies are generated using the generate_water_bodies function, which randomly selects an area and sets it as a water state (WATER). The edges of water bodies may have irregularities with a chance of becoming empty or tree cells.

## Libraries
`pygame`: This is a popular library for creating video games and graphical applications in Python. It provides functionality for handling graphics, user input, and event handling.
`random`: This is a built-in Python module that provides functions for generating random numbers and selecting random items from a sequence. It is used in this code to introduce randomness in generating the initial forest and water bodies.
`button`: This is a custom module or file that contains the implementation of a Button class. The Button class represents a clickable button in the user interface, and it is used to create buttons for starting, stopping, resetting the simulation, and changing the wind direction.

OTHER LIBRARIES NEEDED TO BE ADDED BECAUSE THE CODE WILL BE UPDATED FROM TIME TO TIME

## Current Research and Future Directions
Ongoing Research in Fire Spread Modeling using PCA:
- Real-time data integration
- Satellite imagery utilization
- Machine learning techniques

Recent Developments:
- Topography and vegetation density incorporation
- Real-life maps integration

Future Directions:
- Improved parameterization
- Enhanced computational efficiency
- Integration with other modeling approaches

## CONCLUSION
- Fire spread modeling using probabilistic cellular automata, particularly PCA-based approaches, is highly valuable for fire management and related fields.
- Benefits include capturing uncertainties, providing probabilistic forecasts, and supporting informed decision-making.
- Ongoing research focuses on integrating real-time data, satellite imagery, and machine learning techniques.
- Recent developments involve incorporating topography and vegetation density data, as well as utilizing real-life maps.
- Future directions include improved parameterization, enhanced computational efficiency, and integration with other modeling approaches.



## IN THIS CODE THE VARIABLE VALUES LIKE WIND DIRECTION, WIND SPEED, PROBABILITY OF GETTING STRUCT BY LIGHTNING, etc. CAN BE CHANGED AND A REAL-LIFE WORLD MAP HAS BEEN IMPLEMENTED, THOUGH THERE ARE SOME ERRORS IN THE CODE LIKE ONLY A PORTION OF THE WORLD MAP IS VISIBLE, I AM TRYING MY BEST TO IMPLEMENT THE CORRECTIONS AND IMPLEMENT NEW FEATURES LIKE MULTIDIRECTIONAL WINDS IN THE PROJECT, THIS CODE HAS BEEN TESTED ON MULTIPLE ALGORITHMS(the algorithms have been added in the repository) AND PROCESSES DESIGNED BY ME AND IT CONVERTS ANY PICTURE TO A MAP WITH SUITABLE CONDITIONS ACCORDING TO THE ALGORITHM OF THE CODE, WHICH WILL ENSURE BURNING OF THE FOREST AND THE DESIRED OUTPUT WILL BE SHOWN, PLEASE ENJOY THE WORK AND IT IS ONE OF THE BEST WORK DONE BY ME, ACTUALLY IS A SAMPLE MODEL AND THE FINAL VERSION WILL BE ESTABLISHED BY ME BEFORE 21ST JULY, 2023

























