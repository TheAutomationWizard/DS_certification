from collections import Counter

origianl_string = 'totmtaptat'
substring = 'tta'


def min_Window_Substring(original_string, lookup_string):
    # character_map = dict(Counter(lookup_string))
    character_map = {key: lookup_string.count(key) for key in set(lookup_string)}
    all_possible_substrings = []
    counter = len(character_map)
    substring_char_map = {}
    right_index = left_index = required_letters = 0
    possible_strings = -1
    while left_index < len(original_string):
        if original_string[right_index] in lookup_string:
            if original_string[right_index] in substring_char_map.keys():
                substring_char_map[original_string[right_index]] = substring_char_map[original_string[right_index]] + 1
            else:
                substring_char_map[original_string[right_index]] = 1
            if character_map[original_string[right_index]] == substring_char_map[original_string[right_index]]:
                required_letters += 1

        if required_letters == counter:
            possible_strings += 1
            all_possible_substrings.insert(possible_strings, original_string[left_index:right_index+1])

            while left_index < right_index:
                if original_string[left_index] in lookup_string:
                    substring_char_map[original_string[left_index]] = substring_char_map[original_string[left_index]] - 1
                    if character_map[original_string[left_index]] > substring_char_map[original_string[left_index]]:
                        required_letters -= 1
                        left_index += 1
                        break
                all_possible_substrings[possible_strings] = original_string[left_index+1:right_index + 1]
                left_index += 1

        if right_index == len(original_string)-1:
            break
        right_index += 1

    # return list_of_solutions
    return sorted(all_possible_substrings, key=len)[0]







print(min_Window_Substring(origianl_string, substring))
print(min_Window_Substring('ADOBECODEBANC', 'ABC'))
print(min_Window_Substring('this is a test string', 'tist'))
print(min_Window_Substring('geeksforgeeks', 'ork'))
