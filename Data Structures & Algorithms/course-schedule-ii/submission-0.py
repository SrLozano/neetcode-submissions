class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = defaultdict(list)
        for c, prt in prerequisites:
            preMap[c].append(prt)
        
        visited = []

        def dfs(c):
            # True if cycles
            nonlocal visited
            if preMap[c] == [] and c not in visited:
                visited.append(c)
            
            for preR in preMap[c]:
                if dfs(preR):
                    return True

            preMap[c] = []
            visited.append(c)

            return False


        for c in range(numCourses):
            if c not in visited:
                if dfs(c):
                    # there are cycles
                    return []
                    
        return visited

