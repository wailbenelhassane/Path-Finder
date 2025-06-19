# Search methods

import search


def run_search(search_method, problem):
    result, nodes_generated, nodes_visited, start, end = search_method(problem)

    # Printing of the results
    print("                                                     ")
    print(result.path())
    print(f"Nodos generados: {nodes_generated}")
    print(f"Nodos visitados: {nodes_visited}")
    print(f"Coste total del camino: {result.path_cost}")
    print(f"Duración de la búsqueda: {end - start} nanosegundos")

    print("                                                     ")


# List of problems for testing
problems = [
    ("De A a B", search.GPSProblem('A', 'B', search.romania)),
    ("De O a E", search.GPSProblem('O', 'E', search.romania)),
    ("De G a Z", search.GPSProblem('G', 'Z', search.romania)),
    ("De N a D", search.GPSProblem('N', 'D', search.romania)),
    ("De M a F", search.GPSProblem('M', 'F', search.romania)),
    ("De V a R", search.GPSProblem('V', 'R', search.romania))
]

# Searching Methods
search_methods = [
    ("Búsqueda en amplitud", search.breadth_first_graph_search),
    ("Búsqueda en profundidad", search.depth_first_graph_search),
    ("Búsqueda Branch and Bound (sin heurística)", search.branch_and_bound_priority),
    ("Búsqueda Branch and Bound (con heurística)", search.branch_and_bound_heuristicpriority)
]

# Execution of each problem
for title, problem in problems:
    print(f"\n{'-' * 10} {title} {'-' * 10}")
    for method_name, method in search_methods:
        print(f"\nMétodo: {method_name}")
        run_search(method, problem)
