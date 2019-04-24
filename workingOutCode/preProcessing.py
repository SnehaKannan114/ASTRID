def dataCleanup(data):
    
    for i in range(len(data['method'].values)):
        if data['method'].values[i] == "GET":
            data['method'].values[i] = 0
        elif data['method'].values[i] == "POST":
            data['method'].values[i] = 1
        elif data['method'].values[i] == "PUT":
            data['method'].values[i] = 8
        else:
            data['method'].values[i] = -1

    for i in range(len(data['label'].values)):
        if data['label'].values[i] == "anom":
            data['label'].values[i] = 0
        elif data['label'].values[i] == "norm":
            data['label'].values[i] = 1
        else:
            data['label'].values[i] = -1

    for i in range(len(data['protocol'].values)):
        if data['protocol'].values[i] == "HTTP/1.1":
            data['protocol'].values[i] = 0
        else:
            data['protocol'].values[i] = -1

    for i in range(len(data['pragma'].values)):
        if data['pragma'].values[i] == "no-cache":
            data['pragma'].values[i] = 0
        else:
            data['pragma'].values[i] = -1

    for i in range(len(data['cacheControl'].values)):
        if data['cacheControl'].values[i] == "no-cache":
            data['cacheControl'].values[i] = 0
        else:
            data['cacheControl'].values[i] = -1


    for i in range(len(data['connection'].values)):
        if data['connection'].values[i] == "close":
            data['connection'].values[i] = 0
        elif data['connection'].values[i] == "keep-alive":
            data['connection'].values[i] = 1
        else:
            data['connection'].values[i] = -1

    for i in range(len(data['contentLength'].values)):
        if data['contentLength'].values[i] == "null":
            data['contentLength'].values[i] = -100
        else:
            data['contentLength'].values[i] = int(data['contentLength'].values[i])
        
    for i in range(len(data['contentType'].values)):
        if data['contentType'].values[i] == "null":
            data['contentType'].values[i] = 0
        else:
            data['contentType'].values[i] = -1