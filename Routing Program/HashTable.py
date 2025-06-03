# Source Citation: W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py

class HashTable:
    def __init__(self, size = 40):
        self.data_map = []
        for i in range(size):
            self.data_map.append([])

    def insert_item(self, key, value):
        # Hashes key to find index of bucket
        index = hash(key) % len(self.data_map)
        index_list = self.data_map[index]

        # Updates value if key already exists in bucket
        for k in index_list:
            if k[0] == key:
                k[1] = value
                return True
        # Otherwise insert into bucket
        item = [key, value]
        index_list.append(item)
        return True

    def get_item(self, key):
        # Hashes key to find index of bucket to search
        index = hash(key) % len(self.data_map)
        index_list = self.data_map[index]

        # Searches bucket of matching key and returns value
        for k in index_list:
            if k[0] == key:
                return k[1]
        return None
