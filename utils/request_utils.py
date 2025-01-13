def set_request_data_mutable(request, key, value):
    """
    Set a specific key-value pair in the request data, ensuring the data is mutable.
    """
    # Remember old state
    _mutable = request.data._mutable
    # Set to mutable
    request.data._mutable = True
    # Change the values you want
    request.data[key] = value
    # Set mutable flag back
    request.data._mutable = _mutable

    return request