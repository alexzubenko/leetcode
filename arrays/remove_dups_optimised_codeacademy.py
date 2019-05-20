# remove duplicates
# constant space
# return index of last unique element

def move_duplicates(dupe_list):
  print('initial list: ', dupe_list)
  index = 0
  count = 0
  index_to_check = 0
  length = len(dupe_list)
  while count < length-1:
    print('comparing {} with {}'.format(dupe_list[count], dupe_list[count+1]))
    if dupe_list[index_to_check] == dupe_list[index_to_check+1]:
      dupe_list.insert(length,dupe_list.pop(index_to_check))
      count +=1
    else:
      index_to_check += 1
      index+=1
      count+=1
  return index

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(move_duplicates(['a', 'a', 'g', 't', 't', 'x', 'x', 'x']), 3, move_duplicates(['a', 'a', 'g', 't', 't', 'x', 'x', 'x']) == 3))

# print("{0}\n should equal \n{1}\n {2}\n".format(move_duplicates(['a', 'a', 'c', 'c', 'd', 'd', 'e', 'e', 'f']), 4, move_duplicates(['a', 'a', 'c', 'c', 'd', 'd', 'e', 'e', 'f']) == 4))
#
# print("{0}\n should equal \n{1}\n {2}\n".format(move_duplicates([13, 13, 13, 13, 13, 42]), 1, move_duplicates([13, 13, 13, 13, 13, 42]) == 1))