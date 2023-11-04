import json
import sys

def find_key_in_dict(dict_obj, target_key):
    """
    Recursively search for a key in a nested dictionary.

    :param dict_obj: The dictionary to search.
    :param target_key: The key to search for.
    :return: The value of found key, or None if not found.
    """
    fvalues = []
    # If the target key is in the current level of the dictionary, return its value
    if target_key in dict_obj:
        fvalues.append(dict_obj[target_key])

    # If the value is another dictionary, recurse
    for key, value in dict_obj.items():
        if isinstance(value, dict):
            result = find_key_in_dict(value, target_key)
            if result is not None:
                fvalues+=result

    # If not found, return None
    if fvalues != []:
        return fvalues
    return None

if __name__ == '__main__':
    data_path = sys.argv[1]

    data = []
    try:
        with open(data_path, 'r') as analytics:
            lines = analytics.readlines()
            for l in lines:
                data.append(json.loads(l))
    except FileNotFoundError:
        print(f"Error: The file {data_path} does not exist.")
    
    dictionary = {}
    key_to_find = ['last_value_MaximumFCC','last_value_NominalChargeCapacity','last_value_CycleCount']
    for entry in data:
        for key in key_to_find:
            value = find_key_in_dict(entry, key)
            if value is not None:
                dictionary[key] = value[0]
    dictionary['real_percentage'] = dictionary['last_value_NominalChargeCapacity']/dictionary['last_value_MaximumFCC']*100


    print(f"\nMaximum FCC (original maximum capacity) : {dictionary['last_value_MaximumFCC']} mAh")
    print(f"Nominal Charge Capacity (current maximum capacity) : {dictionary['last_value_NominalChargeCapacity']} mAh")
    print(f"Cycle Count : {dictionary['last_value_CycleCount']} cycles")
    print(f"Relative to when it was new your battery capacity is : {dictionary['real_percentage']} %")