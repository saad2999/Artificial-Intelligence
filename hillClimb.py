def objective_function(x):
    return x**2

def generate_neighbors(x):
    return [x + 1, x - 1]




def hill_climbing(objective_function, initial_solution, max_iterations):
    current_solution = initial_solution
    best_solution = initial_solution
    best_value = objective_function(initial_solution)

    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_solution)
        neighbor_values = [objective_function(neighbor) for neighbor in neighbors]

        best_neighbor = neighbors[neighbor_values.index(max(neighbor_values))]
        best_neighbor_value = max(neighbor_values)

        if best_neighbor_value > best_value:
            current_solution = best_neighbor
            best_solution = current_solution
            best_value = best_neighbor_value
        else:
            break

    return best_solution, best_value

if __name__=="__main__":
  initial_solution = 0
  max_iterations = 100
  best_solution, best_value = hill_climbing(objective_function, initial_solution, max_iterations)
  print("Best solution:", best_solution)
  print("Best value:", best_value)

  

