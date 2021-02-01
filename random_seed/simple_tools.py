def list_sum(the_list):
    _sum = 0
    try:
        for i in the_list:
            _sum += i
        return _sum
    except Exception as e:
        print(e)
