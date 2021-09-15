def CountFrequency(my_list):
    freq = {}
    for items in my_list:
        freq[items] = my_list.count(items)
    for key,value in freq.items():
        print("% d : % d"%(key,value))
if __name__ == "__main__":
      my_list=[1,1,1,2,2,2,4,4,6,6,4,3,3,2,4,5,5,5,2,3,5,1,6]
      CountFrequency(my_list)
      
