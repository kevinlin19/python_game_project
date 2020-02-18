# Sudoku w/ backtracking algorithm
利用backtracking algorithm去解數獨
## backtracking algorithm

回溯法，運用遞迴依序窮舉各個維度的數值，製作所有可能的多維度數值，並且在遞迴途中避免枚舉不正確的多維度數值。回溯法的特色是隨時避免枚舉不正確的數值。一旦發現不正確的數值，就不遞迴至下一層，而是回溯至上一層，節省時間。

因為數獨總共有9*9=81格，每隔有1~9的數字可以填，若用暴力窮舉法會有9^81個數字要嘗試!!非常暴力，所以數獨很多人推薦用backtracking，甚至leetcode也有這個考題([37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
)有興趣的人可以去寫寫看!!

## Reference
- http://www.csie.ntnu.edu.tw/~u91029/Backtracking.html
- https://www.youtube.com/watch?v=DKCbsiDBN6c