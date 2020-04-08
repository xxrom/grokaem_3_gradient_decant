weight = 0.0
goal_pred = 0.8
input = 1.1

for interation in range(4):
  pred = input * weight
  error = (pred - goal_pred) ** 2
  delta = pred - goal_pred

  # derivative [производная] (how fast changed error by changing weight)
  weight_delta = delta * input
  # Minus because derivative show opposite direction
  weight = weight - weight_delta

  print('error:  %.04f, prediction: %.04f, delta: %.04f'%(error, pred, delta))