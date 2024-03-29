collection = []

def ingest(input_string):
    collection.append(input_string)

def appearance(input_string):
    count = 0
    total_items = len(collection)

    for item in collection:
        if input_string in item:
            main = item.split(':')
            sub = input_string.split(':')
            matching_elements = 0

            for i in range(len(sub)):
                if sub[i] == main[i]:
                    matching_elements += 1
                else:
                    matching_elements = 0

                if matching_elements == len(sub):
                    count += 1
                    break

    appearance_ratio = count / total_items
    print(appearance_ratio)
    return appearance_ratio

#Time complexity: O(n*m), where n is the length of the collection, m is the length of the longest element in the collection
#Time complexity: O(n*m), where n is the length of the collection, m is the length of the longest element in the collection



