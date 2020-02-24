def string_to_list(string):
    res_list = string.split(',')
    res_list = [x.strip() for x in res_list]
    return res_list

def list_to_string(lst):
    return ',   '.join(lst)

def most_common(lst): 
    return max(set(lst), key = lst.count) 