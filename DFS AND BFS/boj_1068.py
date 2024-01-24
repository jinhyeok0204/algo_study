from collections import Counter
def main():
    n = int(input())
    parent_node = list(map(int, input().split()))

    graph = [[] for _ in range(n)]

    for i in range(n):
        if parent_node[i] != -1:
            graph[parent_node[i]].append(i)
    print("graph:")
    print(graph)

    k = int(input())
    removed_child = graph[k]  # list
    remove_list = [k] + removed_child
    for each in removed_child:
        if graph[each]:
            for r in graph[each]:
                if r not in remove_list:
                    remove_list.append(r)

    #print(remove_list)

    result_graph = []
    for i in range(n):
        if i not in remove_list:
            result_graph.append(graph[i])

    #print(result_graph)

    count = 0
    for each in result_graph:
        if len(each) == 0:
            count += 1

    print(count)


main()
