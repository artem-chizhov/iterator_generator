from func_generator import gen_list
from iter_class import iter_list

if __name__ == "__main__":
    
    test_list = [
        [1,2,3,4,5],
        ['test_data','test_data_2'],
        [True,False],
        [{'t_t':'ooops'}],
    ]
    print('***'*20)
    print(gen_list(test_list))
    for i in gen_list(test_list):
        print(i)
    print('***'*20)
    
    print(iter_list(test_list))
    for i in iter_list(test_list):
        print(i)
    print('***'*20)