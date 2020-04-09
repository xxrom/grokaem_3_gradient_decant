input = 0.5
weight = 2
alpha = 0.9
pred_goal = 0.234

# learning =)
for iteration in range(40):
  pred = input * weight
  # cube error (for measurement)
  cubeError = (pred - pred_goal)**2

  # derivative f(x) =(k*x) => f(x)'= k => k ~~~ input * (pred - pred_goal) ???)
  weight_delta = input * (pred - pred_goal)
  # change delta with multiping on alpha coefficient
  weight -= weight_delta * alpha

  print('cubeError: %.04f, pred: %.04f, weight_delta: %.04f' % (cubeError, pred, weight_delta))
