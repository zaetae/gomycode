def binary_search(sequence,item):
    begin_index=0
    end_index=len(sequence)-1
    while begin_index<=end_index:
        midpoint=begin_index + (end_index-begin_index)//2
        midpoint_value=sequence[midpoint]
        if midpoint_value==item:
            return True
        elif item<midpoint_value:
            end_index=midpoint-1
        else:
            begin_index=midpoint+1
    return False
sequence_a=[4,5,6,8,9,10,11,12,13,14,15,16]
item_a=4
print(binary_search(sequence_a,item_a))