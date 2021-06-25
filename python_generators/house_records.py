def house_records(path):
    with open(path) as lines:
        record = {}
        for line in lines:
            if line == '/n':
                yield record
                record = {}
                continue
            key, value = line.rstrip('/n').split(': ',1)
            record[key] = value
    yield record #Best Practice Alert! For the last record. Why we did this outside of with block? because It kind of ensures the file handle is closed before yielding the last record
