import itertools
max_square, num_dice = map(int, input().split())
squares = [list(map(int, f"{k*k:0{num_dice}d}")) for k in range(1, max_square + 1)]
dice_perms = list(itertools.permutations(range(num_dice)))
dice_combs = list(map(set, itertools.combinations(range(10), 6)))

def check_digit(dice, digit):
    return digit in dice or (digit in [6, 9] and (6 in dice or 9 in dice))

if num_dice == 1:
    print(sum(all(check_digit(dice_combs[i], square[0])
                  for square in squares)
              for i in range(len(dice_combs))))
if num_dice == 2:
    print(sum(all(any(check_digit(dice_combs[dice_perm[0]], square[0])
                      and check_digit(dice_combs[dice_perm[1]], square[1])
                      for dice_perm in itertools.permutations((i,j)))
                  for square in squares)
              for i in range(len(dice_combs))
              for j in range(i, len(dice_combs))))
if num_dice == 3:
    print(sum(all(any(check_digit(dice_combs[dice_perm[0]], square[0])
                      and check_digit(dice_combs[dice_perm[1]], square[1])
                      and check_digit(dice_combs[dice_perm[2]], square[2])
                      for dice_perm in itertools.permutations((i,j,k)))
                  for square in squares)
              for i in range(len(dice_combs))
              for j in range(i, len(dice_combs))
              for k in range(j, len(dice_combs))))    
