class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.dirs = []
        self.files = []
        self.size = 0           # of files only, use get_size() for total
        self.parent = parent

    def __str__(self):
        return f"{self.name} ({self.size}) {{{self.dirs}}} {{{self.files}}}"

    def get_directory(self, change_to):
        for dir in self.dirs:
            if isinstance(dir, Dir) and dir.name == change_to:
                return dir
        raise ValueError(f'{change_to} could not be found in directory')

    def get_size(self):
        return sum([dir.get_size() for dir in self.dirs if isinstance(dir, Dir)]) + self.size


def get_commands():
    '''
        Splits input into terminal commands
    '''

    commands = []
    with open('day07-input.txt') as f:
        commands = f.read().split('\n$ ')

    commands[0] = commands[0][2:] # remove first '$ '
    commands = [x.splitlines() for x in commands]

    return commands

dirs_list = []

def part_one():
    '''
        Sums the total size of every directory that is less than or equal to 100000
    '''

    root = Dir('/', None)
    current = root

    dirs_list.append(root)

    for command in get_commands():
        if isinstance(current, Dir): # why do i need this
            cmd = command[0]
            output = command[1:]
            if cmd.startswith('cd'):
                change_to = cmd.split(' ')[1]
                if change_to == '/':
                    current = root
                elif change_to == '..':
                    current = current.parent
                else:
                    current = current.get_directory(change_to)
            elif cmd.startswith('ls'):
                for line in output:
                    components = line.split(' ')
                    if components[0] == 'dir':
                        new_dir = Dir(components[1], current)
                        current.dirs.append(new_dir)
                        dirs_list.append(new_dir)
                    else:
                        current.size += int(components[0])
                        current.files.append(line)

    return sum([dir.get_size() for dir in dirs_list if dir.get_size() <= 100000])

def part_two():
    '''
        Gets the smallest directory size we can delete that will free up enough space for the update
    '''

    disk_space = 70000000
    update = 30000000

    dirs_list.sort(key=lambda x: x.get_size())

    available_space = disk_space - dirs_list[-1].get_size()

    for dir in dirs_list:
        if available_space + dir.get_size() >= update:
            return dir.get_size()

if __name__ == "__main__":
    print(f"Day 7 part 1: {part_one()}")
    print(f"Day 7 part 2: {part_two()}")