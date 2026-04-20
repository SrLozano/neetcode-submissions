class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        edges = defaultdict(list)

        for prerequisite in prerequisites:
            edges[prerequisite[1]].append(prerequisite[0])

        print(edges)
        visited = set()

        def detect_cycle(c, path):
            nonlocal visited
            if c in visited:
                return False
            if c in path:
                return True
            visited.add(c)
            path.add(c)

            for post_c in edges[c]:
                print(f"estamos en c: {c} y en {post_c}")
                if detect_cycle(post_c, path):
                    print(f"detectado ciclo en: {c}, {post_c}, {path}")
                    return True

            return False

        for c in range(numCourses):
            if c not in visited:
                path = set()
                cycle = detect_cycle(c, path)
                if cycle:
                    return False
        return True