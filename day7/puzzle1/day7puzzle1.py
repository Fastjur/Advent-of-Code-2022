from typing import List
from enum import Enum

node_idx = 0


class NodeType(Enum):
    DIR = 'dir'
    FILE = 'file'


class Node:
    def __init__(self, node_type: NodeType, name: str, size: int, children: List['Node'] = None):
        if children is None:
            children = []
        if node_type == NodeType.DIR and size > 0:
            raise ValueError('Directories cannot have a size at initialization')
        if node_type == NodeType.FILE and size == 0:
            raise ValueError('Files must have a size')
        if node_type == NodeType.FILE and len(children) > 0:
            raise ValueError('Files cannot have children')
        self.node_type = node_type
        self.name = name
        self.size = size
        self.children = children
        global node_idx
        node_idx += 1
        self.idx = node_idx

    def get_size(self):
        if self.node_type == NodeType.FILE:
            return self.size
        else:
            return sum([child.get_size() for child in self.children])

    def __str__(self):
        return f'{self.name} ({self.idx}: {self.node_type}, size={self.get_size()}, #children={len(self.children)})'


def print_tree(node: Node, level: int = 0):
    print(f'{" " * level}- {node}')
    for child in node.children:
        print_tree(child, level + 1)


root_node = Node(NodeType.DIR, '/', 0, [])
current_dir_path = ['/']


def get_current_dir() -> Node:
    if len(current_dir_path) <= 0:
        return root_node
    res_dir = None
    for path in current_dir_path:
        print('path', path)
        if path == '/':
            res_dir = root_node
            continue
        found = False
        for child in res_dir.children:
            if child.node_type == NodeType.FILE:
                continue
            if child.name == path:
                res_dir = child
                found = True
                continue
        if not found:
            raise ValueError(f'Path {path} not found')
    print("res", res_dir)
    return res_dir


with open('input.txt', 'r') as f:
    lines = [line.strip().split() for line in f.readlines()]
    listing_dir = False
    for line in lines:
        print()
        print(line)
        print('current_dir_path', current_dir_path)
        print_tree(root_node)
        if listing_dir:
            if line[0] == '$':
                listing_dir = False
            else:
                current_dir = get_current_dir()
                if line[0] == 'dir':
                    current_dir.children.append(
                        Node(NodeType.DIR, line[1], 0, [])
                    )
                else:
                    file_size = int(line[0])
                    file_name = line[1]
                    current_dir.children.append(
                        Node(NodeType.FILE, file_name, file_size, [])
                    )

        if line[0] == '$':
            if line[1] == 'cd':
                current_dir = get_current_dir()
                if line[2] == '/':
                    current_dir_path = [root_node.name]
                elif line[2] == '..':
                    current_dir_path = current_dir_path[:-1]
                else:
                    try:
                        next(n for n in current_dir.children if n.name == line[2])
                        print("FOUND")
                    except StopIteration:
                        print("NOT FOUND, creating new dir")
                        new_dir = Node(NodeType.DIR, line[2], 0, [])
                        current_dir.children.append(new_dir)
                    current_dir_path.append(line[2])

            if line[1] == 'ls':
                listing_dir = True

print('\n\nFinal directory tree:')
print_tree(root_node)


def get_dirs_less_than_100000(node: Node) -> List[Node]:
    queue = [node]
    res = []
    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node.node_type == NodeType.FILE:
            continue
        if current_node.get_size() <= 100000:
            res.append(current_node)
        queue.extend(current_node.children)
    return res


dirs_less_than_100000 = get_dirs_less_than_100000(root_node)
print('dirs less than or equal 100000')
for d in dirs_less_than_100000:
    print(" -", d)

print('Sum of sizes of dirs less than or equal 100000')
print(sum([d.get_size() for d in dirs_less_than_100000]))
