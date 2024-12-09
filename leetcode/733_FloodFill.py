from typing import List


class Solution:
    def floodFill(self,image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            self.dfs(image, sr, sc, color, image[sr][sc])
        return image

    def dfs(self,image, i, j, color, initial):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != initial:
            return
        if image[i][j] == initial:
            image[i][j] = color
        self.dfs(image, i - 1, j, color, initial)
        self.dfs(image, i + 1, j, color, initial)
        self.dfs(image, i, j - 1, color, initial)
        self.dfs(image, i, j + 1, color, initial)

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(Solution.floodFill(image, sr, sc, color))