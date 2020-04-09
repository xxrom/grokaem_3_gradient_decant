weight = 0.5
goal_pred = 0.8
input = 2
alpha = 1

# Discrepancy effect (error getting bigger and bigger)
for interation in range(100):

  pred = input * weight * alpha
  error = (pred - goal_pred) ** 2
  delta = pred - goal_pred

  # derivative [производная] (how fast changed error by changing weight)
  weight_delta = delta * input
  # Minus because derivative show opposite direction
  weight = weight - weight_delta

  alpha = alpha * 0.9

  print('error:  %.04f, prediction: %.04f, delta: %.04f, alpha; %.04f'%(error, pred, delta, alpha))