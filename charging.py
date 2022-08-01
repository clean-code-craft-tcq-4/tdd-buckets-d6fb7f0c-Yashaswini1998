def ranges_of_current(current_samples):
    current_samples_unique = [*set(current_samples)]
    samples_count = len(current_samples)
    unique_samples_count = len(current_samples_unique)
    length = 1
    list_of_ranges = []
    count_of_values_in_range = []
    if (samples_count == 0):
        return list_of_ranges
	
    current_samples.sort()
    for i in range (1, unique_samples_count + 1):
        count = 0
        if (i == unique_samples_count or current_samples_unique[i] - current_samples_unique[i - 1] != 1):
            if (length == 1):
                list_of_ranges.append(str(current_samples_unique[i - length]))
            else:
                temp = (str(current_samples_unique[i - length]) + " - " + str(current_samples_unique[i - 1]))
                list_of_ranges.append(temp)
                for j in range (samples_count):
                    if current_samples[j] >= current_samples_unique[i - length] and current_samples[j] <= current_samples_unique[i - 1]:
                        count += 1
                count_of_values_in_range.append(count)
            length = 1
        else:
            length += 1
    return list_of_ranges, count_of_values_in_range

def print_format(list_of_ranges, count_of_values_in_range):
    list_range_count = []
    for i in range(len(list_of_ranges)):
        temp = str(list_of_ranges[i]) + ", " + str(count_of_values_in_range[i])
        list_range_count.append(temp)
    return list_range_count

def charging_measurement(current_samples):
    list_of_ranges, count_of_values_in_range = ranges_of_current(current_samples)
    list_range_count = print_format(list_of_ranges, count_of_values_in_range)
    return list_range_count