class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        edges = defaultdict(list)

        for prerequisite in prerequisites:
            edges[prerequisite[1]].append(prerequisite[0])

        visited = set()

        def detect_cycle(c):
            if c in visited:
                return True
            
            visited.add(c)

            for post_c in edges[c]:
                if detect_cycle(post_c):
                    return True

            return False

        for c in edges:
            if c not in visited:
                cycle = detect_cycle(c)
                if cycle:
                    return False
        return True