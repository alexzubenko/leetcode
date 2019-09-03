class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(array_size)]

    def hash_function(self, key, number_collisions=0):
        return sum(key.encode()) + number_collisions

    def compressor(self, has_value):
        return has_value % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash_function(key))
        curretn_array_value = self.array[array_index]

        if curretn_array_value is None:
            self.array[array_index] = [key, value]
            return
        if curretn_array_value[0] == key:
            self.array[array_index] = [key, value]
            return
        else:
            print('Got the collision here, resolving...')
            number_collisions = 1
            # while curretn_array_value[0]!=key:
            while True:
                new_hash_value = self.hash_function(key, number_collisions)
                new_array_index = self.compressor(new_hash_value)
                new_possible_value = self.array[new_array_index]
                if new_possible_value is None:
                    self.array[new_array_index] = [key, value]
                    return
                elif new_possible_value[0] == key:
                    self.array[new_array_index] = [key, value]
                    return
                else:
                    number_collisions += 1
        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash_function(key))
        possible_return_value = self.array[array_index]
        if possible_return_value is None:
            return None
        if possible_return_value[0] == key:
            return possible_return_value[1]
        else:
            print('Got the collision here during retrieval, resolving...')
            retrieval_collision = 1
            # while possible_return_value[0]!=key:
            while True:
                new_hash_value = self.hash_function(key,retrieval_collision)
                new_array_index = self.compressor(new_hash_value)
                new_possible_value = self.array[new_array_index]
                if new_possible_value is None:
                    return None
                elif new_possible_value[0] == key:
                    return new_possible_value[1]
                else:
                    retrieval_collision +=1




hash_map = HashMap(4)
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')
hash_map.assign('gneiss2', 'metamorphic2')
print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))

# hash_map = HashMap(5)
# # print(hash_map.array)
# hash_map.assign('key', 'value')
# print(hash_map.array)
# # print(hash_map.retrieve('key2'))
# hash_map.assign('key2', 'value')
# print(hash_map.array)