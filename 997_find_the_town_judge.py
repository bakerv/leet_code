class Solution:
    def findJudge(self, n: int, trust) -> int:
        votes = {}
        most_votes = 0
        judge = 1
        who_voted = set()
        for ballot in trust:
            # track people that have cast a vote of trust
            who_voted.add(ballot[0])

            # tally votes of trust
            candidate = ballot[1]
            if candidate not in votes:
                votes[candidate] = 1
            else:
                votes[candidate] += 1

            # update judge tracker to person with  most votes
            if votes[candidate] > most_votes:
                most_votes = votes[candidate]
                judge = candidate

        # determine if anyone is eligible to be the judge
        if n - 1 == most_votes and judge not in who_voted:
            return judge
        else:
            return -1










Test = Solution()
print(Test.findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]
))