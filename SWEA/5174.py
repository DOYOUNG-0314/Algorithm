def count_subtree(tree, node):
    count = 1  # 자기 자신
    for child in tree.get(node, []):
        count += count_subtree(tree, child)
    return count

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    
    tree = {}
    # 부모-자식 관계 구성
    for i in range(E):
        parent = edges[2*i]
        child = edges[2*i+1]
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)
    
    result = count_subtree(tree, N)
    print(f"#{tc} {result}")
