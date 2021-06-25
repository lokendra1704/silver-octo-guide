import sys
def matchinglines(pattern, path):
    with open(path) as handle:
        for line in handle:
            if pattern in line:
                yield line.rstrip('\n')

def parse_log_records(lines):
    for line in lines:
        tag, msg = line.split(": ")
        return {"level": tag, "message":msg}

pattern, path = sys.argv[1], sys.argv[2]
matches = matchinglines(pattern, path) #matches is a generator object
type(matches)
for line in parse_log_records(matches): #Since matches is an generator object, it follows Iterator Protocol so it can be looped.
    print(line)