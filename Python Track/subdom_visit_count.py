class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        track = defaultdict(int)
        for domains in cpdomains:
            freq , dom = domains.split()
            freq = int(freq)
            track[dom] += freq

            subdomains = dom.split(".")
            for i in range(1, len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                track[subdomain] += freq

        return ["{} {}".format(v, k) for k, v in track.items()]
