import numpy as np
class WeatherMath:

    def getTemperatureAmplitude(list_of_temperatures):
        """
        Calculates the temperature amplitude, which is the difference between the maximum and minimum temperatures in a list.

        Args:
        - list_of_temperatures: A list of numerical temperatures.

        Returns:
        - The temperature amplitude as a float.
        """
        amplitude = abs(max(list_of_temperatures) - min(list_of_temperatures))
        return amplitude

    def getShiftingList(list_of_data):
        """
        Generates a list of shifts in data values, which indicate whether each subsequent value in the list is higher or lower than the previous one.

        Args:
        - list_of_data: A list of numerical data values.

        Returns:
        - A numpy matrix containing the original data values along with their corresponding shifts (-1, 0, or 1).
        """
        shifting = [0]
        list_of_data = np.array(list_of_data) # convert list to numpy array for easier manipulation
        for i in range(len(list_of_data)-1): # loop over array elements up to second-to-last element
            if list_of_data[i+1] > list_of_data[i]:
                shifting.append(1)
            elif list_of_data[i+1] < list_of_data[i]: # fixed syntax error here, used elif instead of if
                shifting.append(-1)
            else:
                shifting.append(0)

        list_of_data = np.vstack((list_of_data,shifting)) # concatenate original data with shifts along the vertical axis

        return list_of_data
